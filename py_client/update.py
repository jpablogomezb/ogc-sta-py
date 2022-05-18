import requests

endpoint = "http://localhost:8000/api/things/8/update/"
data = {
    'name': 'Thing 8',
    'description': 'New Thing description 8'
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
