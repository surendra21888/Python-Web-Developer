import requests,csv,json 
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()

print(type(product_data))     #  <class,dict>
products=product_data['products']

print(type(products))         #<class,list> 