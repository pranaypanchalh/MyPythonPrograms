import CaesarCipherEncode as CCE
import CaesarCipherDecode as CCD

operation = input("Press E for encode or D for decode").lower()
message = input("Enter your message:").lower()
key = int(input("Enter your key for the message:"))
while True:
    if operation == "e":
        CCE.encode(message,key)
        break
    elif operation == "d":
        CCD.decode(message,key)
        break
    elif operation == "exit":
        break
    else:
        print("You have eneterd the wrong choice.")