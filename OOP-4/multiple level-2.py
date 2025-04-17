class Grandparent:
    def m1(self):
        print("Grandparent class m1 method")

class parent1(Grandparent):
    def m2(self):
        print("parent1 class m2 method")

class parent2(Grandparent):
    def m3(self):
        print("parent2 class m3 method")

class child(parent1,parent2):
    def m4(self):
        print("child class m4 method")

c1=child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()