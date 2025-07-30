
# Factorial Program 

# def factorial(fact):
#     if fact < 0:
#         return f"You are Fool that you have Entered !"
#     elif fact == 0 or fact == 1:
#         return 1
#     else:
#         return fact * factorial(fact - 1)

# input = int(input("Enter the Number Lets check:"))

# output = factorial(input)
# print(output)

#-----------------------Method2-----------------------

import math 
num = int(input('Enter the Number: '))
if num < 0:
  print("factorial is not defined for negative numbers")
else:
  print(f"The factorial of {num} is : {math.factorial(num)}")
  