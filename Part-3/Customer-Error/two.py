from insuffientBalError import InsuffientBalErr

amount=int(input("enter amount:"))
acc_bal = 40000

if acc_bal < amount:
    #print("low balance")
    raise InsuffientBalErr("low balance")
else:
    print("withdrawl and enjoy")

    print("Good Morning")