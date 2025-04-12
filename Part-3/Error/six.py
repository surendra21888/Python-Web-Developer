enames=["RG","SG","PG","NG"]
#index    0   1   2        3
print(enames[0])   #RG
print(enames[108])   #IndexError
enames.append("Surendra")
print(enames) #["RG","SG","PG","NG","Sur"]
enames.kamal("Arjuna")  #Attribute