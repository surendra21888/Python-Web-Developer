class Test:
    def __init__(self):
        self.a=100

    def m1(self):
        self.b=200 

    @classmethod
    def m2(cls):
        pass

    @staticmethod
    def m3():
        pass
        
t1=Test()
t1.m1()
t2=Test()
t2.m1()

del t2.a 

print(t1.__dict__)
print(t2.__dict__)