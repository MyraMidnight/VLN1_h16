
from modules.logic_layer.LLAPI import LLAPI
from modules.ui_layer.InputHandler import InputHandler

class MenuHandler:
    """Handles the menu (input and printing right menus)"""
    def __init__(self, menu:str = "main"):
        self.currentLocation_str = menu.lower()
        self.breadcrumbs = []
        self.currentMenu_list = {}
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
                "function": LLAPI().createEmployee
            },
            "1.2" : {
                "title": "Voyage",
                "function": LLAPI().createVoyage
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
                "function": LLAPI().getVoyages
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
                "function": "schedule"
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
            "2.1.5" : {
                "title": "Pilots by licence",
                "function": LLAPI().getPilotsByLicence
            },
            "2.5.1" : {
                "title": "Employees not working",
                "function": LLAPI().getAway
            },
            "2.5.2" : {
                "title": "Employees working and destination",
                "function": LLAPI().getWorking
            },
            "2.5.3" : {
                "title": "Single employee week work schedule",
                "function": LLAPI().getWeekWork
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
            "getcrew" : ["2.1.1", "2.1.2", "2.1.3", "2.1.4", "2.1.5"],
            "schedule" : ["2.5.1","2.5.2","2.5.3"],
            "update": ["3.1", "3.2", "3.3"],
        }

    def printHeader(self,menuHeader):
        """Prints the header"""
        #print("\n")
        print("\n", " / ".join(self.breadcrumbs))

    def printMenu(self,menuOptions,currentMenu):
        """Takes in current menu as"""
        for count, item in enumerate(currentMenu,1):
            menuTitle = menuOptions[item]["title"]
            print("{}) {}".format(count, menuTitle))
        print("(Press (q) to quit)")

    def displayMenu(self):
        """printMenu(menu), menus are: main, create, get, update"""
        #if the menu
        if self.currentLocation_str in self.menuLayout:
            self.currentMenu_list = self.menuLayout[self.currentLocation_str]
            
            #find the menu header title
            if len(self.currentMenu_list[0]) == 1:
                menuTitle = self.menuOptions["0"]["title"]
            else: 
                menuTitle = self.menuOptions[self.currentMenu_list[0][:-2]]["title"]
            
            if menuTitle not in self.breadcrumbs:
                self.breadcrumbs.append(menuTitle)

            if menuTitle == "Main menu":
                self.breadcrumbs = ["Main menu"]


            #print the header and menu
            self.printHeader(menuTitle)
            self.printMenu(self.menuOptions,self.currentMenu_list)

            #prompt user to input the number of chosen option
            choice_str = InputHandler().numChoices(len(self.currentMenu_list), "What do you want to do? ")
            chosenOption = self.menuOptions[self.currentMenu_list[int(choice_str)-1]]

            #if exitKey was used
            if choice_str == False:
                #exit program if on main menu, else print main menu
                if self.currentLocation_str == "main":
                    if input("Are you sure you want to quit (y/n)? ").lower() == "y":
                        quit()
                    else:
                        self.currentLocation_str = "main"
                        self.displayMenu()
                else:
                    self.currentLocation_str = "main"
                    self.displayMenu()

            #then run the method connected to the chosen option
            chosenFunction = chosenOption["function"]
            if isinstance(chosenFunction, str) == True:
                #prints the desired menu
                subMenu = chosenFunction
                self.currentLocation_str = subMenu
                self.displayMenu()
            else:
                #runs the desired function
                chosenFunction()
                self.displayMenu()

        else: 
            # If the initial 'currentLocation' is not valid, then default to 'main'
            self.currentLocation_str = "main"
            self.displayMenu()