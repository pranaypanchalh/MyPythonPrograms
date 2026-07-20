import mysql.connector
import customerInformation

def connectDatabase():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12763736",
        password="K82dFx4TSZ",
        database="sql12763736"
    )

def insertAllData():
    for items in customerInformation.accounts:
        cursor.execute("""insert into Bank_Details values (%s,%s,%s,%s,%s,%s,%s)""", (customerInformation.accounts[items]["Name"],customerInformation.accounts[items]["Age"],customerInformation.accounts[items]["Email"],customerInformation.accounts[items]["Number"],customerInformation.accounts[items]["Password"],customerInformation.accounts[items]["Balance"],customerInformation.accounts[items]["AccountNumber"]))
    connection.commit()

def fetchData():
    cursor.execute("select * from Bank_Details")
    rows = cursor.fetchall()
    customerAccounts = {}

    for row in rows:
        customerAccounts[int(row[6])] = {
            "Name": row[0],
            "Age": int(row[1]),
            "Email": row[2],
            "Number": int(row[3]),
            "Password": row[4],
            "Balance": int(row[5]),
            "AccountNumber": int(row[6])
        }
    return customerAccounts
    

def login(accountNumber, password):
    rows = fetchData()
    for row in rows:
        if row[6] == accountNumber:
            if row[4] == password:
                return "True"
            else:
                return "Wrong pin"
        elif accountNumber not in row:
            print
connection = connectDatabase()
cursor = connection.cursor()