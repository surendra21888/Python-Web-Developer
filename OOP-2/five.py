class Test:
    def __init__(self):
        print("constrcutor is special method")
    def get_details(self):
        print("Instance method")
    @classmethod
    def update_TestClass(cls):
        print("class method")
    @staticmethod
    def sum(a,b):
        print("static method")

Test()
Test()