data = int(input("Enter a number to check Prime: "))
i = 2
while i < data:
    if data % i == 0:
        print("Not a prime re")
        break
    else:
     print("Hmmm Its a prime Number")