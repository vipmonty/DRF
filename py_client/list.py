import requests
import json

endpoint = "http://localhost:8000/api/products/"

get_response = requests.get(endpoint)

if get_response.status_code == 200:
    response_data = get_response.json()
    pretty_response = json.dumps(response_data, indent=4)
    print(pretty_response)
else:
    print(f"Failed to retrieve data: {get_response.status_code}")
