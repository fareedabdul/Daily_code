# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def details(self):
#         print(f"{self.name}")
# obj1 = Student("Fareed",22)
# obj1.details()

# data = input("Enter the data: ") # "mam"
# s1 = ""
#  # mam ka length 3, -1 , -1
# for i in range(len(data)-1,-1,-1):
#     s1 += data[i]
    
# if data == s1:
#     print("its a palindrome")
    
    
    

# data = "fareed nagesh salman sanketh".split(" ")
# dt = {}
# for i in data:
#     vowels = ""
#     for j in i:
#       if j in "aeiouAEIOU":
#           vowels += j
#           dt[i] = vowels
# print(dt)
          

# data = ["apple",155,"ab","Salman","nagesh"]
# dt = {}
# for i in data:
#     if type(i) == str:
#         dt[i] = i[0] + i[len(i)//2] + i[-1]
# print(dt) 

# data= ["apple",155,"ab","Salman","nagesh"]
# dt = {}
# for i in data:
#     if type(i) == str:
#         dt[i] = len(i)
# print(dt)
# for length checking yehi hai 


# def is_vowel(st):
#     count = 0
#     total = 0
#     for i in st:
#         if i in 'aeiouAEIOU':
#             count += 1
#             total += ord(i)
#     return count,total

# st = input("enter string: ")
# result = is_vowel(st)


# print(f"count is : {result[0]} and total is: {result[1]}")


# a = "salman" 
# sum = 0
# for idx,val in enumerate(a,start=10):
#     if val in 'aeiouAEIOU':
        
#         sum += idx
# print(sum)
# s = "Fareed"
# for i in range(len(s)):
#     if i in "aeiouAEIOU":
#         print(i[s])

# s = "Fareeed"
# for i in range(len(s)):
#     if s[i] in "aeiouAEIOU":
#         print(f" {s[i]} is values and there positions are {i}")

# n = int(input("Enter the n number: "))
# nums = eval(input(" ev").split())
# nums.sort()
# for i in range(1,n+1):
#     if i not in nums:
#         print("missing number is", i)
#         break


# nums = list(map(int,input('Enter the number: ').split()))
# print(nums)


# s = "Fareeed"
# for i in range(len(s)):
#     if s[i] not in "aeiouAEIOU":
#         print(f" {s[i]} is values and there positions are {i}")

# n = int(input("Enter the perfect number: "))
# sum_of_div = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum_of_div += i
# if n == sum_of_div:
#     print("Its a perfect Number")
# else:
#     print("its not a perfect Number")


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# # Step 1: Find the largest side
# largest = max(a, b, c)

# # Step 2: Check right angle using Pythagoras theorem
# if largest == a and a**2 == b**2 + c**2:
#     print("It's a right-angled triangle.")
# elif largest == b and b**2 == a**2 + c**2:
#     print("It's a right-angled triangle.")
# elif largest == c and c**2 == a**2 + b**2:
#     print("It's a right-angled triangle.")
# else:
#     print("It's NOT a right-angled triangle.")
