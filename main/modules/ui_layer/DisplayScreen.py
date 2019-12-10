from modules.logic_layer.PrintHandler import PrintHandler

import os

class DisplayScreen:


    #===================================================================================
    # Methods that compile the screens for print
    #===================================================================================

    def printList(self, data:list, rowLimit:int = 0,colWidth:int = 10, formatTemplate: str = "", keys: bool = False, numList:bool = False):
        """Prints a given list, can optionally print the key as column title, else it uses the given titles"""

        #set the parameters
        self.__settings["lists"] = {"colWidth": colWidth, "formatTemplate": formatTemplate, "keys": keys,
        "numList": numList }
        
        #get the dataType for 
        screenData = [
            {"header": ["Header of screen"]},
            {"list": data}
        ]

        if rowLimit == 0:
            rowLimit = len(data)

        PrintHandler().printScreen(screenData)

            
    def printListFormat(self, data: list, formatTemplate: str = "", rowLimit:int = 0, enumerate:bool = False):
        """Prints data lists, takes in a list of dictionaries\n
            optional: can add 'type' parameter for specific format.\n
            Types: employees, cabincrew, pilots, flightattendants, planes, destinations
        """

        if rowLimit == 0:
            rowLimit = len(data)
    
        self.printList(data[:rowLimit])

    def printOptions(self, data:list, formatTemplate: str = ""):
        #The 'formatTemplate' parameter is obsolete, left it in because some might be using it
        """Makes printing enumerated tables easy"""

        screenData = [
            {"header": ["Header of screen"]},
            {"options": data}
        ]        
        PrintHandler().printScreen(screenData)

        #self.printListFormat(data, formatTemplate=formatTemplate, enumerate= True)