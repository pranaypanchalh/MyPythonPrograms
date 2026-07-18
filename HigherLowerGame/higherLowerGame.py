from gameData import data
import random

player1Details = {}
player2Details = {}
totalCountOfData = len(data)
userScore = 0
player1Details = data[random.randint(0,totalCountOfData)]

while True:

    #Pick another random is both are equal
    while True:
        if player1Details == player2Details:    
            player2Details = data[random.randint(0,totalCountOfData)]
        else:
            player2Details = data[random.randint(0,totalCountOfData)]
            break

    #print the descriptions
    print(f"Person A is:\nName: {player1Details["name"]}\nDescription: {player1Details["description"]}\nCountry: {player1Details["country"]}\n")
    print(f"Person B is:\nName: {player2Details["name"]}\nDescription: {player2Details["description"]}\nCountry: {player2Details["country"]}\n")

    #give hint
    print(f"Hint: {max(player1Details["follower_count"],player2Details["follower_count"])}")

    #insert by user
    userGuess = input("Guess who has higher follower(choose A or B or type anything to EXIT): ").upper()

    #compare the answers
    if userGuess == "A" and player1Details["follower_count"] > player2Details["follower_count"] or userGuess == "B" and player1Details["follower_count"] < player2Details["follower_count"]:
        print("You guessed it right!\n")
        userScore += 1
        player1Details = player2Details

    elif userGuess == "B" and player1Details["follower_count"] > player2Details["follower_count"] or userGuess == "A" and player1Details["follower_count"] < player2Details["follower_count"]:
        print("You guessed it wrong!\n")
        print("Game over!\n")
        userScore == 0
        break

    else:
        print("You have pressed anything, exiting...")
        break