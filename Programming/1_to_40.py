# 1. Write a statement (WAS) to print "Hello World" by using shell
#sol :-
#  "Hello World"

# 2. WAS to print "Hello World " by using python print Function
# print("Hello World")

#3. WAS to initialize variable and value as 50.
# a = 50

# 4 WAS to initialize multivaraible(values are 150, 120, 250)
# (Take your own variable names)
# a,b,c = 10,20,30

# 5 Print the type of a given value.
# a = 10
# print(type(a))

# 6. Print the memory address of a given value.
# a = "String"
# print(id(a))

# 7. WAS to print your detials, first store your details, extract the values and display it 
# name = "Fareed" 
# age = 21
# location = "Hyd"
# print(f"My name is {name} and age is {age} and my location is {location}")


#8. Swap two values using a temporary variable.
# a = 10
# b = 20
# temp = a 
# a = b
# b = temp
# print(a)
# print(b)

# 9. Swap two values without using a temporary variable.
# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)


# 10. Initialize a variable, print it, reassign a new value, and print again.
# a = 20
# print(a)
# a = 30
# print(a)

# Convert a single value to multi-value (e.g., 10 → ['1', '0']).
# a = 10
# a= list(str(a))
# print(a)

# Concatenate two multi-value data types (str, list, tuple, set, dict).
# string
# s1 = "Hello"
# s2 = "world"
# print(s1 +s2)

# # list

# l1 = [1,2]
# l2 = [3,4]
# print(l1 + l2)

# # set
# st1 = {1,3}
# st2 = {5,6}
# print(st1 | st2)

# #dictionary
# dt = {"name" : "Fareed" ,"age" :20}
# dt2 = {"loc" : "hyd"}
# print(dt | dt2)


# 11. Get the length of a collection.
# a = "string"
# print(len(a))

# 12 Modify the middle value of a given collection.
# a = "Hello mera Fareed"
# a = a[0:5] + " to" + a[10:]
# print(a)

# lst = [11,22,44,44,55]
# mv = len(lst)//2
# lst[mv] = 33
# print(lst)

# 13 Concatenate a new string at the start of a given string.
# s = "Hello "
# print("Fareed" + s1)

#14 Concatenate a new string at the end of a given string.

# s = "Fareed"
# print(s + " abdul")


# 15. Concatenate a new string in the middle of a given string.
# s = "i"
# s1 = "india"
# print(s + "love" + s1)

#16. Modify a character in the middle of a given string.
# a = "Hello mera Fareed"
# a = a[0:5] + " to" + a[10:]
# print(a)

#17. Modify the sequence of characters in a given string.
# s = "Python"
# # Reverse the sequence
# new_s = s[::-1]
# print(new_s)  # Output: "nohtyP"

#18.  Replace an old character with a new character in a given string.
# s = "Duck"
# s = "L" + s[1:]
# print(s)

# 19 Delete a specific character from a string.
# s = "Fareed"
# s = s[:1] + s[2:]
# print(s)

# 20.Delete a sequence of characters from a string.
# s = "Fareed is bad boy"
# s = s[0:10] + s[14:]
# print(s)

# 21. Concatenate a new string at a specific position in a string.
# a = "Hello mera Fareed"
# a = a[0:5] + " to" + a[10:]
# print(a)


#22.  Concatenate a new value at the start of a list.

# lst = [1,2,3]
# lst = [0] + lst
# print(lst)

#23.  Concatenate a new value at the end of a list.

# lst = [1,2,3]
# lst = lst + [4]
# print(lst)

#24. Concatenate a new value in the middle of a list.

# lst = [1,2,3]
# lst2 = [5,6,7]
# print(lst + [4] + lst2)

# 25.  Concatenate a new value at a specific position in a list.
# lst = [1,2,3]
# lst2 = [5,6,7]
# print(lst + [555] + lst2)

# 26Modify a value at a specific position in a list.
# lst = [22,33,55]
# lst[1] = 66
# print(lst)

# 27. Modify a value at the start of a list.
# lst = [10,20,30,40]
# lst[0] = 111
# print(lst)

# 28. Modify a value at the end of a list.
# lst = [10,20,30,40]
# lst[3] = 777
# print(lst)

# 29. Modify a value in the middle of a list.
# lst = [10,20,30,40,50]
# lst[3] = 777
# print(lst)

#30.  Modify the first 4 values of a list.

# lst = [1,2,3,4,55,66]
# lst[:4] = [777,666,333]
# print(lst)

# 31. Modify the sequence of values in a list.
# lst = [1,2,3,4,5]
# lst = lst[::-1]
# print(lst)

# 32. Delete a value at a specific position in a list.

# lst = [11,22,33,44,55]
# lst.pop(2)
# print(lst)

# Delete a value from the end of a list.
# lst = [11,22,33,44,55]
# lst.pop()
# print(lst)

# Delete a value from the start of a list.
# lst = [11,22,33,44,55]
# lst.remove(11)
# print(lst)

# Delete a value from the middle of a list.
# lst = [11,22,33,44,55]
# lst.remove(33)
# print(lst)
# Concatenate a value at the start of a tuple.
# tup1 = (4,5,6)
# print((55,66)+ tup1)
# Concatenate a value in the middle of a tuple.
# tup1 = (1,2,3)
# tup2 = (5,6,7)
# print(tup1 + (4,) + tup2)

# # Concatenate a value at the end of a tuple.
# tup1 = (1,2,3)
# print(tup1 + (4,))