print("Hello Welcome to instagram login For Fun Haan")
user_name = input("Enter your user-name: ")
password = int(input("Enter your Password: "))

# character hona and special char and number and with minumum length 8


if len(password) == 7:
    if 'A' <= password <= 'Z':
        pass
    elif 'a' <= password <= 'z':
        pass
    elif '0' <= password <= '9':
        pass
    elif not('A' <= password <= 'Z' and 'a' <= password <= 'z' and '0' <= password <= '9'):
        print("Sucessfully Logged in ")
    else:
        print(" Enter the valid passwords")