import requests 
from pymongo import MongoClient
products=requests.get('https://dummyjson.com/products').json()['products']
product_data=products.json()['products']

new_product=[]

for product in products:
    new_product ({
        'pid':product['pid'],
        'pName':product['title']
        'category':product['price'],
        'price':product['price'],
        'rating':product['rating']
    })
try:
    client=pymongo.mongoclient('mongodb://localhost.27017')
    db=client['11am']
    product_col=db['products']
    product_col.insert_many(new_products)
    print('product data written successfully')
except:
    pass
finally
    pass

