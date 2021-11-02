from fastapi import FastAPI, Request
from features import MAIL
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# khơi tạo web app 
app = FastAPI()

templates = Jinja2Templates(directory="templates")
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


# URL 
@app.get("/template")
def get_demo_template(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    