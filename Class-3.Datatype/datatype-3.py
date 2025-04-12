bytearray_data = bytearray([0,10,20,255])
print(bytearray_data)       #b'\x00\n\x14\xff'
print(type(bytearray_data)) #<class 'bytes'>

for data in bytearray_data:
    print(data)