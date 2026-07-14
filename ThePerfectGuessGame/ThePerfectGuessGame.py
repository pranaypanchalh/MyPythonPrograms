import random as random
minRange = 1
maxRange = 10
computerValue = random.randint(minRange, maxRange)
print(f"Test {computerValue}")
userValue = 0
while computerValue != userValue:
    userValue  = int(input("Guess the number: "))
    if userValue == computerValue:
        print("You guessed correct!")
    elif userValue > computerValue:
        print("Guess a lower value")
    elif userValue < computerValue:
        print("Guess a higher value")
    else:
        print(f"Please enter between {minRange} and {maxRange}")