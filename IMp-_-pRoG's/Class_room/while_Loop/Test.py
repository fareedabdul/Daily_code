# 1.PRINT THE SQUARES OF NUMBER FROM 1 TO 10 

# start = 1
# end = 10 
# while start <= end:
#     print(start ** 2)

#     start += 1

# 2. print all number divisible from 1 to 50 that are divisible by 7:


# start = 1
# end = 50

# while start <= end:
#     if start % 7 ==0:
#         print(start)
#     start += 1


# 3. print sum from 1 to 100 


# start = 1 
# end = 100 
# sum = 0

# while start <= 100:
#     sum += start 
#     start +=1 

# print(sum)


# 4. PRINT NUMBERS FROM 1 TO 100 BUT ONLY THOSE DIVISIBLE BY BOTH 3 AND 5 

# start = 1
# end = 100 

# while start <= end :
#     if start % 3 == 0 and start % 5 == 0:
#         print(start)
#     start += 1

# 5. by using single while loop print good morning / good afternoon / good evening 

# count = 1

# while count <= 15:
#     if count <= 5:
#         print("GM")
#     elif count <= 10:
#         print("GAF")
#     else:
#         print("GE")
#     count += 1

# Write a Python program that takes input from the user for the type of food item they want (pizza or burger).
# If the item is pizza,
# Ask the user for the size (large, medium, small).
# Use nested if–else statements to check the size:
# If "large" → print "Large Pizza – Rs. 300"
# If "medium" → print "Medium Pizza – Rs. 200"
# If "small" → print "Small Pizza – Rs. 100"
# Any other input → print "Invalid size"
# If the item is burger,
# Ask the user if they want cheese.
# Use nested if–else statements to check:
# If "yes" → print "Cheese Burger – Rs. 150"
# If "no" → print "Regular Burger – Rs. 100"
# If the item is neither pizza nor burger, print "Invalid item".
# 👉 Note: Use only if–else statements (no elif).


print("HEllo Welcome to python Restaurant")
burger = 200
order = input('What do you wanna have Today "Pizza" or "Burger" : ')

match order:
    case "Pizza":
        size = int(input("Enter the size 1 To 15 split from 5: "))
        if  size >= 10 and size <= 15:
            print("Large pizza 899.rs")
        elif size >=5 and size <=10:
            print("Medium Pizza 599.rs")
        elif size >= 1 and size <=5:
            print("Small one 299.rs")
    case "Burger":
        cheese = input("Enter Burger with cheeze or not: ")
        if cheese == "Yes" or cheese == "No":
            if cheese == "Yes":
                print(f"Burger with cheese {burger + 75}")
            elif cheese == "No":
                print(f"Burger without cheese {burger}")
            else:
                print("Select Burger Mama")
    case _:
        print("Inavlid Input please try to select the pizza or burger")
