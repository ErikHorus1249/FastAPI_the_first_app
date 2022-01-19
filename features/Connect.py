import requests
import json

URL = "http://203.162.130.73"

def get_admin_token(username: str, password: str, domain: str):
    url = f'{URL}:5000/v3/auth/tokens'
    header = {'Content-Type': 'application/json'}
    data = { "auth": {
                "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                    "name": username,
                    "domain": { "id": domain },
                    "password": password
                    }
                }
                }
            }
            }
    res = requests.post(url=url, json=data, headers=header)
    
    if res.status_code == 201:
        return res.headers['X-Subject-Token']
    else:
        return ''
    
def get_image_list(token:str):
    url = f'{URL}:9292/v2/images'
    header = {'X-Auth-Token': token}
    res = requests.get(url=url, headers=header)
    
    if res.status_code == 200:
        content = res.content
        return json.loads(content.decode('utf-8'))
    
    