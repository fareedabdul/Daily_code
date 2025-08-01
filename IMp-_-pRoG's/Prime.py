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


# -----------------------------Method 2 -----------------------------

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


def is_prime(n):
    if n <= 1:
        return f"its not a prime number Oops"
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        else:
           return True
input = int(input("Enter the number bro: "))
result = is_prime(input)
print(result)
