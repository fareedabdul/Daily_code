###########################################
# Leap Year 
# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0 ):
#         return True 
#     else:
#         return False
# input = int(input('Enter the Year: '))
# result = leap_year(input)
# print(result)

##################################################################3

# prime number:

# def prime_number(n):
#     count = 0
#     for i in range(2,n):
#         if n % i == 0:
#             count = count+1
#             break

#     if count == 0  and n > 1:
#         print("its a prime")
#     else:
#         print("Not a prime")

# n = int(input("Enter your marzi number: "))
# prime_number(n)


# def prime(inp):

#     if inp <= 1:
#         return f"Its not a prime number"
#     for i in range(2,inp):
#         if inp % i == 0:
#             return f"its not a prime" # if its divide then it is not a prime 
#         else:
#             return f"its a prime"
        
# result = int(input("Enter the input :")) 
# output = prime(result)
# print(output)

########################################################################
# factorial 

# def factorial(n):
#     if n < 0:
#         return "Factorial doesnt exist less than 0"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# int = int(input("Enter the input Number: "))
# result = factorial(int)
# print(result)


# positional Arguments 

# def greet(name,age):
#     return f"hey bro mera name hai {name} and meri age h {age}"

# input = greet(21,"fareed")
# print(input)

# It’ll still run, but the output will be messed up:

# example 1
# def introduce(name,city,Hobby):
#         return print(f"my name is {name}, and i live in {city} and my hobbies are {Hobby}")
# introduce("Fareed","Hyd","Car enthusiats")


#example 2 


# Keyword Arguments
# With keyword arguments, you specify the name of the parameter when passing the value — so the order doesn’t matter!

# def student_info(name,branch,roll_number):
#     return print(f"name is {name} rollNo: is {roll_number} and branch is {branch}")

# student_info(roll_number=102, branch="CSE", name="Fareed")

# def greet(name = "Fareed",language): 
# You should always place required (non-default) parameters first, and default ones later.    print(f"Hello {name}, you prefer {language} ")

# greet("English")                   # Uses default: English
# greet(,language=)  # Overrides default
#######################################################################################
#Example problem 07


# def register(name, role="Student"):
#     return print(f"he is the one {name} and his still is in {role}")
# register("FarXEid")


# -------------------------------------------------------------------------------------------------
# Step 4: Return vs Print
# print():
# Used to display output.

# Doesn’t give back the value to the program.

# return:
# Used to send the result back to where the function was called.

# Useful for storing, testing, or using later.