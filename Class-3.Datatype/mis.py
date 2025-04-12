b = bytes([0,10,20,255])
ba=bytearray([0,10,20,255])
fz = frozenset({10,20,30,40,10,20,30,40})
print(b)   #b'\x00\n\x14\xff'
print(ba)  #bytearray(b'\x00\n\x14\xff')
print(fz)  #frozenset({40, 10, 20, 30})
#print Data type
print(type(b))  #<class 'bytes'>
print(type(ba)) #<class 'bytearray'>
print(type(fz)) #<class 'frozenset'>