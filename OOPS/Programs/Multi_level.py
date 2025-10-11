class Grand_parent:
    def call(self):
        print("I am Grand parent")
        
class Parent(Grand_parent):
    def call(self):
        super().call()
        print("Iam parent")

class Child(Parent):
    def call(self):
        super().call()
        print("I am Child")
        
obj1 = Child()
obj1.call()