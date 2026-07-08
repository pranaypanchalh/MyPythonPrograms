import random

def game(a,b):
    Dict = {"rock":1,"paper":2,"scissor":3,"exit":4}
    valuesDict = Dict.values()
    keysDict = Dict.keys()
    userScore = a
    computerScore = b
    computerChoose = 0

    def computerChooseFunc():
        return random.randint(1,3)

    while userScore>=0:
        print(f"User Score is: {userScore}")
        print(f"Computer Score is: {computerScore}")
        userChooseTemp = input("Choose Rock, Paper or Scissor / type exit to EXIT GAME: ").lower()

        if userChooseTemp in Dict:
            userChoose = Dict[userChooseTemp]
            computerChoose = computerChooseFunc()
            print(f"Computer choose: {computerChoose}")
            if userChoose == 4:
                print("EXITING THE GAME")
                break
                
            elif userChoose == computerChoose:
                print("Tie")

            elif userChoose == 1 and computerChoose == 2 or userChoose == 2 and computerChoose == 3 or userChoose == 3 and computerChoose == 1:
                print("You lost!")
                computerScore += 1
            else:
                print("You won!")
                userScore += 1
        else:
            print("You have entered wrong value try again!")
    return userScore,computerScore
