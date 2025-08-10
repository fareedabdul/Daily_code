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
