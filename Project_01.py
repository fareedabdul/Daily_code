
# Sample project on marks of a student Grading
input1 = input("Enter your name :")

mark1 = int(input("enter the Mark1: "))
mark2 = int(input("enter the Mark2: "))
mark3 = int(input("enter the Mark3: "))

total_marks = mark1 + mark2 + mark3
calculate_avg = total_marks / 3
print("Average : " , calculate_avg)

if calculate_avg >= 90:
    print("Grade A")
elif 75 <= calculate_avg <= 89:
    print("Grade B")
elif 60 <= calculate_avg <=74:
    print("Grade C")
elif 35 <= calculate_avg <= 59:
    print("Grade D")
elif calculate_avg < 35:
    print("Fail")
else:
    print("Please enter your number")
