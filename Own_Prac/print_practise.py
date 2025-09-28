
# _________________________________________________________________________
# print("hello")
# ? print("A", "B", "C") # Default: sep=" " aur end="\n"
# print ("Hello", "world" ,sep="-") 
# sep = values ke beech chipkane wala glue

# ---------------------------------------------------------------------------------


# understanding the end in deeply

# line ke end mein chipkane wala fevicol
# print("Hello","World","Duniya", end=" ")
# print("Apple", end=" ")
# print("Banana")
# a = 10
# print("hello","World","gitam",end=" ")
# print(a)

# sep default " " => space, end ka Newline '/n'
# ⚡ Tumhara confusion clear karte hain

# "2nd line agar default use kar raha hai toh nayi line mein aana na, upar ke andar kyu guss raha h?"

# 💡 Kyunki:

# Default end="\n" tab lagta hai JAB line khatam hoti hai.
# Lekin 1st line mein tumne end=" " lagaya tha → newline hi nahi lagaya → cursor abhi tak upar hi line ke end pe khada tha.
# Isliye "Apple" usi line ke andar guss gaya.
# "Apple" ke baad default \n laga → aur tab nayi line shuru hui.

# a,b,c,d = 1,22,33,55

# print(a,  end=" ")
# print(b,c,sep = ", ", end = ", ")
# print(d)


# okay end mein bhi symbol use karsakte 