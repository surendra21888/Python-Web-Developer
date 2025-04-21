import mysql.connector
dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='11am')
    cursor = dbcon.cursor()
    sql_st='''
            create table employee(
            eid int,
            ename varchar(32),
            esal float
            );
           '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Table Created Successfully")

except mysql.connector.DatabaseError as err:
    print(err.msg)

finally:
    pass 