import requests
data = requests.get('https://dummyjson.com/products')
product_data=data.json()
products=product_data['products']

new_products=[]
for product in products:
    new_products.append((product['id'],product['title'],product['price'],product['category']))

print(new_products)
