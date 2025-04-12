import json
emp={'eid': 101, 'ename': 'Surendra', 'loc': True}

emp_str=json.dumps(emp)
print(emp_str)