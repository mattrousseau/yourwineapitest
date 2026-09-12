import requests

url = 'https://matthieuwineapi.azurewebsites.net/predict'

headers = {
   'accept': 'application/json',
   'Content-Type': 'application/json',
}

data = {'alcohol':9.4, 'volatile_acidity': 0.7}

resp = requests.post(url, headers=headers, json=data)
print(resp.json())
