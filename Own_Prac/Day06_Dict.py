# #Ways to assigning the dict
# #Direct way 01
# d = {777:"Hello"}
# #None
# d
# {777: 'Hello'}
# d1 = dict({445:"rohit"})
# #none
# d1
# {445: 'rohit'}
# d2 = {}
# d2
# {}
# # Accessing the elements from Dict
# # 01 by using key
# d1 = dict({445:"rohit", 7 : "Dhoni", 8:"Ronaldo"})
# d1
# {445: 'rohit', 7: 'Dhoni', 8: 'Ronaldo'}
# d1[8]
# 'Ronaldo'
# d1[7]
# 'Dhoni'
# d1[445]
# 'rohit'
# d1[3]
# Traceback (most recent call last):
#   File "<pyshell#18>", line 1, in <module>
#     d1[3]
# KeyError: 3
# #GET METHOD
#  d1 = dict({445:"rohit", 7 : "Dhoni", 8:"Ronaldo"})
 
# SyntaxError: unexpected indent
# d1 = dict({445:"rohit", 7 : "Dhoni", 8:"Ronaldo"})
# d1.get(445)
# 'rohit'
# d1.get(55,"Invalid re bhai")
# 'Invalid re bhai'
# d1.get(445,"hey come on man ")
# 'rohit'
# #############################################################
# d1 = dict({445:"rohit", 7 : "Dhoni", 8:"Ronaldo"})
# # KEYS ACCESSING
# d1.keys()
# dict_keys([445, 7, 8])
# # VALUES ACCESSING
# d1.values()
# dict_values(['rohit', 'Dhoni', 'Ronaldo'])
# # Both Pair and values
# dl.items()
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     dl.items()
# NameError: name 'dl' is not defined. Did you mean: 'd'?
# d1.items()
# dict_items([(445, 'rohit'), (7, 'Dhoni'), (8, 'Ronaldo')])



# s1
# {'hello': 1, 'world': 22, 'Bro': 364}
# s1.pop("Bro")
# 364
# s1
# {'hello': 1, 'world': 22}
# s1.popitem()
# ('world', 22)
# s1.popitem("hello")
# Traceback (most recent call last):
#   File "<pyshell#57>", line 1, in <module>
#     s1.popitem("hello")
# TypeError: dict.popitem() takes no arguments (1 given)
# s1.popitem()
# ('hello', 1)
# s1
# {}
# s1 = dict({'hello': 1, 'world': 22, 'Bro': 364})
# s1.clear()
# s1
# {}
# s1
# {}
# {}
# {}
# s1 = dict({'hello': 1, 'world': 22, 'Bro': 364})
# del s1
# s1
# Traceback (most recent call last):
#   File "<pyshell#67>", line 1, in <module>
#     s1
# NameError: name 's1' is not defined. Did you mean: 'd1'?
# d1
# {8: 'Ronaldo'}
# s1
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     s1
# NameError: name 's1' is not defined. Did you mean: 'd1'?


#####################################################################################################
# Adding values pairs
# d ={}
# d["key 01"] = "Darwaza2"
# d
# {'key 01': 'Darwaza2'}
# d["Key 02"] = "Darawaza3"
# d
# {'key 01': 'Darwaza2', 'Key 02': 'Darawaza3'}


# -------------------------------------------------------------
# s = {}
# lists = ["Mon","Tue","Wed"]
# routine = s.fromkeys(lists,"Same Routine")
# routine
# {'Mon': 'Same Routine', 'Tue': 'Same Routine', 'Wed': 'Same Routine'}


# Dictnary will ba play vital role in Real time data
# and dictonary is a key and value pairs 
# dictonary can have a uniq keys No duplicates4
# values can be duplicates and any datatypes 
# keys are immutable
# keys should be single element
# key should be uniq
# dict is a mutable

# *****************************We have 3 types of assigning method------------------
# ! first is Direct assigning : d ={}
# ! Class object : d1 = dict({key: value})
# ! DEfault value : d = {}


# *******************************we have basically 5 types of accessing the dict----------
# ? by the key value : syn :- dict[]
# ? by GET method : var.get(key,sp)
#? only keys : var.keys()
# ? only values : var.values()
# ? Full items : var.items()

#***********************************removing the key elements
# ? Pop()  :- var.pop(key,secondparameter)
# ? popitem() :- var.popitem() // Randomly it will delete
# ? clear() :- clear the all dictonary set No error
# ? del - 2types  - 1.first type :- del var
# ? second type - del var[key]

#*********************************adding the elememt
#? 1.key value pairs = syntax : dict[key] ="value"
#? 2.updating the variable : dict.update(key = "value")
# ?  first you need a S = {} , then create key for different in list []
#? then access the dictionary and then dict.fromkeys(listname,"Value")

