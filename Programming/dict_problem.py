# li = "apple is my fav".split(" ") 
# dt = {}

# for i in li: # ["apple","is","my"]
#     vowels = ""  # empty vowels var
#     for j in i:
#         if j in "aeiouAEIOU":
#             vowels += j
            
#             dt[i] = vowels
# print(dt)
            
# li = [1, 2, 13, 55, 8, 99]

# for i in range(0,len(li),2):
#     print(li[i])


# names = ["fareed"," waheed"," bhaiya the bro"]
# res = " ** ".join(names)  
# print(res)  

# li = [1, 2, 13, 55, 8, 99]

# for i,v in enumerate(li,start=1):
#     if v % 2 != 0:
#         print(i,v*5)

# data = input('Enter the string: ')
# for i in data:
#     if i in "aeiouAEIOU":
#         print(i, end=" ")

li_data = eval(input("Enter the number:"))
et= []
for i in li_data:
    if type(i) == int and i % 5 == 0 and 99 < i < 1000:
        et.append(i)
print(et)