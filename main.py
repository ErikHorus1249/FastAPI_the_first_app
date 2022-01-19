from email import header
from fastapi import FastAPI, Request
from features import *
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import requests

from features import Connect

# init app 
app = FastAPI()


# root 
@app.get("/")
def get_root():
    return {'data':'this is root dir'}


@app.get("/get_images")
def get_token(username: str, password: str, domain: str):
    token = Connect.get_admin_token(username, password, domain)
    images = Connect.get_image_list(token)['images']
    for image in images:
        print(image['id']+" "+image['name'])
    return True

    