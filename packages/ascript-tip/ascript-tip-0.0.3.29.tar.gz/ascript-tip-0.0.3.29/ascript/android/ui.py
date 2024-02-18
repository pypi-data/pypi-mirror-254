import time

from airscript.ui import Window as asWindow
from airscript.ui.dialog import toast as astoast
from airscript.ui.dialog import alert as asalert
from airscript.ui.dialog import confirm as asconfirm
from airscript.ui.dialog import promat as aspromat
from airscript.ui import Float  as asFloat

class WebWindow:
    def __init__(self,html:str,tunnel =None):
        super().__init__()
        if tunnel:
            self.window = asWindow(html,tunnel)
        else:
            self.window = asWindow(html)

    def mode(self,mode:int=0):
        self.window.model(mode)

    def tunner(self,fun):
        self.window.model(fun)

    def size(self,width=None,height=None):
        if width:
            self.window.width(width)

        if height:
            self.window.height(height)

    def background(self,color:str):
        self.window.background(color)

    def drag(self,is_drag:bool=False):
        self.window.drag(is_drag)

    def dim_amount(self,dim:float=0.5):
        self.window.dimAmount(dim)

    def gravity(self,gravity:int=None,offset_x:int=None,offset_y:int=None):
        if gravity:
            self.window.gravity(gravity)
        if offset_x:
            self.window.x(offset_x)

        if offset_y:
            self.window.y(offset_y)

    def show(self):
        self.window.show()

    def close(self):
        self.window.close()

    def call(self,js:str):
        self.window.call(js)

class Dialog:
    @staticmethod
    def toast(msg,dur=3000,gravity=1|16,x=0,y=0.2):
        astoast(msg,dur,gravity,x,y)

    @staticmethod
    def alert(msg:str,submit:str="确认"):

        _res = []
        def tunner(k,v):
            if k =='__alert':
                _res.append(True)

        asalert(msg, tunner, submit)

        while len(_res)<1:
            time.sleep(0.5)
        return True

    @staticmethod
    def confirm(msg:str, title:str =None, submit:str="确认", cancel:str= "取消"):
        win =  asconfirm(msg)
        if title:
            win.title(title)

        __res = []
        def tunner(k,v):
            if k == "__confirm":
                if v == "sure":
                    __res.append(True)
                else:
                    __res.append(False)

        win.submit(submit)
        win.cancle(cancel)
        win.show(tunner)

        while len(__res) <1:
            time.sleep(0.5)

        return __res[0]

    @staticmethod
    def prompt(msg:str= "请输入信息", title:str=None, value:str=None, hint:str=None, submit:str= "确认", cancel:str= "取消"):
        win = aspromat(msg)
        if title:
            win.title(title)

        __res = []

        def tunner(k, v):
            if k == "__promat":
                if v == "cancle":
                    __res.append(False)
                else:
                    __res.extend([True,v])

        win.value(value)
        win.hint(hint)
        win.submit(submit)
        win.cancle(cancel)
        win.show(tunner)

        while len(__res) <1:
            time.sleep(0.5)

        if __res[0]:
            return __res[1]

        return None


class Loger(WebWindow):
    pass

class FloatWindow:
    @staticmethod
    def hide():
        asFloat.hide()

    @staticmethod
    def show(x:float=None,y:float=None,dim:float=None):
        if x and y:
            asFloat.show(x,y)
        elif x and y and dim:
            asFloat.show(dim,x, y)
        elif dim:
            asFloat.show(dim)






