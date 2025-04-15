class Account:
    '''claass created by Surendra'''

    def open_account(self):
        pass
    def deposit_amount(self,amount):
        pass 
    @classmethod
    def update_min_bal(cls,amount):
        pass 
    @staticmethod
    def cal_interest():
        pass

a1=Account()
a2=Account()

#how to print class and object info
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)