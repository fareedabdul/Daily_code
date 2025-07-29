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
#             return f"its not a prime"
#         else:
#             return f"its a prime"
        
# result = int(input("Enter the input :")) 
# output = prime(result)
# print(output)

########################################################################
# factorial 

def factorial(n):
    if n < 0:
        return "Factorial doesnt exist less than 0"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
int = int(input("Enter the input Number: "))
result = factorial(int)
print(result)