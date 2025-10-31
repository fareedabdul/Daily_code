li = "apple is my fav".split(" ") 
dt = {}

for i in li: # ["apple","is","my"]
    vowels = ""  # empty vowels var
    for j in i:
        if j in "aeiouAEIOU":
            vowels += j
            
            dt[i] = vowels
print(dt)
            
