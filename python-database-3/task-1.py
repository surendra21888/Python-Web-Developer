import requests
data = requests.get('https://dummyjson.com/products')
product_data=data.json()
status_code = data.status_code



print(product_data)
print(status_code)
products=product_data['products']
print(len(products))
