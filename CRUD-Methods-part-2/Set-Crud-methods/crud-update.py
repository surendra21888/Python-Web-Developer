s1 ={'a','b','c'}
s2={'d','e'}
s3="Rahul"

s1.update(s2)  
print(s1)    #{'d', 'e', 'a', 'c', 'b'}
s1.update(s3,{'z','x','z'})
print(s1)