import requests

thing_id = input("What is the Thing Id that you want to delete?\n")

try:
    thing_id = int(thing_id)
except:
    thing_id = None
    print(f'{thing_id}, provide an Id.')

if thing_id:
    endpoint = f"http://localhost:8000/api/things/{thing_id}/delete/"

    get_response = requests.delete(endpoint)
    if get_response.status_code == 404:
        print(f'{thing_id} doesn`t exists.')
    print(get_response.status_code, get_response.status_code == 204)
