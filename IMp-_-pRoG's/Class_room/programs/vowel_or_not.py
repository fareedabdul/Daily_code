chr = input("Enter the character: ")
d = {}
s = set()
if chr in "AEIOUaeiou":
    d[chr] = "AEIOUaeiou"
    print(d)
else:
    s.add(chr)
    print(s)
