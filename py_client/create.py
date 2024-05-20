import requests

endpoint = "http://localhost:8000/api/products/"

data = {"title":"from create.py"} # this line create json type format data

get_response = requests.post(endpoint, json=data) # we now tell it to requests.post(<the endpoint>, json=<the data>)

print(get_response.json())

