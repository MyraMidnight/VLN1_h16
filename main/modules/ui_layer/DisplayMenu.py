import sys
sys.path.insert(1, '../') #to be able to get to sibling directory

from ui_layer.InputHandler import InputHandler
from logic_layer.LLAPI import LLAPI

class DisplayMenu:
    """Handles the menu (input and printing right menus)"""
    def __init__(self):
        #dictionary for menu
        self.currentMenu = {}
        self.menuOptions = { 
            #---------- Create --------------
            "1": {
                "title": "Create new data",
                "function": "create" 
            },
            "1.1" : {
                "title": "Employee",
                "function": "create" # LLAPI().createEmployee
            },
            "1.2" : {
                "title": "Voyage",
                "function": "create" # LLAPI().createVoyage
            },
            "1.3" : {
                "title": "Destinations",
                "function" : LLAPI().createDestination
            },
            "1.4" : {
                "title": "Aircrafts",  
                "function": "create"
            },
            #---------- Get --------------
            "2" : {
                "title": "Get data",
                "function": "get"
            },
            "2.1" : {
                "title": "Crew",
                "function": "get"
            },
            "2.2" : {
                "title": "Voyages",
                "function": "get"
            },
            "2.3" : {
                "title": "Destinations",
                "function": "get"
            },
            "2.4" : {
                "title": "Aircrafts",
                "function": "get"
            },
            "2.4" : {
                "title": "Schedule",
                "function": "get"
            },
            #---------- Update --------------
            "3" : {
                "title": "Update data",
                "function": "update"
            },
            "3.1" : {
                "title": "Crew",
                "function": "update"
            },
            "3.2" : {
                "title": "Voyages",
                "function": "update"
            },
            "3.3" : {
                "title": "Destinations",
                "function": "update"
            }
        }
        self.menuLayout = {
            "main": ["1", "2", "3"],
            "create": ["1.1", "1.2", "1.3", "1.4"],
            "get": ["2.1", "2.2", "2.3", "2.4"],
            "update": ["3.1", "3.2", "3.3", "3.4"]
        }


    def printMenu(self,menu):
        """printMenu(menu), menus are: main, create, get, update"""
        #if the specified menu exists
        if menu in self.menuLayout:
            #find the correct menu from menuLayout and loop through the options

            self.currentMenu = self.menuLayout[menu]
            for count, item in enumerate(self.currentMenu,1):
                menuTitle = self.menuOptions[item]["title"]
                print("{}) {}".format(count, menuTitle))
            #use InputHandler to get the numbered input
            choice = InputHandler().numChoices(len(self.currentMenu), "What do you want to do? ")
            #compares choice to the last digit in the options
            if choice in [item[-1:] for item in self.currentMenu]:
                #finds the chosen option in the menuOptions
                chosenOption = self.menuOptions[self.currentMenu[int(choice)-1]]
                chosenFunction = chosenOption["function"]
                print(chosenOption["title"]) #just a test to show it found the option
                #then run the method connected to the chosen option
                if isinstance(chosenFunction, str) == True:
                    #prints the desired menu
                    print()
                    DisplayMenu().printMenu(chosenFunction)
                else:
                    #runs the desired function
                    chosenFunction()

DisplayMenu().printMenu("main")