# n = 7868
# while n > 0:
#     last_digit = n % 10
#     print(last_digit,end="")
#     n = n // 10

def fibnocci(n):
    a = 0
    b = 1
    for i in range(n+1):
        print(a,end="")
        c = a+b
        a = b
        b = c
fibnocci(5)  