# if we want to access any member of the class can access in two ways 

# ---> by using class name 
# --> by using object name 


# most of the time we use the obj name to call them 

# by using Class name 
# by using obj Name


# class Fareed:
#     a = 10
#     b = 20
    
# roshan1 = Fareed()
# Roshan2 = Fareed()

# print(a) #name 'a' is not defined
# print(Fareed.a)   10 by using class name 
# print(roshan1.a)  10 by using obj name 

## ! Modification 
class Fareed:

    a = 10
    b = 20
    
roshan1 = Fareed()
Roshan2 = Fareed()

print(Fareed.b)
print(roshan1.b)
print(Roshan2.b)
print()
Fareed.b = 555
print(Fareed.b)
print(roshan1.b)
print(Roshan2.b)
print()


roshan1.b = 777 # obj1 will be discontinued from class
print(Fareed.b)
print(roshan1.b)
print(Roshan2.b)
print()

Fareed.b = 888

print(Fareed.b)
print(roshan1.b)
print(Roshan2.b)
print()