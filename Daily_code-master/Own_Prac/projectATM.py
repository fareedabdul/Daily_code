
# *****************************Atm project hai ye bohut simple Try it ....***********************************

default_pass = 1234
max_attempts = 3
count = 0

while count < max_attempts:
    userp = int(input("Enter the password :"))
    if userp == default_pass:
        print("Welcome to ATM!")
        break
    else:
        print("Incorrect PIN. Try again.")
        count += 1
if count == max_attempts:
    print("bhai your has been Blocked")