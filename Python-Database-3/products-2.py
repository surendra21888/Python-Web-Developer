import requests,mysql.connector

data = requests.get('https://dummyjson.com/products')
product_data=data.json()
products=product_data['products']

new_products=[]
for product in products:
    new_products.append((product['id'],product['title'],product['price'],product['category']))

#print(new_products)
dbcon = None 
try:
    dbcon=mysql.connector.connect(host="localhost",user='root',password='root',database='11am')
    cur=dbcon.cursor()
    sql_st ='''
                insert into product values(%s,%s,%s,%s);
            ''' 
    cur.executemany(sql_st,new_products)
    dbcon.commit()
    print("Product Data write into Product Table")
except mysql.connector.DatabaseError as err:
    print(err)
    
finally:
    pass