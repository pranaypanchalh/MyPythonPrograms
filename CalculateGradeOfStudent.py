grade = int(input("Enter the student's grade (0-100): "))
if grade >= 90 and grade <= 100:
    print("The student's grade is: EX")
if grade >= 80 and grade < 90:
    print("The student's grade is: A")
if grade >= 70 and grade < 80:
    print("The student's grade is: B")
if grade >= 60 and grade < 70:
    print("The student's grade is: C")
if grade >= 50 and grade < 60:
    print("The student's grade is: D")
if grade >= 0 and grade < 50:
    print("The student's grade is: F")
else:
    print("Invalid grade entered. Please enter a grade between 0 and 100.")