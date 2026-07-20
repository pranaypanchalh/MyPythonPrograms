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
print(op.login(1001,"Pranay@123"))