# def counting_vowels(text):
#     vowels_list = "aeiouAEIOU"
#     vowel_counter = 0

#     for i in text:
#         if i in vowels_list:
#             vowel_counter += 1

#     return vowel_counter
        
# inp = input("Enter the string: ")
# result = counting_vowels(inp)
# print(result)


# Create a function that takes a list of numbers and returns the sum of even numbers only.

def sum_of_even(lst):
    total = 0

    for i in lst:
        if i % 2 ==0:
            total += i
    return total 

input = list(map(int,input("Enter the Number:").split()))
result = sum_of_even(input)
print(result)

