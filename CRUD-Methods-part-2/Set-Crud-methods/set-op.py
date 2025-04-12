s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2)) #{40, 10, 50, 20, 60, 30}
print(s1.intersection(s2)) #{40,30}
print(s1.difference(s2)) #{20,10}
print(s2.difference(s1)) #{50,60}
print(s1.symmetric_difference(s2)) #{10, 50, 20, 60}