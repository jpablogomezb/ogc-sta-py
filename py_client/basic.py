import requests

#endpoint = "http://httpbin.org/anything"
#endpoint = "http://139.162.133.135:8456/v1/isAlive"
endpoint = "http://localhost:8000/api/home/"

get_response = requests.get(endpoint, params={"abc": 123})
# json={"name":"Thing 3", "description": "This is Thing 3"}
#print(get_response.status_code)
print(get_response.json())



