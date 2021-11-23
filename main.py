from fastapi import FastAPI, Request, File, UploadFile
from features import MAIL
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import aiofiles

# khơi tạo web app 
app = FastAPI()

# static dir registry 
app.mount("/media", StaticFiles(directory="media"), name="media")

# khoi tao bien template 
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
# @app.get("/template")
# def get_demo_template(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

@app.get("/form")
def get_demo_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/form2")
def get_demo_form(request: Request):
    return templates.TemplateResponse("index1.html", {"request": request})

@app.post("/files")
async def upload_file(upload_file: UploadFile = File(...)):
    file_name = upload_file.filename
    file_path = f"media/{file_name}"
    async with aiofiles.open(file_path, "wb") as file_handler:
        content = upload_file.read();
        file_handler.write(content)
        
    return {"status": True}
