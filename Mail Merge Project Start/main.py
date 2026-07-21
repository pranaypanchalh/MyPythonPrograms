with open ("Mail Merge Project Start/Input/Letters/starting_letter.txt" , "r") as letterFormatFile:
    letterFormat = letterFormatFile.read()

with open ("Mail Merge Project Start/Input/Names/invited_names.txt" , "r") as invitedNamesFile:
    namesList = invitedNamesFile.read().split("\n")

for name in namesList:
    with open (f"Mail Merge Project Start/Output/ReadyToSend/Invitation Letter For {name}.txt" , "w+") as formattedLetterFile:
        formattedLetterFile.write(letterFormat.replace("[name]",name))