#invoke products Rest API and
#insert data into mongodb collection
import requests, pymongo
products=requests.get('https://dummyjson.com/products').json()['products']
print(type(products))
print(len(products))