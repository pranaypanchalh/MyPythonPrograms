def sortStudByMk():
    dic = {}
    for i in range (1,6):
        temp = input("Enter Student Name: ")
        dic[temp] = int(input("Enter Marks: "))
    print(sorted(dic.items()))
sortStudByMk()

#works