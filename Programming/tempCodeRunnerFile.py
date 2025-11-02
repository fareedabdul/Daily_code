li_data = eval(input("Enter the number:"))
et= []
for i in li_data:
    if type(i) == int and i % 5 == 0 and 99 < i < 1000:
        et.append(i)
print(et)