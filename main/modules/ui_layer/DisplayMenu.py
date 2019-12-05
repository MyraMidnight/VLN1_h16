class DisplayMenu:
    """Displays the menu"""

    def printHeader(self,menuHeader):
        """Prints the header"""
        print(menuHeader)

    def printMenu(self,menuOptions,currentMenu):
        """Takes in current menu as"""
        for count, item in enumerate(currentMenu,1):
            menuTitle = menuOptions[item]["title"]
            print("{}) {}".format(count, menuTitle))

