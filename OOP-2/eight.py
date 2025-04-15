class test:
    '''class craeted by Surendra'''
    a=100
    def __init__(self):
        self.b=20
        self.c=30
    def m1(self):
        self.d=40

t1=test()
print(t1.__dict__)     #{'b':20,'c':30}
print(test.__dict__)   #{'a':10}