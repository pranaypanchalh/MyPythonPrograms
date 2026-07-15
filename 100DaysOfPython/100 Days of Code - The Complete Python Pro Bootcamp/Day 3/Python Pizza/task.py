print("Welcome to Python Pizza Deliveries!")
totalOrderPrice = 0
while True:
    size = input("What size of pizza do you want? S, M or L: ").upper()
    if size == "S":
        totalOrderPrice += 15
        break
    elif size == "M":
        totalOrderPrice += 20
        break
    elif size == "L":
        totalOrderPrice += 25
        break
    else:
        print("You have entered wrong choice")

while True:
    addPepperoni = input("Add pepperoni for pizza? Y or N: ").upper()
    if size == "S" and addPepperoni == "Y":
        totalOrderPrice += 2
        break
    elif size == "M" and addPepperoni == "Y" or size == "L" and addPepperoni == "Y":
        totalOrderPrice += 3
        break
    elif addPepperoni == "N":
        break
    else:
        print("You have entered wrong choice")

while True:
    addExtraCheese = input("Add extra cheese for pizza? Y or N: ").upper()
    if addExtraCheese == "Y":
        totalOrderPrice += 1
        break
    elif addExtraCheese == "N":
        break
    else:
        print("You have entered wrong choice")

print(f"Your total is: {totalOrderPrice}")