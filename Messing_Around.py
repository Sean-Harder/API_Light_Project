#LIFX API THINGS
import requests
import json

token = "#########################"

headers = {
    "Authorization": "Bearer %s" % token,
}

response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)

lights = response.json()


label_i = lights[0]["id"]
    
payload = {
    "states": [
        {
            "selector" : f"id:{'d073d52083e8'}",
            "power": "off"
        }
    ]
}

response = requests.post('https://api.lifx.com/v1/lights/all/toggle', headers=headers)

feedback = response.json
print(feedback)