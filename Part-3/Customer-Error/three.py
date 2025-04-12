from insuffientBalError import InsuffientBalErr as lowbalerror

acc_bal=40000
try:
    amount=int(input("enter amount"))
    if acc_bal<amount:
        raise lowbalerror("buddy - low bal! please check!")
    else:
        print("please withdrawl and enjoy!")

except lowbalerror as err:
    print(err)
except:
    print("check the code default errors")

    print("Good Morning")