import mysql.connector

conn = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12763736",
    password="K82dFx4TSZ",
    database="sql12763736"
)
column1Lis = []
column2Lis = []
column3Lis = []

cursor = conn.cursor()

#cursor.execute("Insert into testDatabase values (2, 'Oum', 'Hi')")
#conn.commit()

cursor.execute("SELECT * FROM testDatabase")
for row in cursor.fetchall():
    column1Lis.append(row[0])
    column2Lis.append(row[1])
    column3Lis.append(row[2])

print(column1Lis)
print(column2Lis)
print(column3Lis)

conn.close()
