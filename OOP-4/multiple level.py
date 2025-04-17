class grandparent:
    def m1(self):
        print("Grandparent class m1 method")
    def m2(self):
        print("Grandparent class m2 method")

class parent(grandparent):
    def m3(self):
        print("parent class m3 method")
class child(parent):
    def m4(self):
        print("child class m4 method")


c1=child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()