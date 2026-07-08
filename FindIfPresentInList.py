lis = ["Pranay", "John", "Alice", "Bob"]
name = input("Enter a name to check if it is present in the list: ")
if name in lis:
    print(f"{name} is present in the list.")
else:
    print(f"{name} is not present in the list.")