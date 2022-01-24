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
    header = {'Accept': 'application/json','X-Auth-Token': token, 'Content-Type': 'application/json'}
    res = requests.get(url=url, headers=header)
    
    if res.status_code == 200:
        content = res.content
        return json.loads(content.decode('utf-8'))
    

def get_server_list(token:str):
    url = f'{URL}:8774/v2.1/servers/detail?host=Ubuntu'
    header = {'X-Auth-Token': token}
    res = requests.get(url=url, headers=header)
    
    if res.status_code == 200:
        content = res.content
        return json.loads(content.decode('utf-8'))
    
def create_server(token):
    header = {'Accept': 'application/json','X-Auth-Token': token, 'Content-Type': 'application/json'}
    url = f'{URL}:8774/v2.1/servers'
    data = {
        "server": {
            "name": "cirros_api_1",
            "imageRef": "c0287939-c13f-41c2-ace8-a46d1cd4b1e1",
            "flavorRef": "0",
            "networks": "auto"
        }
    }
    
    # code = requests.post(url=url, json=data, headers=header)
    
    code = requests.get(url=url, headers=header)
    
    return code