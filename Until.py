# def new_fun(a,b)
#     return a + b
# new_fun(10,20)

# def new_fun(a,b)
#     ...
# print(new_fun(a=10,20))


# # def demo(name,age):
# #     ...
# # print(demo("Fareed",21))

# #? Hamesha function ke andar kuch operation (return ya print ya calculation) hona chahiye, tabhi woh kuch output dikhayega.


# def demo(name,age):
#     print(name,age)
# print(demo("fared",21))


# def demo(name,age):
#     return name,age
# res = demo("fared",21)
# print(res) 


# #####################################################################################################################
# # class and object 
# Class :- Class is a blueprint or template that tells objects what actually object should perform or behave
# print("heLLOW")


# print("Hello new Year 2026")

# Strings
# Strings slicing
# Strings methods in python


# ! strings - a string is a collection of characters 
# name_first = "Siddhu"
# ex_name = "Dia"
# sentence = "Iam learning python"

# print(f"{name_first} loved {ex_name} and now {sentence}") # * formatted strings 


# Strings slicing

#!  strings ka ek part nikalna  or extracting the specific character or word....



#syntax:  string[start:end+1:stepvalue]
# start is included 0
# end is excluded o 


# text = 'python' 

# ! postitve indexing - forward indexing 
# print(text[0:4])
# print(text[2:6])
# print(text[:4]) 
# print(text[2:]) 

# !  negative indexing - backward indexing 

# text = 'python' 

# print(text[-1])
# print(text[-4:-1])

# ! Step value 
#syntax:  string[start:end+1:stepvalue]

# text = 'python' 
#p-0 y-1 t-2 h-3 o-4 n-5
# print(text[:])
# print(text[0:5:2])
# print(text[1::2])

# name = 'Fareed'
# print(name[:2]+"***"+name[-1])

# Fa***d
# lower()
# print(name.lower())

# name = 'Siddhu is a gay and gay is a fareed'
# print(name.split())



# ! find is used to find the particular index of the string and for its only first occurence

# normal = "Fareed is a Good boy ???"

# # var.stringmethods()

# s = normal.find("o")

# print(s)


# ! index is to find the exact position of the charcter as a number 

# print("helle".index("e")) #1

# name = False
# print(name)

# normal = "Fareed is a Good boy ???"

# print(normal.count("o"))

# print("python".startswith("py")) # boolean values - true or false

# print("python.py".endswith("p"))

# print("ab".isdigit())

# print("abc".isalpha())

# print("abc123".isalnum())

# print("   ".isspace())

# print("hi".center(6,"-"))


#!  if condition:
#!  # RUNS IF ONLY TRUE 
#! else:
#! # RUNS IF ONLY FALSE


# nums = 23

# if nums < 0:
#     print("he is adult with no job")
# else:
#     print("he is not a adult")

n = 12

if n % 2 != 0:
    print("True")
else:
    print("True")
    
    