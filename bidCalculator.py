dic = {}
bid = 0
while True:
    name = input("Please enter your name: ").lower()
    if name == "exit":
        print(max(dic, key=dic.get))
        break
    else:
        bid = int(input("Enter your bid: $"))
        dic[name] = bid