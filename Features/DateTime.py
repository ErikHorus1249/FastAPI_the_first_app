import datetime
import time 

def getNow():
    x = datetime.datetime.now()
    return f'{x.hour}:{x.minute}:{x.second}:'
    
def getUpdateTime():
    return str(datetime.datetime.now())
    
def now():
    return round(time.time(), 1)

def getNotice(mess):
    print(f'[+]{getNow()} {mess}')