class Account:
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name 
        self.acc_bal=amount

    def deposit_amount(self,amount):
        self.acc_bal = self.acc_bal+amount
    def withdrawl(self,amount):
        self.acc_bal = self.acc_bal-amount

a1=Account(101,"Rahul",5000)
a2=Account(102,"Sonia",50000)
print(a1.__dict__)
print(a2.__dict__)
a1.deposit_amount(15000)
a2.deposit_amount(150)
print(a1.__dict__)
print(a2.__dict__)

a1.withdrawl(15)
a2.withdrawl(5000)
print(a1.__dict__)
print(a2.__dict__)