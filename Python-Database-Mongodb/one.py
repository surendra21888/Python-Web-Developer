#invoke Products Rest API and 
# insert data into mongoDB Collection
import requests, pymongo
products=requests.get('https://dummyjson.com/products').json()['products']
mongoDB_url='mongodb://localhost:27017/'
try:
    client=pymongo.MongoClient(mongoDB_url)
    db=client['11am']
    prod_col=db['products']
    prod_col.insert_many(products)
    print("Product data inserted successfully")
    
except Exception as err:
    print(err)