# 
# ! what is set ?
# set is a mutbale data and its can contain 64 bit and it will takes the postive and negative values and set cant take the duplicate values in result output it will only display the unique values 

# ! how do you create an empty set ?
#  creating a emopty set 
# s = set()
# print(type(s))

# ! why {} is not an empty set ? 
# because its a empty dictionary 

# ! can a set contain a list to a tuple and vice versa? 
# yes absolutely you can convery to vice versa anything 
# s = {1,23,5}
# print(list(s))
# print(tuple(s))
# list1 = [5,5,5]
# print(set(list1))
# print(tuple(list1))


#! can a set contain duplicate elements ? explain 
# set doesnt contain duplicate in the set, even if you try to add the duplicates it will not add and in resultant output it will show the unique items
#Why 👍 ?
#A set is based on the mathematical definition of a set → which always stores unique elements.
#Internally, Python uses hashing to store set elements.
#Since each unique value has only one hash entry, duplicates are not stored.

#! how do you an element to a set ? 
# s = set((1,5,3))
# s.add(58)
# print(s)

# ! how do you remove an element from a set ? 
# there are many ways but 
# remove---------------------
# s = set((1,5,3))
# s.remove(10) // Key error
# print(s)
# discard : if you pass any unknown value it will return nothing 
# s = set((1,5,3))
# s.discard(10) /// it will not give any error for us  
# print(s)


#! how do you check if an number is exist or not
# we use membership operator like --in-- --Not-in-- operator
# s = (221,222,223)
# print(222 in s)

# ! can a set contains different datatypes ? 

# s = set(([55,66,66],"string",88))
# print(s)

#  What can a Python set contain?
# A set can only contain hashable (immutable) objects.
# 📌 Allowed (Hashable / Immutable)
# Numbers → int, float, complex, bool
# s = {1, 2.5, True, 3+4j}
# Strings → immutable ✅
# s = {"apple", "banana"}
# Tuples (only if all elements inside are hashable)
# s = {(1, 2), (3, 4)}
# frozenset (immutable version of set)
# s = {frozenset([1, 2]), 3, "hi"}
# 📌 Not Allowed (Unhashable / Mutable)
# list ❌
# dict ❌
# set ❌

# ! are sets mutable or immutable ? can you modify a set after it created
# ✅ Sets are mutable → Yes, you can modify a set after it is created (add, remove, clear elements).

# ⚡ But the elements inside a set must be immutable.

# can a set contain another set ? why or why not?
# ❌ A set cannot contain another set because sets are mutable (unhashable).
# ✅ But it can contain a frozenset (immutable, hashable).

# Example:

# s = {1, frozenset({2,3})}
# print(s)   # {1, frozenset({2, 3})}