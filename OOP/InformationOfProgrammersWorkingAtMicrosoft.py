class microsoftEmployee:
    Name = "Name"
    Age = "Age"
    Salary = 0
    Language = "Language"
    def __init__(self, Name, Age, Salary, Language):
        self.Name = Name
        self.Age = Age
        self.Salary = Salary
        self.Language = Language

Pranay = microsoftEmployee("Pranay","20", 5000,"Python")
print(Pranay.Name, Pranay.Age, Pranay.Salary, Pranay.Language)