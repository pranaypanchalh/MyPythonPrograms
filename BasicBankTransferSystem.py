import mysql.connector
import random

#Name, Age, Email, Number, Passowrd, Balance, AccountNumber
print("====================================================================================================/n")

conn = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12763736",
    password="K82dFx4TSZ",
    database="sql12763736"
)
adminpassword = 8758

#Function for choosing from multiple operations
def OptionChoose():
    print("====================================================================================================/n")
    print("1. View Account Details")
    print("2. Add Account")
    print("# Exit operation by typing 'exit'")

    ChoosenOption = input("Please choose an option for operation: ")
    if (ChoosenOption == '1'):
        print("====================================================================================================/n")
        OptionViewDetails()
    if (ChoosenOption == '2'):
        print("====================================================================================================/n")
        OptionAddAccount()
    if (ChoosenOption == '3'):
        print("====================================================================================================/n")
        OptionDeleteAccount()
    if (ChoosenOption == 'exit'):
        return
    else:
        print("====================================================================================================/n")
        print("Oops! No option for ", ChoosenOption)
        OptionChoose()

#function for generating random number for account number      
def RandomAccountNumberGenerator():
    Random = random.randint(100000, 999999)
    cursor.execute("SELECT 1 FROM Bank_Details WHERE AccountNumber = %s", (Random,))
    result = cursor.fetchone()
    if result is None:
        return(Random)
    else:
        RandomAccountNumberGenerator()

#function for option 1 to view account's detail of the holder
def OptionViewDetails():
    AccountNumber = input("Please Enter Your Account Number: ")
    cursor.execute("SELECT * FROM Bank_Details WHERE AccountNumber = %s", (AccountNumber,))    
    row = cursor.fetchone()
    print("Name: ", row[0])
    print("Age: ", row[1])
    print("Age: ", row[1])
    print("Age: ", row[1])
    print("Age: ", row[1])
    print("Age: ", row[1])

#function to add new account and details
def OptionAddAccount():
    print("Let's Enter Your Details:")
    Name = input("Please Enter Your Name: ")
    Age = int(input("Please Enter Your Age: "))
    Email = input("Please Enter Your Email: ")
    Number = int(input("Please Enter your Number: "))
    Password = input("Please Enter Your Password: ")
    ConfirmPassword = input("Re-Enter Your Password: ")
    if (Password != ConfirmPassword):
        print("Password does not match please Re-Enter details")
        OptionAddAccount()
    else:
        Balance = int(input("Enter your Balance: "))
        AccountNumber = RandomAccountNumberGenerator()
        print(f"This is your Account Number: ", AccountNumber)
        cursor.execute("INSERT INTO Bank_Details values (%s, %s, %s, %s, %s, %s, %s)", (Name, Age, Email, Number, Password, Balance, AccountNumber))
        conn.commit()
        print("Your Account has been added!")

#function to remove account and details
def OptionDeleteAccount():
    AccountToDelete = int(input("Enter Your Account Number To Delete: "))
    cursor.execute("SELECT Number FROM Bank_Details WHERE AccountNumber = %s", (AccountToDelete,))
    AccountNumber = cursor.fetchone()
    if (AccountNumber != None):
        NumberCheck = input("Please Enter Phone Number: ")
        if (AccountNumber[0] == NumberCheck):
            cursor.execute("SELECT Password FROM Bank_Details WHERE AccountNumber = %s", (AccountToDelete,))
            AccountPassword = cursor.fetchone()
            PasswordCheck = input("Enter Your Password To Verify: ")
            if (AccountPassword[0] == PasswordCheck):
                cursor.execute("DELETE FROM Bank_Details WHERE AccountNumber = '%s'", (AccountToDelete,))
                conn.commit()
                print("Your Account Will Be Deleted Soon")
                print("====================================================================================================/n")
            else:
                print("Account Password Is Incorrect Please Re-Enter")
                OptionChoose()
        else:
            print("Account Phone Number Is Incorrect Please Re-Enter")
            OptionChoose()
    else:
        print("Account Does Not Exist")

checkadminpassword = int(input("Enter Admin Password: "))
if (adminpassword == checkadminpassword):
    print("The password is correct")
    cursor = conn.cursor()
    OptionChoose()
else:
    print("The Admin Password is incorrect! exiting...")