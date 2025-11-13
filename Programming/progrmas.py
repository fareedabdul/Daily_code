# data = input("Enter the String: ")
# ch = input("Enter the character to check: ")
# for i in range(len(data)):
#     if data[0] == ch:
#         print(f"Successfully its a Match {data[0]}!")
#         break
# else:
#     print("Mama you Failed 😒 " ) 

##################################################################################



# data = input("Enter the string: ")
# for i in data:
#     if ('a' <= i <= 'z'):
#         print("Succesfully")
#         break
# else:
#     print("Not a lower case")



##########################################################################################

data = int(input("Enter a number to check Prime: "))
i = 2
while i < data:
    if data % i == 0:
        print("Not a prime re")
        break
    i += 1
else:
     print("Hmmm Its a prime Number")