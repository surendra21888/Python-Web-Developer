class account: 
    def __init__(self,id,names,amount):
        self.acc_id=id
        self.acc_names=names
        self.acc_bal=amount


a1=account(101,"Surendra",10000)
a2=account(102,"Arjuna",5000)
print(a1.__dict__)
print(a2.__dict__)