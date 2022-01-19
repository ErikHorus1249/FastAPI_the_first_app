from email import message
from http import server
from os import stat
from Features.Google import Create_Service
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64

CLIENT_SECRET_FILE = 'credentials/client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']


# ham chuc mail 
def send_mail(receiver: str, content: str, subject: str):
    # khoi tao dich vu 
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # Thông điệp muốn gửi  - email body
    emailmasg = content
    mineMessage = MIMEMultipart()
    # địa chỉ mail người nhận 
    mineMessage['to'] = receiver
    # subject của email 
    mineMessage['subject'] = subject
    mineMessage.attach(MIMEText(emailmasg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mineMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

    labels = message['labelIds']

    if "SENT" in labels:
        return True
    else:
        return False

