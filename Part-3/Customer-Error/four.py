

try:
    print(10/0)   #program creating Error
    #raise ZeroDivisionError("Go to Movie")  # we are creating and throwing
except ZeroDivisionError as err:
    print(err)