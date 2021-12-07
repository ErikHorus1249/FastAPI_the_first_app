from fastapi import FastAPI, Request, File, UploadFile
from features import MAIL
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import aiofiles
from fastapi.middleware.cors import CORSMiddleware

# khơi tạo web app 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# static dir registry 
app.mount("/media", StaticFiles(directory="media"), name="media")

# khoi tao bien template 
templates = Jinja2Templates(directory="media/templates")

# Xây dựng api đầu tiên
# root
@app.get("/")
def get_root():
    # Json 
    # return {'data':'this is root dir'}
    # String 
    return "this is root dir"


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
    return templates.TemplateResponse("ajax.html", {"request": request})

@app.get("/form2")
def get_demo_form(request: Request):
    return templates.TemplateResponse("index1.html", {"request": request})

# upload file 
@app.post("/files")
async def upload_file(upload_file: UploadFile = File(...)):
    # tao bien de lu ten file 
    file_name = upload_file.filename
    # khai bao noi luu tru 
    # media/main.png 
    file_path = f"media/{file_name}"
    # file_path = "media/" + file_name
    # wb - write binary 
    async with aiofiles.open(file_path, "wb") as file_handler:
        content = upload_file.read();
        file_handler.write(content)
        
    return {"status": True}
