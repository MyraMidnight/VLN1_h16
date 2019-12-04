import sys
sys.path.insert(1, '../') #to be able to get to siblingn directory

from logic_layer.LLAPI import LLAPI

class DisplayMenu:
    """Handles the menu (input and printing right menus)"""
    def __init__(self):
        #dictionary for menu
        self.menuOptions = { 
            #---------- Create --------------
            "1": {
                "title": "Create new data",
                "function": ""
            },
            "1.1" : {
                "title": "Crew",
                "function": ""
            },
            "1.2" : {
                "title": "Voyages",
                "function": ""
            },
            "1.3" : {
                "title": "Destinations",
                "function": LLAPI().createDestination
            },
            "1.4" : {
                "title": "Aircrafts",
                "function": ""
            },
            #---------- Get --------------
            "2" : {
                "title": "Get data",
                "function": ""
            },
            "2.1" : {
                "title": "Crew",
                "function": ""
            },
            "2.2" : {
                "title": "Voyages",
                "function": ""
            },
            "2.3" : {
                "title": "Destinations",
                "function": ""
            },
            "2.4" : {
                "title": "Aircrafts",
                "function": ""
            },
            "2.4" : {
                "title": "Schedule",
                "function": ""
            },
            #---------- Update --------------
            "3" : {
                "title": "Update data",
                "function": ""
            },
            "3.1" : {
                "title": "Crew",
                "function": ""
            },
            "3.2" : {
                "title": "Voyages",
                "function": ""
            },
            "3.3" : {
                "title": "Destinations",
                "function": ""
            }
        }
        self.menuLayout = {
            "main": ["1", "2", "3"],
            "create": ["1.1", "1.2", "1.3", "1.4"],
            "get": ["2.1", "2.2", "2.3", "2.4"],
            "update": ["3.1", "3.2", "3.3", "3.4"]
        }

    def runFunction(self,function):
        """runs a function defined in the options"""
        function()


    def printMenu(self,menu):
        """printMenu(menu), menus are: main, create, get, update"""
        #if the specified menu exists
        if menu in self.menuLayout:
            #find the correct menu from menuLayout and loop through the options

            currentMenu = self.menuLayout[menu]
            for count, item in enumerate(currentMenu,1):
                print("{}) {}".format(count, self.menuOptions[item]["title"]))
            choice = input("What do you want to do? ").strip()
            #compares choice to the last digit in the options
            if choice in [item[-1:] for item in currentMenu]:
                #finds the chosen option in the menuOptions
                chosenOption = self.menuOptions[currentMenu[int(choice)-1]]
                print(chosenOption["title"]) #just a test to show it found the option
                #then run the method connected to the chosen option
                self.runFunction(chosenOption["function"])

DisplayMenu().printMenu("get")
