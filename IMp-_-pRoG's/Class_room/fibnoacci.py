# def fibnacci(num):
#     if num ==0 or num == 1:
#         return num
#     else:
#         return fibnacci(num - 1) + fibnacci(num - 2)
# input = int(input("Enter the number for Fib haan : "))
# result = fibnacci(input)
# print(result)

# Method 2:
def fibonacci(num):
    fareed = 0
    roshan = 1
    if num == 1 or num == 0:
        return num
    for i in range(2,num+1):
        temp = fareed +roshan
        fareed = roshan 
        roshan = temp
    return roshan

input = int(input("Enter the Number of fib: "))
result = fibonacci(input)
print(result)

