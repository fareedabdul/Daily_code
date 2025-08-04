# user_input = input("Enter The student number")

def calculate_avg(sub1,sub2,sub3):
    avg = sub1 + sub2 + sub3 
    return avg / 3
subj1 = int(input("Enter the subject1: "))
subj2 = int(input("Enter the subject2: "))
subj3 = int(input("Enter the subject3: "))

def assign_grade(returning):
    if returning > 90:
        return (f"Grade A")
    elif 70 <= returning <= 89:
        return (f"Grade B")
    elif 45 <= returning <= 69:
        return (F'Grade C')
    elif 35 < returning:
        return f"Fail Bro"
    else:
        return f" please enter the marks first for checking !!"
   

returning = calculate_avg(subj1,subj2,subj3)
print(returning)




