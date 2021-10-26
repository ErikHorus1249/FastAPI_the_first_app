from fastapi import FastAPI
from features import MAIL
# khơi tạo web app 
app = FastAPI()

# Xây dựng api đầu tiên
# root
@app.get("/")
def get_root():
    return {'data':'this is root dir'}
    # {key}
    # json 
    # localhost:5500/

# URL 
@app.get("/home")
def get_homepage():
    return "This is a homepage   !"


# truy xuất  query xác định bằng 1 dấu hỏi 
# get / post / push / delete  - method request 

@app.get("/calculator")
def calculator(a: int , b: int):
    return {"data": a + b}

# gửi mail
# GET PUSH DELETE - method  
@app.get("/login_get")
def login_with_get_method(pwd: str, user_name: str):
    return {"login": {"user_name": user_name, "password": pwd, "method": "get"}}

# host  -> URL: http://localhost:8000/home
# https://vi.wikipedia.org/wiki/URL
# protocol 

@app.get("/send_mail")
def send_email_for_client(receiver: str, content: str, subject: str):
    status = MAIL.send_mail(receiver, content, subject)
    if status:
        return {"receiver": receiver,"sent": status}
    else:
        return {"sent": status}
