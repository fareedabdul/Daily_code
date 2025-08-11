
# ! 1 : What is a tuple in python ? how is it different from a list ??
# * Okay Tuple is a non primitive data type ---2 its a multi value data type ----3 it is immutable ]--> and its a variable length memory ]--> Tuple is a 64 bit it stores 
#  * list is mutable ordered based on memory Slower than tuple and both are ordered in terms of storing 

# ! 2 : how do you create an empty tuple and a tuple with one element
# my_tuple = () //  its a tuple with no elements
# my_tuple = (55,) // give ,(comma) after the element 
# print(my_tuple) 

# ! 3 : are tuple mutable or immutable ? explain with an example 
#* tuple are immutable becoz it changed you chnaged the value okay 
# tupl  = (55,66)
# tupl[0] = 99
# ? ✅ This happens because tuples lock their contents after creation.

# ! 4 : how do you access  elements in a tuple ? give an example 

#? Indexing → pick one element
mixed = (1, "apple",[55,66], 3.5, True)
# print(mixed[0])  # (1, 'apple', 3.5, True)
# print(mixed[1::])
# print(mixed[2][0]) /Nested Tuple Access

#? Slicing → pick a range of elements

# ? Nested indexing → go deeper if it has tuples/lists inside

# ! 5 :can a tuple contain elements of different data types ? show with an example 


# Tuple with only immutable items → works as a key
# t1 = (1, 2, 3)
# my_dict = {t1: "ok"}  # ✅ Works

# # Tuple with a list inside → fails as a key
# t2 = (1, [2, 3])
# my_dict = {t2: "not ok"}  # ❌ Error

#? ✅ Things a tuple can contain
# ?Numbers (int, float, complex)
# ?Strings
# ?Booleans
# ?Lists
# ?Other tuples
# ?Dictionaries
# ?Sets
#? Functions
#? Classes & objects
#? Even modules or file handles


