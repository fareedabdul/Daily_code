# operators are used to perform some operations on variables and values

# variable are containers {pushpa container}
# brain,  topic :  operators - value 
# siddhu = 10
# print(siddhu)

# operators 

#  A T M A C B I L - 8
# A = ARITHMETIC OPR
# T = TERNARY - OPR
# M = MEMBERSHIP OPERATOR
# A = ASSIGNMENT OPR
# C = COMPARISON OPR / RELATIONAL OPR
# B = BITWISE OPR
# I = IDENTITY OPR
# L = LOGICAL OPR


#  A = ASSIGNMENT OPR

# !  IT IS USED TO ASSIGN THE VALUE TO VARIABLE 
# ? TWO TYPES - 1) NORMAL ASSIGNMENT 2) COMPOUND ASS
#  1) NORMAL ASSIGNMENT
 
# a = 10
# print(a)

# 2)  compound ass

# com of bitwise and arithmetic

# a = 20
# a -= 1
# print(a)

# b = 20


# a = 20
# b = 40
# print(a + b)

# a,b = 20,69
# t1 = a + b
# print(t1)

# ----------------------------------

# Identity operator

# there are 2 types of identity operator :- compare the address of object/ values, syntax-id(var_name)
# 1) is :  both the conditions are true
# 2) is not : operator both the condtions are pointing at the different address it will return false


# 64 bit                                  32 bit
# address

# int                                    int
# float                                  bool
# complex                               str without chr
# str with spcl chr                     char
# list, tuple, set, dict


# n = True
# n1 = False

# print(n is n1) # 


# s = "siddhu"
# s1 = "siddhu#"


# print(id(s))
# print(id(s1))

# print(s is not s1)

# s = (55,66,77)
# s1 = ("hello")

# print(s is not s1)



# Mutable and immutable
# mutable = we can chnge the Value
# immuatble = we cant the value 

# Non- primitive datatypes
# List 
# tuple
# set
# dict


# tuple = (55,"hello", 8.6, 777)
# print(tuple)

# tuple.append(69)
# print(tuple)



# -----------------------------------------------------------------
################------Dia---------####################################
# input_yaha_pe_Dalo = input("Enter your Crush Name: ") # string
# years_of_Relationship = int(input("Enter the years of relationship: "))

# print(f"He loves you More than his own heart .{input_yaha_pe_Dalo} and your bonding since lasting for the years of {years_of_Relationship}")



start = 1
count = 15
# Good morning  - 5, Good Afternoon -5 , Good Evening -5 .  

while start <= count:
    if start >= 1 and start <=5: # 1 2 3 4 5
        print("Good Morning")
    elif start >= 6 and start <=10:
        print("Good afternoon")
    else:
        print("Good evening")

    start += 1
