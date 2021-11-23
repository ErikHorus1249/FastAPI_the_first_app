# Su dung python cho viec dung mot trang web

## Bước 0: chuẩn bị:
+ Khởi tạo git repo
+ chuẩn bị file và thư mục như đã có : main.py, README.md, requirements.txt
- main.py : code nội dung web app
- README mô tả về dự án 
- requirement để liệt kê các thư viện sử dung cho dự án
+ Cài đặt thư viện
hai thư viện: Fastapi, Urvicon:
`$ pip install fastapi`
`$ pip install uvicorn`
+ ghi các thư viện ra requirement file

`$ pip freeze > requirements.txt`

## Bước 1:
Chạy:

`$ uvicorn main:app --reload`


`$ pip install aiofiles`

`$ pip install python-multipart`

`$ pip install gunicorn`