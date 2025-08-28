num = int(input("Enter the number :"))
d = {}
if num % 2 == 0:
    d[num] = num **2
    print(d)
else:
    d[num] ="odd"
    print(d)