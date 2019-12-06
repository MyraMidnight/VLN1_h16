import sys
sys.path.insert(1, '../../') #to be able to get to sibling directory

from LLAPI import LLAPI
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayMenu import DisplayMenu

class MenuHandler:
    """Handles the menu (input and printing right menus)"""
    def __init__(self):
        self.currentLocation = "0"
        self.currentMenu = {}
        self.menuOptions = { 
            #---------- Create --------------
            "0": {
                "title": "Main menu",
                "function": "create" 
            },
            "1": {
                "title": "Create new data",
                "function": "create" 
            },
            "1.1" : {
                "title": "Employee",
                "function": "main" # LLAPI().createEmployee
            },
            "1.2" : {
                "title": "Voyage",
                "function": "main" # LLAPI().createVoyage
            },
            "1.3" : {
                "title": "Destinations",
                "function" : LLAPI().createDestination
            },
            "1.4" : {
                "title": "Aircrafts",  
                "function": "main"
            },
            #---------- Get --------------
            "2" : {
                "title": "Get data",
                "function": "get"
            },
            "2.1" : {
                "title": "Crew",
                "function": "main"
            },
            "2.2" : {
                "title": "Voyages",
                "function": "main"
            },
            "2.3" : {
                "title": "Destinations",
                "function": "main"
            },
            "2.4" : {
                "title": "Aircrafts",
                "function": "main"
            },
            "2.4" : {
                "title": "Schedule",
                "function": "main"
            },
            #---------- Update --------------
            "3" : {
                "title": "Update data",
                "function": "update"
            },
            "3.1" : {
                "title": "Crew",
                "function": "main"
            },
            "3.2" : {
                "title": "Voyages",
                "function": "main"
            },
            "3.3" : {
                "title": "Destinations",
                "function": "main"
            }
        }
        self.menuLayout = {
            "main": ["1", "2", "3"],
            "create": ["1.1", "1.2", "1.3", "1.4"],
            "get": ["2.1", "2.2", "2.3", "2.4"],
            "update": ["3.1", "3.2", "3.3"]
        }

    def displayMenu(self,menu:str = "main"):
        """printMenu(menu), menus are: main, create, get, update"""
        #if the menu
        if menu in self.menuLayout:
            self.currentMenu = self.menuLayout[menu]
            
            #find the menu header title
            if len(self.currentMenu[0]) == 1:
                menuTitle = self.menuOptions["0"]["title"]
            else: 
                menuTitle = self.menuOptions[self.currentMenu[0][:1]]["title"]
            #print the header and menu
            DisplayMenu().printHeader(menuTitle)
            DisplayMenu().printMenu(self.menuOptions,self.currentMenu)

            #prompt user to input the number of chosen option
            choice_int = InputHandler().numChoices(len(self.currentMenu), "What do you want to do? ")
            chosenOption = self.menuOptions[self.currentMenu[choice_int]]

            #then run the method connected to the chosen option
            chosenFunction = chosenOption["function"]
            if isinstance(chosenFunction, str) == True:
                #prints the desired menu
                MenuHandler().displayMenu(chosenFunction)
            else:
                #runs the desired function
                chosenFunction()