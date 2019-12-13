
from modules.logic_layer.LLAPI import LLAPI
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.HelpSection import HelpSection

class MenuHandler:
    """Handles the menu (input and printing right menus)"""
    def __init__(self, menu:str = "main", logo:str = ""):
        self.__logo = logo
        self.minScreenWidth = 100
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
                "function": LLAPI().createPlane
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
                "function": "voyages"
            },
            "2.3" : {
                "title": "Destinations",
                "function": LLAPI().getDestinations
            },
            "2.4" : {
                "title": "Aircrafts",
                "function": "aircraft"
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
                "title": "Find pilots by licence",
                "function": LLAPI().getPilotsByLicence
            },
            "2.1.6" : {
                "title": "Sorted pilots by licence",
                "function": LLAPI().printPilotsByLicence
            },
            "2.2.1" : {
                "title": "All voyages",
                "function": LLAPI().getVoyages
            },
            "2.2.2" : {
                "title": "Voyages of a day",
                "function": LLAPI().getDayVoyages
            },
            "2.2.3" : {
                "title": "Voyages of week",
                "function": LLAPI().getWeekVoyages
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
            "2.4.1" : {
                "title": "All planes",
                "function": LLAPI().getPlanes
            },
            "2.4.2" : {
                "title": "Licences by plane type",
                "function": LLAPI().licenceByCount
            },
            #---------- Update --------------
            "3" : {
                "title": "Update data",
                "function": "update"
            },
            "3.1" : {
                "title": "Crew",
                "function": LLAPI().updateEmployee
            },
            "3.2" : {
                "title": "Voyages",
                "function": LLAPI().updateVoyage
            },
            "3.3" : {
                "title": "Destinations",
                "function": LLAPI().updateDestination
            }, 
            "4": {
                "title": "Help",
                "function": HelpSection().getHelp
            }
        }
        self.menuLayout = {
            "main": ["1", "2", "3", "4"],
            "create": ["1.1", "1.2", "1.3", "1.4"],
            "get": ["2.1", "2.2", "2.3", "2.4", "2.5"],
            "voyages":["2.2.1","2.2.2","2.2.3"],
            "getcrew" : ["2.1.1", "2.1.2", "2.1.3", "2.1.4", "2.1.5", "2.1.6"],
            "aircraft": ["2.4.1","2.4.2"],
            "schedule" : ["2.5.1","2.5.2","2.5.3"],
            "update": ["3.1", "3.2", "3.3"],
        }
        print(logo) #print logo on init :V

    def printHeader(self,menuHeader):
        """Prints the header"""
        #print("\n")

    def printMenu(self,menuOptions,currentMenu):
        """Takes in current menu as"""
        
        #format the options into strings for print
        breadCrumbs =  " / ".join(self.breadcrumbs)
        formattedMenu = [breadCrumbs, ""]

        for count, item in enumerate(currentMenu,1):
            menuTitle = menuOptions[item]["title"]
            formattedMenu.append("{}) {}".format(count, menuTitle))
        formattedMenu.append("")
        formattedMenu.append("Press (q) to quit")
        lineWidth_int = self.minScreenWidth

        frameTop_str = "╔{}╗"
        frameBody_str = "║    {}    ║"
        frameBottom_str = "╚{}╝"
        horizontalBar = "═" * (lineWidth_int +len(frameBody_str) - len(frameBottom_str))
        
        print(frameTop_str.format(horizontalBar))
        for line in formattedMenu:
            line = line.ljust(lineWidth_int)
            line = frameBody_str.format(line)
            print(line)

        print(frameBottom_str.format(horizontalBar))

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
            self.printMenu(self.menuOptions,self.currentMenu_list)

            #prompt user to input the number of chosen option
            choice_str = InputHandler().numChoices(len(self.currentMenu_list), "What do you want to do? ")
            chosenOption = self.menuOptions[self.currentMenu_list[int(choice_str)-1]]

            #if exitKey was used
            if choice_str == False:
                #exit program if on main menu, else print main menu
                if self.currentLocation_str == "main":
                    if input("\nAre you sure you want to quit (y/n)? ").lower() == "y":
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