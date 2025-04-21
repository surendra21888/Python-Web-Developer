import mysql.connector
dbcon=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='11am')
    print(dbcon)
    cursor=dbcon.cursor()
    sql_st=''' insert into employee values(101,'Surendra',45000.45);'''
    cursor.execute(sql_st)
    dbcon.commit()
    print('Data Inserted')
except mysql.connector.DataError as err:
    print(err.msg) 

finally:
    pass
