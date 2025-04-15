class Account:
    ''' created by Surendra Reddy'''
    def open_account(self):
        print("Account Opened Successfully!") 
    def deposit_amount(self):
        print("Amount Depsited") 
    def withdrawl(self):
        print("Amount Withdrawl")  

a1=Account()
a2=Account()
#printing object in the form of dict
print(a1.__dict__)  #{}
print(a2.__dict__)  #{}
print(Account.__dict__)