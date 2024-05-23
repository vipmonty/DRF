import requests

pk = int(input('Please provide Id of row you want to update.'))

endpoint = f"http://localhost:8000/api/products/{pk}/update/"
title_input = input('Please provide product title')
data = {
    "title": f"{title_input}",
    # "price": 129.00
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
