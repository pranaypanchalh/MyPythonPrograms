def countZero(li):
    count = 0
    for i in li:
        if i==0:
            count=count+1
    print(count)
myList = [0,1,2,0,1,2,0]
countZero(myList)
