# instance method

# class Student:
#     college = "Holy mary"
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def show_details(self):
#         print(f"NAME : {self.name}")
#         print(f"age : {self.age}")
#         print(f"college : {Student.college}")
        
# obj1 = Student("Fareed",21)
# obj1.show_details()

# --------------------------------------------------
# Class Method


# class Student:
#     college = "Holy Mary"
    
#     @classmethod
#     def chnge_clg(cls,new_name):
#         cls.college = new_name
        
# Student.chnge_clg("HMC")
# print(Student.college)


# ------------------------------------------------
# static method


# class Student:
#     @staticmethod
#     def print():
#         print("Welcome to all")
# Student.print()