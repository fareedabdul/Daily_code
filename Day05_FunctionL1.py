# def function(name):
#     print(f"Hello ,{name}")

# function("Fareed")


# def add(a,b,c):
#     return a+b+c
# result = add(5,6,1) 
# print(f"this are the 3 adding number of {result}")

# Function that multiplies two numbers and returns the result.

# def multiply(num1,num2):
#     return num1 * num2
# input1 = int(input("Enter the first number"))
# input2 = int(input("ENter the second number"))
# result = multiply(input1,input2)
# print(f"the multiplication of two numbers are {result}")

# Function that takes a string and prints it in uppercase.
# def function(input1):
#     return input1.upper()

# result = function("fareed")
# print(result)

# Function that takes your birth year and returns your age.

# def calculate_age(birth_year):
#     current_year = 2025
#     return current_year - birth_year

# input1 = int(input("Enter your birth year: "))
# result = calculate_age(input1)
# print("Your age is:", result)



# def function(name, age, city):
#    return f"Hello, my name is {name},iam {age} years old, and i live in {city} "

# result = function("Fareed",12,"Hyderabad")
# print(result)


# def greet(name, age = 21):
#    return  f"Hello {name}, you are {age} years old."


# result = greet("fareed")

# print(result)

# def calculate(num1, num2):
#     add = num1 + num2
#     diff = num1 - num2
#     return add, diff

# result1,res2= calculate(10, 5)
# print(result1,res2)         
################### if we are passing more than one argument then 
# defined in Two name vaiable and call them


# def number(num1, num2):
#     add = num1 + num2
#     mul = num1 * num2
#     return add, mul

# result1,result2 = number(15,6)
# print(result1,result2)


# def palindrome(text):
#     text = text.lower().replace(" ","")
#     return text == text[::-1]

# User_input = input("Enter the word or letter:")

# if palindrome(User_input):
#     print("Is palindrome")
# else:
#     print("Not a palindrome")

# palind = input("Enter ma: ")
# if palind == palind[::-1]:
#     print("success")
# else:
#     print("Chal Ye nahi hota")

# name = "Fareed"
# if name == "Fareed":
#     print("Success Bro")

# print1 = print("Hello World!")
# if print1 == "Hello World!":
#     print("Sucess")
# else:
#     print("no success") 


######################################### Default parameters
# def greet(name, age =21):
#     return f"hello {name} now you are {age} and good mrng"

# result = greet("Fareed",25)
# print(result) #  manually bhi values pass kar sakte hai even though you have passed the deafult value 


############ Function 2

# def dummy(name):
#     return (f"hello {name}")
# result = dummy("Fareed")
# print(result)


################## prob Functions 3 

# def func():
#     return (
#         "Hello world\n"
#         "chill bro\n"
#         "Mastering Functions\n"
#         "Dont misuse of functions as you misuse me\n"
#     )
# result = func()
# print(result)

################# Problem Functins 4 Return multiple values

# def cal(num1,num2):
#     add =  num1 + num2
#     sub = num1 - num2
#     mul = num1 * num2
#     div = num1 / num2
#     return (add,sub,mul,div)

# result1,result2,result3,result4 = cal(1,9)
# print(result1,result2,result3,result4)

####################################### Function 5 functions in loops
# def square(n):
#     return n * n
# for i in range (1,11):
#     print(f"square of {i} is {square(i)}")


################################### Function Return vs print 

# def add(a,b):
#    return (f"1st value is {a} and 2nd is {b}")

# result = add(1,5)
# print(result)

################ 1 .  Create a function that takes two numbers and returns their sum, product, and difference.
# def function(num1,num2):
#     sum = num1 + num2
#     pro = num1 * num2
#     diff = num1 - num2
#     return sum,pro,diff
# result1,result2,result3 = function(5,6)
# print(result1,result2,result3)

#######################2.  Create a function is_even(n) that returns True if the number is even, else False

# def is_even(n):
#     if n % 2 == 0:
#         print("Its an even")
#     else:
#         print("its not")
#     return 

# is_even(2)


###################3...Create a function that takes name, age, and location, and prints a greeting.

# def details(name,age,locations):
#     return (f"hi my name is {name} and my age is {age} and iam from {locations}")

# result = details("fAREED",21,"Hyd")
# print(result)


#################4.  Write a function that calculates the square and cube of a number and returns both.


# def function(n):
#     sqaure = n * n 
#     qube = n * n * n 
#     return sqaure,qube

# result = function(5)
# print(result)

################# 5. Create a function to check whether a student has passed based on average (>= 40).

# def is_pass(num1):
#     if num1 <= 40:
#         print("pass")
#     elif 40 <= num1 <= 75:
#         print("he got a very good score actually")
#         return 
    
# is_pass(41)

#######################6. Create a function with default parameter city = "Hyderabad", and takes name.

# def city(name,city="Hyderabad"):
#     return (f"my name is{name} and live in {city}")

# result = city("Fareed")
# print(result)

#################################7. Create a function compare_numbers(a, b) which returns the maximum number.

# def compare_num(a,b):
#     if a > b:
#         print(f"{a} is greater than {b}")
#     elif b > a:
#         print(f"{b} is greater than {a}")
#         return
    
# compare_num(5,7)

############################8.Write a function square(n) and call it inside a for loop from 1 to 10.

# def square(n):
#     return  f"this are are the {(n*n)} "
# for i in range(1,100):  
#       # return n
#  result = square(i)
#  print(result)

#######################9. Create a function that accepts marks in 3 subjects and returns total, average, and grade.

# def subjects(a,b,c):
#     Total = a+b+c
#     avg = (a+b+c) / 3
#     if Total > 65:
#         print("your Grade is A")
#     return Total,avg 
# result1, result2= subjects(55,66,20)
# print(result1,result2)

############################10.  Create a function greet() that uses return instead of print, and show the difference.

# def greet():
#     print(f"Hello world")
# greet()

# Create a calculator function that takes two numbers and an operator (+, -, *, /) and returns the result.


# def calculator(num1,num2):
#     add = num1 + num2
#     mul = num1 * num2
#     sub= num1 - num2
#     div = num1 / num2

#     return add,mul,sub,div

    
# inp1 = int(input("Enter the value1: "))
# inp2 = int(input("Enter the value2: "))

# result1,result2,rs3,rs4 = calculator(inp1,inp2)
# print(result1,result2,rs3,rs4)

##############################12.Verey level ra 
# def square(n):
#     return n * n

# for i in range(1, 11):
#     print(f"Square of {i} is {square(i)}")


###################### 
#lEAP YEAR 

# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
#         return True
#     else:
#         return False
    
# result = int(input("Enter the leap year: "))
# output = leap_year(result)
# print(output)

