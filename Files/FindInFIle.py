f = open("Files/TestFile.txt")
keyword = input("Enter a word you want to find in TestFile:")
data = f.read()
if (keyword in data):
    print(f"File contains word: {keyword}")
else:
    print(f"There is no word: {keyword}")
f.close()