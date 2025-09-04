# write to create a list of even numbers and tuple of odd numbers 1 - 20

# start = 1 
# end = 20
# even = []
# odd = ()

# while start <= end:
#     if start % 2 == 0:
#         even.append(start)
#     else:
#         odd += (start,)
#     start += 1
# print(even,odd,sep="\n")


# WAP to print A - Z


# start = 65
# end = 90

# while start <= end:
#     print(chr(start))

#     start += 1

# WAP TO PRINT a - z
# start = 97
# end = 122

# while start <= end:
#     print(chr(start))
#     start += 1

# WAP TO PRINT 0 - 9 

# start = 48
# end = 57

# while start <= 57:
#     print(chr(start))

#     start +=1

# WAP TO FETCH ALL CHAR FROM A GIVEN STRING ONE BY ONE 

# S = input("Enter the string :")
# start = 0
# end = len(S)-1
# while start <= end:
#     print(S[start])

#     start += 1

#WAP TO PRINT CHARACTER IN REVERSE ?

# s = "Fareed"

# start = -1
# end = -abs(len(s))
# while start >= end:
#     print(s[start])

#     start -= 1

# WAP TO GET THE EXPECTED ANS

# INPUT = "HEl2$"

# output : uc = HE lc = l num = 2 spcl = $ 


# s = input("Enter the qna and get the answer: ")

# start = 0
# end = len(s)-1

# uc, lc, num, spcl = "","","",""
 
# while start <= end:
#     if "A" <= s[start] <= "Z":
#         uc += s[start]
#     elif "a" <= s[start] <= "z":
#         lc += s[start]
#     elif "0" <= s[start] <= "9":
#         num += s[start]
#     else:
#         spcl += s[start]

#     start += 1
# print(uc,lc,num,spcl,sep="\n")


# WAP TO GET FOLLOWING OUTPUT 

# s = input("Enter the string :")
# start = 0
# end = len(s)-1
# res = ""

# while start <= end:
#     if "A" <= s[start] <= "Z":
#         res += s[start].lower()
#     elif "a" <= s[start] <= "z":
#         res += s[start].upper()
#     elif "0" <= s[start] <= "9":
#         res += str(int(s[start]) **2)
#     else:
#         res += s[start]

#     start += 1
# print(res) 


# Q) WAP TO ITERATE OVER A LIST AND GET THE MAX NUMBER 


# list = [5,55,777,66]
# start = 0
# end = len(list) -1 
# assume = list[0]

# while start < end: 
#     if list[start] > assume:
#         assume = list[start]
#     start += 1
# print(f"big number is {assume}")


# Q) WAP TO ITERATE OVER A LIST AND GET THE TOTAL 
# list = [55,88,777,232]
# start = 0
# end = len(list) -1 
# total = 0

# while start <= end:
#     total += list[start]
#     start += 1
    
# print(total)


# Q) WAP TO GET THE MINIMUM NUMBER FROM A GIVEN TUPLE 

t = ("hi",8,99,66,6,7,{"a":10},2,-55)


# start = 0
# end = len(t)-1
# assume = t[3]

# while start < end:
#     if type(t[start]) == int:
#         if t[start] < assume:
#             assume = t[start]

#     start += 1

# print(assume)