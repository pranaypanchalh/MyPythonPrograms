import operations as op

class BankCustomer:
    def __init__(self, Name,Age,Email,Number,Password,Balance,AccountNumber):
        self.Name = Name
        self.Age = Age
        self.Email = Email
        self.Number = Number
        self.Password = Password
        self.Balance = Balance
        self.AccountNumber = AccountNumber


while True:
    optionChoose = input("Login or Register: ").lower()
    if optionChoose == "register":
        op.register(*op.getUserCredentialsForRegister())

    elif optionChoose == "login":
            Customer = BankCustomer(*op.login())
    else:
         print("Exiting")