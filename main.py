from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import aiofiles
from fastapi.middleware.cors import CORSMiddleware
from Routes.Sensor import sensor

# init app with fast api  
app = FastAPI()

# static dir registry 
# app.mount("/Media", StaticFiles(directory="Media"), name="Media")

# set_up CORS middleware 
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# route API 
app.include_router(sensor)

