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
    

def login():
    loopStatus = 0
    while loopStatus == 0:
        inputAccountNumber = int(input("Please enter your account number: "))
        inputPassword = input("Please enter your password: ")
        rows = fetchData()
        if inputAccountNumber in rows.keys():
            if inputPassword in rows[inputAccountNumber]["Password"]:
                print("Logged in success fully")
                loopStatus = 1
                return list(rows[inputAccountNumber].values())
            else:
                print("Wrong Password, please try again")
        else:
            print("Account does not exist")
        
def getUserCredentialsForRegister():
    loopStatus = 0
    inputName = input("Please enter your name: ")
    inputAge = int(input("Please enter your age: "))
    inputEmail = input("Please enter your email: ")
    inputNumber = int(input("Please enter your phone number: "))
    while loopStatus == 0:
        inputPassword = input("Create new password: ")
        inputConfirmPassword = input("Confirm new password: ")
        if inputPassword == inputConfirmPassword:
            return inputName, inputAge, inputEmail, inputNumber, inputPassword
            loopStatus = 1
        else:
            print("Password did not match")

def register(name, age, email, number, password):
    rows = fetchData()
    tempRow = []
    for row in rows:
        tempRow.append(row)
    newestAccountNumber = max(tempRow)
    newestAccountNumber += 1
    cursor.execute("insert into Bank_Details values (%s,%s,%s,%s,%s,%s,%s)", (name, age, email, number, password, 0, newestAccountNumber))
    connection.commit()
    print(f"Your account number is: {newestAccountNumber}")
connection = connectDatabase()
cursor = connection.cursor()