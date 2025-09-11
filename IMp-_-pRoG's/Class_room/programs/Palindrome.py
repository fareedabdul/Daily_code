data = input("enter the data to check the palindrome: ")

if data == data[::-1] :
    print("its a palindrome")
else:
    print("its not a palindrome")