import requests

endpoint = "http://localhost:8000/api/things/" 

get_response = requests.get(endpoint) 
print(get_response.json())
