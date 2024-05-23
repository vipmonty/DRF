import requests
pk = int(input('Please enter the product ID of desired product.'))
endpoint = f"http://localhost:8000/api/products/{pk}"

get_response = requests.get(endpoint)

print(get_response.json())
