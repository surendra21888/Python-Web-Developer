import json,mysql.connector,csv,requests 
#Extract Data
data = requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()


fp = open('user.csv','w',newline="")
csvwriter=csv.writer(fp)
csvwriter.writerow(['id','name','loc','email'])

for user in users:
    csvwriter.writerow([user['id'],user['name'],user['address']['city'],user['email']])

print("New CSV File Created and written successfully!")

fp.close()