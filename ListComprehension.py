import random as rnd
name = "Angela"
newList = [letter for letter in name]
print(newList)

print([n*2 for n in range(1,5)])

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print([item.upper() for item in names if len(item)>5])

studentsScore = {student:int(input(f"Enter marks for {student}: "))  for student in names}
print(studentsScore)