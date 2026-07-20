class Calculator:
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
    
first = Calculator(1,2)
print(first.add())