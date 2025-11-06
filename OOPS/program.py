# class Sample:
#     a = 10
#     b = 20
    
# obj1 = Sample()
# obj2 = Sample()

# print(id(Sample))
# print(id(obj1))
# print(id(obj2))

# # print(Sample.__dict__)
# # print(dir(obj1))

# print(obj1.__dict__)


# class data:
#     a = 10
#     b = 20
# obj1 = data()
# obj2 = data()
# print(obj2.a)
# print(obj1.a)

# print(data.__dict__)
# print(dir(obj1))

# print(data.a)
# print(data.b)  # its an class name okay

# print(obj1.a)
# print(obj1.b) # its an object name and its an obj1

# print(obj2.a)
# print(obj2.b) 

# class SampleData:
#     a = 10
#     b = 20 
# obj1 = SampleData()
# obj2 = SampleData()

# # print(SampleData.a)
# # print(obj1.a)
# # print(obj2.a)
# SampleData.a = 500
# print(SampleData.a)
# print(obj1.a)
# print(obj2.a)
# obj1.a = 777
# print(SampleData.a)
# print(obj1.a)
# print(obj2.a)
# SampleData.a = 800


# from functools import wraps
# def deco(func):
#     def wrapper(*args,**kwargs):
#         print("Hello Start")
#         func(*args,**kwargs)
#         print("Ended") 
#     return wrapper


# @deco
# def basic():
#     print("Hello world")
# basic()


# num = "145"
# sum = 0
# for i in num:
#     fact = 1
#     for j in range(1,int(i)+1):
#         fact *= j
#     sum += fact
# if num == str(sum):
#     print('its a perfect number')
# else:
#     print("its not a perfect number")

# inp = [12, "program", 6+78j, "kaiku"]
# dt = {}

# for i in inp:              
    
#     if type(i) == str:     
#         vowels = ""
#         for j in i:         # go through each letter
#             if j in "aeiouAEIOU":
#                 vowels += j
#         dt[i] = vowels      # store result

# print(dt)



# inp = [12, "program", 6+78j, "kaiku"]
# dt = {}

# for i in inp:              
    
#     if type(i) == str:     
#         vowels = ""
#         for j in i:         # go through each letter
#             if j not in "aeiouAEIOU":
#                 vowels += j
#         dt[i] = vowels      # store result

# print(dt)
   

# inp = input("Enter the input: ").split()
# print(inp)

# class cls_name:
#     school_name = "Loyola"
#     loc = "Hyderabad"
#     subject = "PFS"
#     trainer = "Monty"

# obj1 = cls_name()
# print(obj1.school_name)

# class math:
#     @staticmethod
#     def add(a,b):
#         return a + b
    
# print(math.add(10,20))

# class student:
#     school_name = "Lola school"
    
#     def __init__(self,name):
#         self.name = name
        
#     @classmethod
#     def change_school(cls,new_name):
#         cls.school_name = new_name
# print(student.school_name)
# student.change_school("Loyola")
# print(student.school_name)


# class Student:
#     name = "Fareed"
#     marks = 90
    
#     def display(self):
#         print(f"name is {Student.name} and marks are {Student.marks}")
# obj1 = Student()
# obj1.display()
        
    
# class parent:
#     sub = "python"
#     institute = "qsp"
#     batch = "a21"
# class child(parent):
#     def __init__(self,name):
#         self.name = name
#     def display(self):
#         print(f"std_name: {self.name} sub: {self.sub} and institute : {self.institute} and batch is {self.batch}")
# obj1 = child("Fareed")
# obj1.display()

###########################################################################################
# class Parent:
#     def __init__(self):
#         print("Parent class constructor")
# class child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("its a child class")
# obj1 = child()
    
#################################################################################################

#method overriding
# class vehicle:
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#     def start(self):
#         super().start()
#         print("car started")
# obj1 = car()
# obj1.start()
        
        
# def deco_name1(func):
#     def wrapper(*args,**kwargs):
#         print("d1 start")
#         func(*args,**kwargs) 
#         print("d1 end")
#     return wrapper
# def deco_name2(func):
#     def wrapper(*args,**kwargs):
#         print("d2 start")
#         func(*args,**kwargs)
#         print("d2 end")
#     return wrapper

# @deco_name1
# @deco_name2
# def user():
#     print("Fareed as a user")
# user()

    
    
# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         print("Class B")

# class C(B):
#     pass

# obj = C()
# obj.show()


# class A:
#     def __init__(self):
#         print("A")

# class B(A):
#     def __init__(self):
#         print("B")
#         super().__init__()

# class C(B):
#     def __init__(self):
#         print("C")
#         super().__init__()

# obj = C()


# class Person:
#     per = "normal person rehte"
#     def display(self):
#         print("Mein abhi just normal person hoon")
# class Employee(Person):
#     c = "employee"
#     def display(self):
#         print("Mein abhi just Employee hoon")
# class Manager(Employee):
#     def display(self):
#         print(f"manager hoon sala mere niche {self.c} and {self.per} ")
# obj1 = Manager()
# obj1.display()

# class grandparent:
#     jagah = "10acres"
# class parent:
#     ghar = "5bhk"
# class son(grandparent,parent):
#     def display(self):
#         print(f"mekhu nana ne {self.jagah} and mujhe mummy ne {self.ghar}")
# obj1 = son()
# obj1.display()
        
        
    