#Lottery lucky dip system
from random import randint,choices

lottery_numbers=[]

for x in range(10):
    lottery_numbers.append(randint(100,999))

print(lottery_numbers)
print(choices(lottery_numbers))