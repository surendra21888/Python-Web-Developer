bytes_data = bytes([0,10,20,255])
print(bytes_data)       #b'\x00\n\x14\xff'
print(type(bytes_data)) #<class 'bytes'>

for data in bytes_data:
    print(data)