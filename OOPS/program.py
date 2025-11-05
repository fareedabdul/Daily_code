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
   

inp = input("Enter the input: ").split()
print(inp)