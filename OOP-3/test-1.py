class Test:
    def __init__(self):
        self.a=10

    def m1(self):
        self.b=20 

    @classmethod
    def m2(cls):
        pass

    @staticmethod
    def m3():
        pass
        


t1=Test()
t1.e=50

t2=Test()
t2.m2()
t2.m1()
t2.m3()