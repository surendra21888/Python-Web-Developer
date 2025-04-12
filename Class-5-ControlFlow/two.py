#WAP to verify given number is 3 digit number or not?

num = int(input("Enter Number:"))

if num>=100 and num<=999:
    print("Yes - Given number is 3 Digit Number")
else:
    print("Not a 3 Digit Number")