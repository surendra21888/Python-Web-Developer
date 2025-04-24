import json,requests
#Extract Data
products=requests.get('https://dummyjson.com/products').json()['products']
#print(type(products))  # <class 'list'>

#Load data into json file
fp=None 
try:
    fp = open('product.json','w')
    json.dump(products,fp)
    print("New JSON File created successfully")
except Exception as err:
    print(err)
finally:
    fp.close()