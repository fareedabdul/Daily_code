# # user_input = input("Enter The student number")

# def calculate_avg(sub1,sub2,sub3=0):
#     avg = sub1 + sub2 + sub3 
#     return avg / 3 if sub3 != 0 else avg / 2 

# def assign_grade(returning):
#     if returning > 90:
#         return (f"Grade A")
#     elif 70 <= returning <= 89:
#         return (f"Grade B")
#     elif 45 <= returning <= 69:
#         return (F'Grade C')
#     elif  returning < 35 :
#         return f"Fail Bro"
#     else:
#         return f" please enter the marks first for checking !!"

# num_students = int(input("how many student do want to Enter : "))

# for i in range(num_students):
#     print(f"\n--- Student {i+1} ---")
#     name = input("Enter student name: ")
#     sub1 = int(input("Enter Subject 1 marks: "))
#     sub2 = int(input("Enter Subject 2 marks: "))
#     third = input("Do you want to enter Subject 3 marks? (y/n): ")

#     if third.lower() == 'y':
#         sub3 = int(input("Enter Subject 3 marks: "))
#         avg = calculate_avg(sub1, sub2, sub3)
#     else:
#        avg = calculate_avg(sub1, sub2)

#     grade = assign_grade(avg)

#     print(f"\n{name}'s Report:")
#     print(f"Average: {avg}")
#    print(f"Grade: {grade}")
###################################################################################################

def calculate_marks(sub1, sub2, sub3=0):
    total = sub1 + sub2 + sub3
    return total / 3 if sub3 != 0 else total / 2

def grade_marks(avg):
    if avg > 90:
        return "Grade A"
    elif 75 <= avg <= 89:
        return "Grade B"
    elif 45 <= avg <= 74:
        return "Grade C"
    else:
        return "Bro, you need to improve"

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    print(f"\n---- Student {i + 1} ----")
    name = input("Enter the name of the student: ")
    sub1 = int(input("Enter Subject 1 marks: "))
    sub2 = int(input("Enter Subject 2 marks: "))

    third = input("Do you want to enter a third subject? (y/n): ")

    if third.lower() == "y":
        sub3 = int(input("Enter Subject 3 marks: "))
        avg = calculate_marks(sub1, sub2, sub3)
    else:
        avg = calculate_marks(sub1, sub2)

    grade = grade_marks(avg)
    
    print(f"\n{name}'s Report")
    print(f"Average: {avg}")
    print(f"Grade: {grade}")



