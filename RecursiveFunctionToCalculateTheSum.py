def sumFunc(value):
    if value==1:
        return 1
    return sumFunc(value-1)+value

print(sumFunc(int(input("Enter a number: "))))
