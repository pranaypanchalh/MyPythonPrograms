Dict = {"Ghar": "House", "Paani": "Water", "Doodh": "Milk", "Aam": "Mango", "Kela": "Banana"}
search = input("Enter a Hindi word: ")
if search in Dict:
    print(Dict[search])
else:
    print("Word not found in the dictionary.")