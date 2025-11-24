def studMarks():
    list = []
    sortedlist = []
    studName = []
    for i in range(1,7):
        studName.append(input("Enter Student Name:"))
        list.append(int(input("Enter Student {i} marks: ")))
    sortdList = list   
    sortedlist.sort()
    print(sortedlist)
studMarks()

#doeesnt work modified