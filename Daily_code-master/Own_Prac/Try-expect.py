n = 5
try:
    print(n/0)
except ZeroDivisionError:
    print("aab uhtauch")


l = [77,88,66,99]
try:
    print(l.index(1000))
except ValueError:
    print("this value which you passed is not found")
except IndexError:
    print("This index is not found")
