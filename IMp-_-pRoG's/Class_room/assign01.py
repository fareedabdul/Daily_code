chr1 = input("Enter the character: ")
if "A" <= chr1 <= "Z":
    chr1 = chr(ord(chr1)+32)
    print(f"So this its basically uppercase converted to LOWER {chr1}")
elif "a" <= chr1 <= "z":
    chr1 = chr(ord(chr1)-32)
    print(f"So this its basically lowercase converted to UPPER {chr1}")
elif "0" <= chr1 <= "9":
    print(int(chr1) ** 2)
elif not("A" <= chr1 <= "Z" or "a" <= chr1 <= "z" or "0" <= chr1 <= "9" ):
    print(chr(ord(chr1)+1))
    print(chr(ord(chr1)-1))

    