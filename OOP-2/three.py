class Account:
    '''claass created by Surendra'''
    def open_account(self):
        print("Account Opened successfully")
    def deposit_amount(self,amount):
        print("Amount Deposited Successfully")
    @classmethod
    def update_min_bal(cls,amount):
        print("min bal updated") 
    @staticmethod
    def cal_interest():
        print("Utility method")

a1=Account()
a2=Account()
#how to access class method. using object and class Name
a1.update_min_bal(600)
Account.update_min_bal(600)