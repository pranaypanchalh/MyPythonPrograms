import resources as rcs
import elements as el

class Machine(rcs.Resources):
    def __init__(self):
        count = 0
        customerChoose = 0
        menuItemsList = []
        totalItemsAsList = [] #stores ["1","2","3"]
        for menuItems in rcs.Resources.MENU:
            count += 1
            menuItemsList.append(menuItems)
            totalItemsAsList.append(str(count))
    def displayMenu(self):
        el.Elements.welcomeBanner()
        for count, items in enumerate(rcs.Resources.MENU):
            el.Elements.button(count+1, items.title(), rcs.Resources.MENU[items]["cost"])
    def chooseOption(self):
        Machine.customerChoose = input("Please choose from Menu: ")
    def checkOption(self):
        if Machine.customerChoose in Machine.totalItemsAsList:
            
Start = Machine()
Start.displayMenu()