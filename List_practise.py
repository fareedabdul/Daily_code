 # ! what is list in python ? 
#* list is ordered and it can contain Homogenous and heterogenous data types and we can slicing and indexing on the list like indirect ways to access the list so yeah and list is mutable, EX :: the list in amazon wherever you want you can change your list items in the list so that is the list specaility 

# ! 2. how do you create an empty list ? give two ways ?
# ? 1st method is direct method 
# list = []
# print(list)
# ? 2nd method is direct method 
# l = list()
# print(l)

# ! 3 . what are the data types that can be stored in a python list?
#? in list we can any type of data types primitive and non primitive 

# list = ["string",2.55, True, 2+6j, [98,99, 999], {420 : ValueError }, ("hello boss")]
# print(type(list[5]))

# ! 4 . how do you access the last item in a list 
# ? by indexing and slicing but the efficient way to access the list item is list indexing 
# list = [55,77,66,888]
# print(list[-1])

# ! 5 . what does the append() method do?
# ? append method will add the item in the last or in the end 
# l = [1,5,5]
# l.append(55)
# print(l)


# ! 6 . what the difference between append() and list.extend()?
# ? append method will add the item in the last or in the end 
# l = [1,5,5]
# l.append([55,88])
# print(l)            # basically its an nested list and add different element

#? Both are list methods that add elements, but the way they add is very different.

# l = [1,5,5]
# l.extend([33,89,"hi"])
# print(l) # Adding each element separately


# ! 7 .how do you check if an item exists in a list or not ?

# l = ["Fareed", 55, 77, 707]

# if "Fareeee" in l:
#     print("Found")
# else:
#     print("Not found")


#############################################################################

# * itermediate level 

# ! 1 : what is list slicing ? give an example 
# ? basically list slicing means cutting a part of the list and extracting or fetching the specific string or value is called as slicing  

# l = ["fareed",1,2,88,["syncrony Raidurg"], "Qualcomm"]
# print(l[4:1:-1])

# ! 2 : what happens when you use negative slicing index in a list 
# ? it will basically give the list in the format of reverse

# ! 3 : how does list.insert(index,item) work ? what happens if the index out of range 

# l = [ 0,1,2,3]
# l.insert(6,"Fareed")
# print(l)

# ? if it is out of range then i will directly assign the character in the last and for normal it will assign in the given position 


# ! 4 : whats the difference between remove and pop methods 
# l = [10, 20, 30, 20]
# l.remove(20)         # Removes first occurrence of 20
# print(l)             # [10, 30, 20]

# l = [10, 20, 30]
# removed_item = l.pop(1)   # Removes item at index 1
# print(l)                  # [10, 30]
# print(removed_item)       # 20

# if you pass nothing it will remove the last item 

# l = [ 1,5,36]
# l.pop(1)
# print(l) # removes 5

# ! 4 : how can you reverse a list without modifying the original list ? 

# [::-1]

# l = ["fareed", 55,77, " lion "]
# l1 = l[::-1]
# print(l1)

# ! 5 : explain the behaviour of list([1,2] * 3)

#? basically it will loop the elements 3 times 

# l = list([1,2] * 3)
# print(l)


# ! 6 : what is simple copy, shallow copy and deep copy in a list 
# ? *** 1 .simple copy is like me like who ever takes me and talk i talk from my heart i will never change and whoever i take them inside me like in my heart i will not change my behaviour like memory address

# ? *** 2. shallow copy outer one side inner list one side both plays differnt like outer list whoever access then it will point to the same address and whoever enter into the existing list like nested that will treatend another way so yeah this is matter all about shllow copy 

# ? *** 3. deep copy its like my brother  see he never be like sharing same things to other alwasy he want differernt things like other like shirt paint or anything that is there and in side the list what ever it created there will also no same address would be there it will be different address and Like how to import **** import copy from deep copy 

# Simple copy → "We share the same body and soul" 😅

# Shallow copy → "Different bodies, but same heart inside nested lists"

# Deep copy → "Different bodies, different hearts — no link at all"

#1 : copy like reference
# l1 = [1,2,3]
# l2 = l1
# l2[0] = 88
# print(l1)

# #2. 
# l1 = [[1,2],[3,4]]
# l2 = l1.copy()

# # l2[0] = [33,44]
# l2[1][0] = [33,55]
# print(l1)

# If you change the outer list, originals stay safe.

# If you change inside a nested list, both will be affected.


# ! 6 : like how to modify the strings indirect way 

# s = "Fareed"
# s ="x" + s[1:]   # replace first letter with "X"
# print(s)          # "Xareed"

# s = s + "abdul"
# print(s)

# Modify 
# s = s[0:3] + "Z" + s[3::]
# print(s)

