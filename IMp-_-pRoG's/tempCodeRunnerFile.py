def sum_of_even(lst):
    total = 0

    for i in lst:
        if i % 2 ==0:
            total += i
    return total 

input = list(map(int,input("Enter the Number:").split()))
result = sum_of_even(input)
print(result)
