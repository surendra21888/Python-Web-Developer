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

#how to access class members? using object
a1.open_account()
a1.deposit_amount(5000)
a1.update_min_bal(600)
a1.cal_interest()