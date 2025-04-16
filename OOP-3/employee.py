class Employeee:
    ''' created By Surendra '''
    org_name="TCS"   #static variable

    def _init_(self,id,name,sal):
        self.emp_id=id
        self.ename=name 
        self.esal=sal

e1=Employeee(101,'Surendra',75000.75)
e2=Employeee(102,'Girish',85000.85)
e3=Employeee(103,'Mahesh',95000.95)

print(Employeee._dict_)
print(e1._dict_)
print(e2._dict_)
print(e3._dict_)