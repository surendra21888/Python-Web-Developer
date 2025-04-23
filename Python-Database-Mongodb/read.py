from pymongo import MongoClient

try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['11am']
    prod_col=db['products']
    
    products=prod_col.find({})

    for product in products:
        print(product)

except Exception as err:
    print(err)