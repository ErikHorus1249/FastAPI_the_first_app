import requests
import json

URL = "http://203.162.130.73"
TOKEN = "gAAAAABh_ATg8vHkWskoK61HNWwRf8St-cCqYqHG-aC8DwSlXrPJHeTPdQXajpT6wdMowe_Cgdb8F2QCvFLK-QiM8DcyzXJOAi_rZJH0o8jbGuLTZGRv_7HoMPUaZNEhJWVk7JtfQdehAUFNcrNOKR3E-KHvy0DG7VKekSTHo8miN36KXuBQ4V0"


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
    
def get_image_list():
    url = f'{URL}:9292/v2/images'
    header = {'Accept': 'application/json','X-Auth-Token': TOKEN, 'Content-Type': 'application/json'}
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
    
def create_server():
    header = {'X-Auth-Token': TOKEN, 'Content-Type': 'application/json'}
    url = f'{URL}:8774/v2.1/servers'
    data = {
        "server": {
            "name": "cirros_2",
            # "imageRef": "c0287939-c13f-41c2-ace8-a46d1cd4b1e1",
            "imageRef": "3b1cc60d-8bc7-4d07-8e67-4c00d7e1a957",
            "flavorRef": "1",
            "networks" : [{
                "uuid" : "9b9685ba-04fc-48f6-a33f-694f67cc6ac7"
            }]
        }
    }
    
    response = requests.post(url=url, json=data, headers=header)
    
    # code = requests.get(url=url, headers=header)
    
    return response