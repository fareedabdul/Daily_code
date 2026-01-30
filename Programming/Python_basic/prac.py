# 1. Write a program to find the sum of numbers.✅

# n = int(input("Enter the sum : "))
# sum = 0

# for i in range(0, n + 1):
#     sum += i
# print(sum)
# 2. Write a program to find the sum of digits of a number.

# n = input("Enter the digit to sum: ")
# sum = 0
# for i in n:
#     sum += int(i)
# print(sum) ✅
# 3. Count the number of vowels in a given string. ✅
# n = input('Enter the string ').lower() 
# count = 0
# for i in n:
#     if i in "aeiou":
#         count += 1
# print(count)
# 4. Check whether given String is a palindrome.

# n = input("Enter the string to check palindrome: ")
# if n == n[::-1]:
#     print("its palindrome")
# else:
#     print("sorry its not a palidrome")
    # 5. Write a program to generate the Fibonacci series.

# n = int(input("enter thte number to check fiboncalli series: "))
# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b 
#     a = b 
#     b = c
# 6. Write a program to find the second largest number in a given array.

# a = [10,20,30,40]
# largest = a[0]
# second = -1

# for num in a:
#     if num > largest:
#         largest, second = num, largest
#     elif num > second and num != largest:
#         second = num
# print(second)
# 7. Write a program to find the second largest number in a given number.

# a = 8522556
# digits = list(set(str(a)))
# digits.remove(max(digits))
# print(max(digits))
# 8. Write a program:
#     - If divisible by 5 → print **BUZZ**
#     - If a number is divisible by 3 → print **FIZZ**
#     - If divisible by both → print **FIZZBUZZ**
# 9. Write a Python program to check whether a given number is **prime**.

# n = int(input("Number enter kar: "))
# i = 2

# while n > 2:
#     if n % i == 0:
#         print("its not a prime number")
#         break
#     i += 1
# else:
#     print("prime") 
# 10. Write a program to **reverse a number** without converting it to a string.
# n = int(input("Enter the number: "))
# rev = 0

# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# print(rev)
    
    
# 11. Write a program to find the **factorial** of a number.

# n = int(input("Enter : "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

# 12. Write a program to check whether a given number is a **palindrome**.
# n = int(input("Enter the digit: "))
# rev = 0
# temp = n

# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# if(temp == rev):
#     print("its a palindorme")
# else:
#     print("its not a plaidnome")
# 13. Write a program to **remove duplicate elements** from a list.
# a = [ 10, 20,30,40,50,50]
# new  = []
# for i in a:
#     if i not in new:
#         new.append(i)
# print(new)
# 14. Write a program to check whether two strings are **anagrams**.

n1 = input("enreyt 1 : ")
n2 = input("enreyt 1 : ")

if sorted(n1) == sorted(n2):
    print("its a ana")
else:
    print("its not a ana")