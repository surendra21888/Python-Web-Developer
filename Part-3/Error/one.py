a = int(input("Enter First Number:"))
b = int(input("Enter First Number:"))
try:
    print(a/b)
except ZeroDivisionError as Err:
    print(a/1)
print("Good Morning")