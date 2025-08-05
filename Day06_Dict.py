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