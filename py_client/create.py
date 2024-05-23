import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title": "5/25/24"}  # this line create json type format data

# we now tell it to requests.post(<the endpoint>, json=<the data>)
get_response = requests.post(endpoint, json=data)

print(get_response.json())
