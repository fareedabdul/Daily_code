# input1 = int(input("Enter the Number :"))

# if input1 < 0:
#     print("Its a Negative Number")
# elif input1 > 0:
#     print("Its a Postive number")
# else:
#     print("its a zero")

age = int(input("Enter the age :"))

if age < 13:
    print("you are a child Beta")
elif 13 <= age < 19:
    print("youa are a Teen")
elif 19 <= age < 59:
    print("you are an adult mama")
elif age >= 60:
    print("you are a senior")
else:
    print("Enter your age")