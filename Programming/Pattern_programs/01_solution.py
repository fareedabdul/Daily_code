# n = 5 
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j:
#             print("#",end=" ")
#         elif i + j == n + 1:
#             print("$",end = " ")
#         else:
#             print(' ',end=" ")
#     print()


  #       $ 
    #   $
      #
#   $   #
# $       #



# n = 5 
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i+j == n+1 or i == j:
#             print("@",end = " ")
#         else:
#             print("#",end =" ")
#     print()
    
  
# n = 5
# for i in range(1,n+1):
#     m = 23
#     for j in range(1,n+1):
#         if i == j or i >j:
#             print(m,end =" ")
#             m +=1
#         else:
#             print(" ",end = " ")
#     print()

# print(chr(ord("A") +32))

# n = 5
# for i in range(1,n+1):
#     char = "A"
#     for j in range(1,n+1):
#         if i==j or i < j:
#             print(char,end=" ")
#             char = chr(ord(char)+1)
#         else:
#             print(" ",end=" ")
#     print()

# n = 5
# char = "L"
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i < j:
#             print(char,end=" ")
#             char = chr(ord(char)+1)
#         else:
#             print(" ",end=" ")
#     print()
            
            
n = 5

for i in range(1,n+1):
    m = i
    for j in range(1,n+1):
        if i % j == 0 or  i >= j:
            print(m**2,end=" ")
            m += 1
        else:
            print(" ",end=" ")
    print()


