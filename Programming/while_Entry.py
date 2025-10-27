# Strong Number ek aisa number hota hai jiske digits ke factorials ka sum usi number ke barabar hota hai.

n = int(input("Enter the Number: "))

res = 0
demo = n

while n != 0:
    ld = n % 10
    fact = 1
    while ld != 0:
        fact *= ld
        ld -= 1
    res += fact
    n //= 10

if demo == res:
    print("Strong hai")
else:
    print("Nahi hai Strong")
