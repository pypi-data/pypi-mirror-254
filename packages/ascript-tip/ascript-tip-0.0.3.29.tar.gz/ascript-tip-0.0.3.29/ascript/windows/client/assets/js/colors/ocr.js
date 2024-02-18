var ocrMarks = null;
var ocrres_itemdom = $(".ocr_item_dom");

$(document).ready(function () { 
    makeOcrStr();
    $("#ocr_test").click(function(e){
        clearmarks();
        $("#ocr_test_loading").show();

        ocrDao.img_path = $(image).attr("path")

        $.ajax({
            url: fun_findocr,
            type:'POST',
            contentType:'application/json',
            dataType:'json',
            data:JSON.stringify(ocrDao),
            async: true,
            success: function (res) {
                $("#ocr_test_loading").hide();
                $("#findcolor_res_reset").show();
                $("#findcolor_res").text(res.data.length)
                $("#findcolor_res").show();
                
                
                ocrMarks = res.data;
                
                res.data.forEach((item,index,arr)=>{
                    var idom = ocrres_itemdom.clone(true);
                    idom.find(".ocr_item_dom_text").text(`${item.text}`)
                    var conf = item.confidence+"";
                    idom.find(".conf").text(conf.substring(0,4));
                    idom.find(".rect").text(item.region_position[0][0]+","+item.region_position[0][1]+","+item.region_position[2][0]+","+item.region_position[2][1]);
                    $(idom).addClass("ocr_item_dom"+index);
                    $(idom).appendTo("#ocr_reslist");

                    $(idom).on('mouseover', function() {
                        $(idom).addClass("list-group-item-success");
                        $(`.ocr_marks${index}`).addClass("ocr_markshover")
                        $(`.ocr_marks${index}`).addClass("shadow-dark-lg")
                        
                    });

                    $(idom).on('mouseout', function() {
                        $(idom).removeClass("list-group-item-success");
                        $(`.ocr_marks${index}`).removeClass("ocr_markshover")
                        $(`.ocr_marks${index}`).removeClass("shadow-dark-lg")
                    });

                    $(idom).click(function(e){
                        makeOcrStr()
                    });

                    idom.find(".ocr_item_dom_text").click(function(e){
                        $("#input_ocr_mathcer").val(idom.find(".ocr_item_dom_text").text());
                    });

                    idom.find(".rect").click(function(e){
                        // --更改识别范围
                        var p_left= item.region_position[0][0] -5;
                        var p_top= item.region_position[0][1] -5;
                        var p_right= item.region_position[2][0] +5;
                        var p_bottom= item.region_position[2][1] +5;

                        scope_pos[0] = {
                            x:p_left,
                            y:p_top
                        }

                        scope_pos[1] = {
                            x:p_right,
                            y:p_bottom
                        }

                        $(part_box).show();

                        changeImageMarkSize();

                        // changeBoxRect();
                    })

                    idom.find(".conf").click(function(e){
                        // -- 更改识别可信度
                        $("#input_ocr_similar").val(conf.substring(0,4))
                        
                    })

                    // add mark 
                    var markDom =  $(`<div class="ocr_marks${index} ocr_marks"></div>`);
                    markDom.appendTo("#ocr_res")

                    $(markDom).click(function(e){
                        $("#input_ocr_mathcer").val($(`.ocr_item_dom${index}`).find(".ocr_item_dom_text").text());
                        makeOcrStr()
                    });

                    $(markDom).on('mouseover', function() {
                        $(`.ocr_item_dom${index}`).addClass("list-group-item-success");
                        $(markDom).addClass("ocr_markshover")
                        $(markDom).addClass("shadow-dark-lg")
                        let top = $(`.ocr_item_dom${index}`).offset().top - $(`#ocr_res_con`).offset().top;
                        top = $(`#ocr_reslist`).scrollTop()+top;
                        // let pt =  $(`.ocr_item_dom${index}`).posation().top
                        $(`#ocr_reslist`).scrollTop(top);
                    });

                    $(markDom).on('mouseout', function() {
                        $(`.ocr_item_dom${index}`).removeClass("list-group-item-success");
                        $(markDom).removeClass("ocr_markshover")
                        $(markDom).removeClass("shadow-dark-lg")
                    });

                });
                // $('.findres').modal('show')
                changeImageMarkSize();
            },
            error: function (err) {
              $("#ocr_test_loading").hide();
              alert(err)
            }
          })
    });
});

var ocrDao = {
    rect:null,
    confidence:null,
    pattern:null
};

function makeOcrStr(){
    ocrDao = {};
    var ocrStr = "Ocr()"
    var rectStr = "";
    var patternStr = "";
    var confidenceStr = "";
    var max_side = ""

    var params = []

    if(scope_pos[0]!=null && scope_pos[1]!=null){
        ocrDao.rect =[scope_pos[0].x,scope_pos[0].y,scope_pos[1].x,scope_pos[1].y];
        rectStr = `rect = [${scope_pos[0].x},${scope_pos[0].y},${scope_pos[1].x},${scope_pos[1].y}]`
        params.push(rectStr)
    }

    if($("#input_ocr_max_slid").val().length>0){
        if($("#input_ocr_max_slid").val() !="0"){
            max_side = `max_side_len = ${$("#input_ocr_max_slid").val()}`
            params.push(max_side)
        }
        
        ocrDao.max_side_len = $("#input_ocr_max_slid").val();
    }

    if($("#input_ocr_mathcer").val().length>0){
        patternStr = `pattern ="${$("#input_ocr_mathcer").val()}"`
        params.push(patternStr)
        ocrDao.pattern = $("#input_ocr_mathcer").val();
    }

    if($("#input_ocr_similar").val().length>0){
        if($("#input_ocr_similar").val()!='0.1'){
            confidenceStr = `confidence = ${$("#input_ocr_similar").val()}`
            ocrDao.confidence = $("#input_ocr_similar").val();
            params.push(confidenceStr)
        }


    }

    // if($("#input_ocr_model_path").val().length>0){
    //     if($("#input_ocr_model_path").val() !="默认"){
    //         ocrStr = `Ocr("${$("#input_ocr_model_path").val()}")`
    //         ocrDao.model = $("#input_ocr_model_path").val();
    //     }
    // }



    if(ocr_type=="find_all"){
        
    }else{
        ocr_type = "find"
    }

    ocrDao.findtype = ocr_type;

    var params_str = ""

    for (let i = 0; i < params.length; i++) {
        if(i==0){
            params_str = params_str + params[i];
        }else{
            params_str = params_str+","+params[i];
        }
    }

    document.getElementById("ocrc_ode_input").value = `Ocr(${params_str}).${ocr_type}()`;

}

