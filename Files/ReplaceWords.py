lis = ["word1","word2","word3","word4"]

with open("Files/ReplaceWords.txt", "r") as oldf:
    oldText = oldf.read()

newText = oldText
for i in lis:
    newText = newText.replace(i, "#"*len(i))

with open("Files/ReplaceWords.txt", "w") as newf:
    newf.write(newText)