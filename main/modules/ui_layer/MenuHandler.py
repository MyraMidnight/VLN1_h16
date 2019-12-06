
from modules.logic_layer.LLAPI import LLAPI
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayMenu import DisplayMenu

class MenuHandler:
    """Handles the menu (input and printing right menus)"""
    def __init__(self):
        self.currentLocation = "main"
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
                "function": "getcrew"
            },
            "2.2" : {
                "title": "Voyages",
                "function": "main"
            },
            "2.3" : {
                "title": "Destinations",
                "function": LLAPI().getDestinations
            },
            "2.4" : {
                "title": "Aircrafts",
                "function": LLAPI().getPlanes
            },
            "2.5" : {
                "title": "Schedule",
                "function": "main"
            },
            #---------- Get submenu ---------
            "2.1.1" : {
                "title": "Employee",
                "function": LLAPI().getSingleEmployee
            },
            "2.1.2" : {
                "title": "Crew (all employees)",
                "function": LLAPI().getAllCrew
            },
            "2.1.3" : {
                "title": "Pilots",
                "function": LLAPI().getPilots
            },
            "2.1.4" : {
                "title": "Flight Attendants",
                "function": LLAPI().getFlightAttendants
            },
            #---------- Update --------------
            "3" : {
                "title": "Update data",
                "function": "update"
            },
            "3.1" : {
                "title": "Crew",
                "function": "getcrew"
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
            "get": ["2.1", "2.2", "2.3", "2.4", "2.5"],
            "getcrew" : ["2.1.1", "2.1.2", "2.1.3", "2.1.4"],
            "update": ["3.1", "3.2", "3.3"],
            
        }

    def printHeader(self,menuHeader):
        """Prints the header"""
        print(menuHeader)

    def printMenu(self,menuOptions,currentMenu):
        """Takes in current menu as"""
        for count, item in enumerate(currentMenu,1):
            menuTitle = menuOptions[item]["title"]
            print("{}) {}".format(count, menuTitle))

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
            self.printHeader(menuTitle)
            self.printMenu(self.menuOptions,self.currentMenu)

            #prompt user to input the number of chosen option
            choice_int = InputHandler().numChoices(len(self.currentMenu), "What do you want to do? ")
            chosenOption = self.menuOptions[self.currentMenu[choice_int]]

            #then run the method connected to the chosen option
            chosenFunction = chosenOption["function"]
            if isinstance(chosenFunction, str) == True:
                #prints the desired menu
                self.currentLocation = chosenFunction
                self.displayMenu(chosenFunction)
            else:
                #runs the desired function
                chosenFunction()
                self.displayMenu(self.currentLocation)