import requests

#Extract Data
data = requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()

#Transform Data

new_users=[]
for user in users:
    new_users.append((user['id'],user['name'],user['address']['city'],user['email']))
  
print(new_users)