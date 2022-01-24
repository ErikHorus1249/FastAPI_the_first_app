import requests
import json

URL = "http://203.162.130.73"

    
token1 = 'gAAAAABh7V1WTBrvYP2vXdHEEmMc1DwBsUBCQu5NsrWa32Z0d-QIvl1KNUHzMvfRvKGmuIdbhJ1w5LBcGG5_VJVJILG7jN1aYqektZXD_Q1yWacvpz2LliQICyVaOUzMkdB5efkGHHZjRq1Vpd7wvtcAnNVKlAWZqf5mieAXb5ACHrjPOSHNm8I'

print(token1)

payload = {
    "server" : {
        "name" : "cirros1",
        "imageRef": "4f4ebf12-b001-4c72-9f1c-088e63ac8bd8",
        "flavorRef" : "2",
        "security_groups": [
            {
                "name": "default"
            }
        ],
        "networks" : [{
            "uuid" : "9b9685ba-04fc-48f6-a33f-694f67cc6ac7",
        }]
    }
}


header = {'X-Auth-Token': token1,
          'Content-Type': 'application/json'}

url = f'{URL}:8774/v2.1/servers'
# url = f'{URL}:8774/v2.1/servers'
# url = f'{URL}:5000/v3/users?name=admin'

res = requests.post(headers=header, url=url, data=json.dumps(payload))
# res = requests.get(headers=header, url=url)

print(res.text)
