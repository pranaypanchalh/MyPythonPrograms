def sumList():
    numList = []    
    for i in range (1, 6):
        numList.append(int(input("Enter Number:")))
    print(sum(numList))
sumList()