# ✅ Q1: Swap two numbers using a temp variable
x = 10
y = 20
temp = x  # temp = 10
x = y     # x = 20
y = temp  # y = 10

print(x)
print(y)

# ✅ Q2: Swap two numbers without using a temp variable (using list unpacking)
x = 10
y = 36
[x, y] = [y, x]

print(x)
print(y)

# ✅ Q3: Swap two numbers using arithmetic operators
x = 20
y = 10

x = x + y
y = x - y
x = x - y

print(x)
print(y)

# ✅ Q4: Print your name, age, and city
name = "Fareed"
age = 21
city = "Hyderabad"
print(name, "is my name ok")
print("I am", int(age), "years old")
print("I live in", city)

# ✅ Q5: Print favorite color
favourite_color = "skyBlue"
print(favourite_color)

# ✅ Q6: Swap two numbers using tuple unpacking
a = 5
b = 10

a, b = b, a

print(a)
print(b)

# ✅ Q7: Take input name and age, and print formatted greeting
name = input("What's your name? ")
age = input("And your age? ")

print(f"Hello {name}, you are {age} years now")  # f = formatted string

# ✅ Q8: Add two numbers from input
input1 = int(input("Enter the first value: "))
input2 = int(input("Enter the second value: "))

print("Sum is:", input1 + input2)

# ✅ Q9: Calculate age from birth year
input1 = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - input1
print(f"You are {age} years old and born on {input1}")

# ✅ Q10: Check if input is a string or not (note: input is always string unless converted)
input1 = input("Enter something: ")

if input1.isdigit():
    print("Your input is an integer")
else:
    print("Your input is not an integer")

# ✅ Q11: Check type of float
x = 10.5
print(type(x))
print(x)

# ✅ Q12: Check type of boolean
print(type(True))  # Output: <class 'bool'>

# ✅ Q13: Find the larger of two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The largest number is", num1)
elif num2 > num1:
    print("The largest number is", num2)
else:
    print("Both are equal")

# ✅ Q14: Check pass or fail based on marks
marks = int(input("Enter your marks: "))
if marks < 35:
    print("Failed")
elif marks >= 35:
    print("Passed")
else:
    print("Absent")

# ✅ Q15: Check even or odd
input1 = int(input("Enter a number: "))

if input1 % 2 == 0:
    print("It's an even number")
else:
    print("It's an odd number")
