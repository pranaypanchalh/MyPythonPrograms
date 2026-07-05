students = {}
for i in range(6):
    students[input(f"Enter the name of student {i+1}: ")] = int(input(f"Enter the marks of student {i+1}: "))   

sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=False)
print("Students sorted by marks in ascending order:")
print(sorted_students)