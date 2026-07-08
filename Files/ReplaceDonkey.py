oldText = ""
with open("Files/ReplaceDonkey.txt", "r") as oldf:
    oldText = oldf.read()

newText = oldText.replace("Donkey","######")
with open("Files/ReplaceDonkey.txt", "w") as newf:
    print(newText)
    newf.write(newText)