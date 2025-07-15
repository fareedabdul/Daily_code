# for i in range(1, 11): // range(start, end)
#     print(i)

# 💡 Logic:
# This prints numbers from 1 to 10.
# range(1, 11) → gives values from 1 to 10 (11 is not included)
# You can imagine this like counting laddoos from 1 to 10 for a party 🍬

# ------------------------------------
# 2.
# --------------------------------------

# i = 1 # start counting from 1
# while i <= 10: # Jab tak i ki value 10 se chhoti ya barabar hai, tab tak loop chalega
#     #  Matlab: Jab tak i = 1, 2, 3, 4, 5 — tab tak chalna hai
# # Jaise hi i = 11 hota hai, loop ruk jaayega
#     print(i)
#     i = i + 1  #i ki value badhaayega har baar
# ------------------------------------
# 3.
# --------------------------------------

# i = 10
# while i >= 1:   # i <= 10 ye logic -(minus mein jayegaa toh samjjh)
#     print(i)
#     i = i - 1


# ------------------------------------
# 4.
# --------------------------------------


# num = int(input("Enter the Table Number :"))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")


# ------------------------------------
# 5.
# --------------------------------------


# i = 0
# while i <= 50:
#     print(i)
#     i = i + 2
 
# ------------------------------------
# 6.
# --------------------------------------

# i = 1
# while i <= 50:
#         if i % 2 ==0:
#             print(i)
#             i += 1 # ✅ Always increase i (even or odd)


# ------------------------------------
# 7.
# --------------------------------------


# 💡 Logic:
# This is adding numbers from 1 to n (sum)
# 🪙 Imagine ek piggy bank hai — har din ₹1, ₹2, ₹3 ... daal raha ho


# n = int(input("Enter the total sum number: "))

# total = 0

# for i in range(1, n+1):
#     total = total + i
#     print(f"1 se {n} tak pura milakar {total}")