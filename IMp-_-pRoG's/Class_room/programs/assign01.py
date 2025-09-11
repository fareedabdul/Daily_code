# chr1 = input("Enter the character: ")
# if "A" <= chr1 <= "Z":
#     chr1 = chr(ord(chr1)+32)
#     print(f"So this its basically uppercase converted to LOWER {chr1}")
# elif "a" <= chr1 <= "z":
#     chr1 = chr(ord(chr1)-32)
#     print(f"So this its basically lowercase converted to UPPER {chr1}")
# elif "0" <= chr1 <= "9":
#     print(int(chr1) ** 2)
# elif not("A" <= chr1 <= "Z" or "a" <= chr1 <= "z" or "0" <= chr1 <= "9" ):
#     print(chr(ord(chr1)+1),chr(ord(chr1)-1))
    # print(chr(ord(chr1)-1))

# balance = 10000
# num = int(input("Enter the amount to withdrawn: "))

# if num > 0:
#     if balance <= num:
#         print(f"Okay you have withdrawn succesfully {num} and remaining balance is {balance - num++}")
#     else:
#         print("Bro You dont have enough Money enter the enough value yaar")
# elif num < 0:
#     print("Enter the positive Number")
############################################################################

balance = int(input("Enter the bal amount: "))
num = int(input("Enter the amount to withdraw: "))

if num > 0 and balance>0:
    if num <= balance:
        print(f"Okay you have withdrawn successfully {num} and remaining balance is {balance - num}")
    else:
        print("Bro, you don’t have enough money. Enter a smaller amount.")
elif num < 0:
    print("Enter a positive number")
else:
    print("Bhai you have  negative balance+")

