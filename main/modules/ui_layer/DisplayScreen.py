from modules.logic_layer.PrintHandler import PrintHandler

import os

class DisplayScreen:
    def __init__(self):
        self.__terminalSize = self.__getTerminalSize()
        self.__compiledSections = []
    
    def __getTerminalSize(self):
        width ,height= os.get_terminal_size()
        return {"height": height, "width": width}

    #===================================================================================
    # the PrintScreen method (optional 'frame' bool parameter)
    #===================================================================================
    def __printScreen(self, frame:bool = False):
        
        thickBar = "#"*self.__terminalSize["width"]
        frame_str = "|{}|"

        #------------ Print with frame------------------
        if frame:
            #print the top
            print(thickBar)

            #print the body of frame
            for section in self.__compiledSections:
                print("\n".join(section))
                print()

            #print the bottom
            print(thickBar)

        #------------ Without Frame------------------
        else:
            #print the body of frame
            for section in self.__compiledSections:
                print("\n".join(section))
                print()

    #===================================================================================
    # Methods that can be called to display data
    #===================================================================================

    def printList(self, data:list, rowLimit:int = 0,colWidth:int = 10, formatTemplate: str = "", keys: bool = False, numList:bool = False):
        """Prints a given list, can optionally print the key as column title, else it uses the given titles"""

        #set the parameters
        # self.__settings["lists"] = {"colWidth": colWidth, "formatTemplate": formatTemplate, "keys": keys,
        # "numList": numList }
        
        #get the dataType for 
        sectionData_list = [
            {"header": ["Header of screen"]},
            {"list": data}
        ]

        if rowLimit == 0:
            rowLimit = len(data)

        self.__compiledSections =  PrintHandler().sectionHandler(sectionData_list)
        #prints the compiled sections
        self.__printScreen()

            
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

        sectionData_list = [
            {"header": ["Header of screen"]},
            {"options": data}
        ]        
        self.__compiledSections = PrintHandler().sectionHandler(sectionData_list)
        #prints the compiled sections
        self.__printScreen()
        #self.printListFormat(data, formatTemplate=formatTemplate, enumerate= True)

    def printCustom(self, sectionData:list, frame:bool = True):
        """Lets you customize how the screen appears by providing sectionData, is framed by default"""
        
        self.__compiledSections = PrintHandler().sectionHandler(sectionData)
        #prints the compiled sections
        self.__printScreen()