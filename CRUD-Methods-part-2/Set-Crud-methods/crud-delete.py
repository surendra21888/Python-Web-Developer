s1={101,102,103}
#s1.remove(102)
s1.discard(102)
print(s1)  #{101, 103}

#s1.remove(1)  #KeyError: 1
s1.discard(1) #No Error
print(s1)    # #{101, 103}