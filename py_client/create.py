import requests

endpoint = "http://localhost:8000/api/things/"
data = {
    'name': 'New Thing 10',
    'description': 'New Thing description 10'
}
get_response = requests.post(endpoint, json=data) 
print(get_response.json())
