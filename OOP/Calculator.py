class calculator:
    def __init__(self, a):
        self.a = a
    def square(self):
        return self.a*self.a

squareObj = calculator(5)
print(squareObj.square())