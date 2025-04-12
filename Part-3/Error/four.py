fp=None
try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print(a/b)
    fp=open("data.txt",'r')
    print(fp.read())

except ZeroDivisionError as err:
    print(a/1)

except ValueError as err:
    print("Enter only Digits")

except FileNotFoundError as err:
    fp=open('abc.txt','r')
    print(fp.read())
except :
    print("New Error! check Code")