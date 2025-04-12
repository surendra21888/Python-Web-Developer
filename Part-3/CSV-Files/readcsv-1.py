import csv

fp = open('emp.csv','r')
csvreader=csv.reader(fp)

print(csvreader)
print(type(csvreader))
print(csvreader)

for user in csvreader:
    print(user)