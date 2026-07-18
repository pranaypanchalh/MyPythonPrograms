from resources import RESOURCES as rcs
from resources import MENU as menu
import elements as el

sectionWidth = 50 #width of the sections
count = 0 #variable for count only
totalNumberOfItems = [] #list of number eg if 5 items ["1","2","3","4","5"]
machineMoney = 0 #total money recieved 
resourceSufficient = [] #adds false when an ingredient is insufficient 
resourcesList = rcs.keys() #adds total resources name as list
el.coffeeIcon()
el.section(sectionWidth)
el.welcomeBanner()

for coffee in menu: #prints the available options
    count += 1
    totalNumberOfItems.append(str(count))
    el.button(count, coffee, menu[coffee]["cost"])
    #print(f"{count}. {coffee.title()} - ${menu[coffee]["cost"]}")
count = 0 #reset count after use
while True:
    el.section(sectionWidth)
    customerChoice = input("What would you like to have?:") #enter customer choice
    resourceSufficient = []

    if customerChoice != "report" and customerChoice in totalNumberOfItems: #check if user has enetered any choice other than report or unavailable option or spelling mistake
        customerChoiceInt = (int(customerChoice) - 1) #decreases number by one for list indexing or gathering information from list
        coffeeList = list(menu.keys()) #list all coffee menu from MENU

        for checkResources in menu[coffeeList[customerChoiceInt]]["ingredients"]: #check if the ingredients are available for vending the coffee
            if rcs[checkResources] >= menu[coffeeList[customerChoiceInt]]["ingredients"][checkResources]:
                resourceSufficient.append(True) #appends when the ingridient is sufficient
            else:
                resourceSufficient.append(False) #appends when the ingridient is insufficient

        if False not in resourceSufficient:
            while True:
                el.paymentBanner()
                payConfirmation = input(f"Your {coffeeList[customerChoiceInt].title()} is here! press P to pay ${menu[coffeeList[customerChoiceInt]]["cost"]}:").upper() #input for payment confirmation

                if payConfirmation == "P": #check state
                    for resources in menu[coffeeList[customerChoiceInt]]["ingredients"]: #gets all ingridients from selected option from menu and divides it from total resources
                        rcs[resources] = rcs[resources] - menu[coffeeList[customerChoiceInt]]["ingredients"][resources] #divide      
                    machineMoney += menu[coffeeList[customerChoiceInt]]["cost"]
                    el.section(sectionWidth)
                    el.thankYouBanner()
                else:
                    print("Transaction has been cancelled! Please press P next time")
                break
        else:
            el.sorryBanner()
            print("Insufficient resources please choose other item or comeback again.")
            

    elif customerChoice == "report":
        el.section(sectionWidth)
        print("Resources left:\n")
        count = 0
        for resources in rcs:
            count += 1
            print(f"{count}. {resources} : {rcs[resources]}")
        print(machineMoney)
    
    elif customerChoice != "report" and customerChoice not in totalNumberOfItems and customerChoice != "exit":
        print("Please enter valid option")
    
    elif customerChoice == "exit":
        el.section(sectionWidth)
        el.exiting()
        print("Exiting...")
        break