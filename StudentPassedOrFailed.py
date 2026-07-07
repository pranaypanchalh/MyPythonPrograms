Hindi = int(input("Enter marks in Hindi out of 70: "))
English = int(input("Enter marks in English out of 70: "))
Gujarati = int(input("Enter marks in Gujarati out of 70: "))
if (Hindi/70)*100 >= 33 and (English/70)*100 >= 33 and (Gujarati/70)*100 >= 33:
    print("Student has passed.")
else:
    print("Student has failed.")
if (Hindi+English+Gujarati)/210*100 >= 40:
    print("Student has passed in all subjects")