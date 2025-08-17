
#! 1. what is a string in python 
#? string in python is a collection of characters or words that play a very imp role in python for understanding python syntax and all other stuff where 2. python is immutable datatype 3. that cant be changed once kit allocated ya we can change it by the indirect access 4. and python has 29 methods for doing everything that can be able to do,, 5. it has many way to create by the "single double quotes" & "" double quotes"" & 'single quotes'

#!2. how are string defined ?
#? "single double quotes" & "" double quotes"" & 'single quotes'

#! 3. what is the difference between single, double , and triple quotes in python string 
#? ookay first two are same and only triple quotes that will store the strings in multi-lines okay thats all

#! 4. strings are immutable 
# s = "String"
# s[0] = "f"
# print(s) #?'str' object does not support item assignment
#? strings are immuatable we cant change the data once it fixed 


#! 5. How do you access the strings by indexing 
#? we can access the string by index like by its index position its simple as that 

# s= "strings"
# print(s[5])

#! 6. what is string concatenation ? provide an example 

#? concatenation is like adding strings indirectly by using + operator like there are 5 basic methods are there 1. adding first 2. second 3. at the specific position 4. modify 5 . Del 
#** example :--->
# s = "fareed is a good "
# s = s + "Boy"
# print(s)

#! 7. how can you repeat a string mulitple times in python ?
# s = "ABC" * 3
# print(s)
# by muliply multiply symbol 


#! 8 . what is the use of the len() function with strings ? 

#? length is like finding the exact how many charcter or letters on a given string...
# like  
# s = " Python "
# print(len(s))

#! 9 . explain the diff between .lower(), .upper(), and captilize()
#? lower will do all the character in lower alphabetical 
#? upper will do all the character in upper  Case
#? Capitlize will do all the character in lower capital

# s = "lonty"
# print(s.lower())
# print(s.upper())
# print(s.capitalize())

#! 9 . explain the all 29 method functionalities and syntax


#! 10 . how do you remove whitespace from the beginning and end of a string ? 
#? we use lstrip for removing the spacing at the beginning
# s = "    sting bihar"
# s = s.lstrip()
# print(s)

#! 10 . whats the different between find() and index() methods 
#? so finds is like it finds the first index of the substring and both the index and find similar work karte hai, In find agar khuch nahi toh it will return -1 and in index shows ValueError: Substring Not Found 


# s = "python programming"

# print(s.find("pro"))   # 7
# print(s.find("x"))     # -1


#index.....................................

# s = "python programming"

# print(s.index("pro"))   # 7
# print(s.index("x"))     # ❌ ValueError: substring not found

#! 10 . how do you check if a substring exists within a string or not 
# s = " hello world kaise hoo sab thik ? "
# print("hello" in s)
# print("helo" in s)

#! 11 . What is string Formatting ? Explain with an example using f-strings 
#? see string formatting is a type that lets you print variables and all examples in one go
# a = 10
# b =30 
# print(f"Hello bro {a} and {b}")

#! 12 .  How do you replace parts of a string with another string 
# s = " Hello world, world is big"

# print(s.replace("world", "Earth"))
# print(s.replace("world", "Earth",1))

# string.replace(old, new, count) its a syntx