import csv

fp = open('emp.csv','r')
csvreader=csv.reader(fp)

users = list(csvreader)

for user in users[1:]:
    print(user[1])