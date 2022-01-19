from fastapi import FastAPI
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from Routes.Sensor import sensor
import os

# start app 
app = FastAPI()

# set_up static file 
app.mount("/Media", StaticFiles(directory="Media"), name="Media")

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
