import requests


# endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api/" #this endpoint is a working real endpoint for our project purposes

get_response = requests.post(endpoint, json={"title": "Viphakone Monty","content":"dog"}) # GET/HTTP request for WEB API aka Application programming interface

# print(get_response.text) # print raw text response in HTML format dependinhg on Endpoint
print(get_response.json()) # this will give us endpoint response in json format, which is like python dictionary
# print(get_response.status_code) # to receive status Code of endpoint
'''
API NOTES 
API = APPLICATION PROGRAMMING INTERFACE
HTTP Request -> HTML
REST API HTTP Request -> JSON
JSON = JAVAcript Object Notation ~ python Dictionary
'''