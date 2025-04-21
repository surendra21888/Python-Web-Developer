import requests

data = requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()
#print(type(data))
#print(type(data.json()))
#print(users)

new_users=[]
for user in users:
    new_users.append((user['id'],user['name']))

print(new_users)
