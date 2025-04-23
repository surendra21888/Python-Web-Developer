from pymongo import MongoClient
db_url='mongodb://localhost:27017/'
try:
    client=MongoClient(db_url) 
    db=client['11am']
    emp_col=db['employees']
    emp_col.insert_one({"eid":101,"ename":"Rahul","esal":45000.45})
    print("New Employee Doc inserted successfully")

except Exception as err:
    print(err)