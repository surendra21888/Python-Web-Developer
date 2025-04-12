unames=['Rahul','Sonia','Priyanka','Modi']#list
enames=('Rahul','Sonia','Priyanka','Modi')#tuple
eids={101,101,102,103,104,105}            #set  
emp={
    'eid':101,
    'ename':'Rahul'
}  #dict
ename="Rahul Gandhi"  #str
values=range(5,51,5)  #range
print('Rahul' in unames)  # True
print('Rahul' in enames)  #True
print(108 in eids)        #False
print('a' in ename)       #True
print(5 in values)        #True