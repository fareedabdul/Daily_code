def fibnacci(num):
    if num ==0 or num == 1:
        return num
    else:
        return fibnacci(num - 1) + fibnacci(num - 2)
input = int(input("Enter the number for Fib haan : "))
result = fibnacci(input)
print(result)