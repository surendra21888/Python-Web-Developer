import json,mysql.connector,csv,requests 
#Extract Data
data = requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()

#Transform Data
new_users=[]
for user in users:
    new_users.append((user['id'],user['name'],user['address']['city'],user['email']))

#load into mysql user Table
dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='11am') 
    cur = dbcon.cursor()
    sql_st='''
           insert into user values(%s,%s,%s,%s);
           '''
    cur.executemany(sql_st,new_users)
    dbcon.commit()
    print("user data inserted successfully")
except mysql.connector.DatabaseError as err:
    print(err)
finally:
    cur.close()
    dbcon.close()