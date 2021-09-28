from fastapi import FastAPI

# khơi tạo web app 
app = FastAPI()

# Xây dựng api đầu tiên
# root
@app.get("/")
def get_root():
    return {'data':'this is root dir'}
    # json 

@app.get("/home")
def get_homepage():
    return "This is a Homepage !"