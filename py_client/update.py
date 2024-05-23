import requests

pk = int(input('Please provide Id of row you want to update.'))

endpoint = f"http://localhost:8000/api/products/{pk}/update/"
title_input = input('Please provide product title')
field_prompts = f"title, content, price, sale_price, discount, test_field, vip"
print(field_prompts)
field_updater = input('choose from provided fields to update.')
update_prompt = input(f"You chose {field_updater}, Now provide Value:")

data = {
    "title": f"{title_input}",
    f"{field_updater}": f"{update_prompt}"
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
