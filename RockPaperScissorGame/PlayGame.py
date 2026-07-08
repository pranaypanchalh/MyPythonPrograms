from RockPaperScissorGame import game

# Read the file
with open("RockPaperScissorGame/HiScore.txt", "r") as f:
    data = f.read()

# Convert to integers
a, b = map(int, data.split("+"))

na, nb = game(a, b)

# Replace the file contents
with open("RockPaperScissorGame/HiScore.txt", "w") as f:
    f.write(f"{na}+{nb}")