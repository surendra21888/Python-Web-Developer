import json
user = '''
       {
       "userName":"Surendra",
       "avail":true,
       "loc":null
       }
       '''

user_data = json.loads(user)
print(user_data)
print(user)