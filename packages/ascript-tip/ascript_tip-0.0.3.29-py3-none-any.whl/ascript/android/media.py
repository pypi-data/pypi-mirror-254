
from airscript.system import Media as asMedia

def volume(percent:int,type:int =3):
    asMedia.volume(percent,type)

def talk(msg:str):
    asMedia.talk(msg)

def play(path:str,callback=None):
    if callback:
        asMedia.play(path,callback)
    else:
        asMedia.play(path)

def recode(path:str,time=None):
    if time:
        return asMedia.recode(path,time)
    else:
        return asMedia.recode(path)

def vibrate(time:int=200):
    asMedia.vibrate(time)



