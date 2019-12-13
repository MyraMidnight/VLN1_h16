from modules.ui_layer.PrintHandler import PrintHandler

import os

class DisplayScreen:
    def __init__(self):
        self.__terminalSize = self.__getTerminalSize()
        self.__compiledSections = []
        self.minScreenWidth = 100
    
    def __getTerminalSize(self):
        width ,height= os.get_terminal_size()
        return {"height": height, "width": width}

    #===================================================================================
    # the PrintScreen method (optional 'frame' bool parameter)
    #===================================================================================
    def __printScreen(self, frame:bool = False):
        terminalWidth = self.__terminalSize["width"]
        lineWidth_int = self.minScreenWidth

        #------------ Print with frame------------------
        if frame:

            #find the widest line in any section
            for section in self.__compiledSections:
                longestString = len(max(section, key=len))
                if longestString > lineWidth_int:
                    lineWidth_int = longestString

            frameTop_str = "╔{}╗"
            frameBody_str = "║    {}    ║"
            frameBottom_str = "╚{}╝"
            horizontalBar = "═" * (lineWidth_int +len(frameBody_str) - len(frameBottom_str))

            #print the top
            print(frameTop_str.format(horizontalBar))

            #print the body of frame
            for section in self.__compiledSections:
                for line in section:
                    line = line.ljust(lineWidth_int)
                    line = frameBody_str.format(line)
                    print(line)
                # print("\n".join(section))
                # print()

            #print the bottom
            print(frameBottom_str.format(horizontalBar))

        #------------ Without Frame------------------
        else:
            #print the body of frame
            for section in self.__compiledSections:
                print("\n".join(section))
                print()
        
        #clears the compiledSections after each print, to prevent misprint
        self.__compiledSections = []

    #===================================================================================
    # Methods that can be called to display data
    #===================================================================================

    def printList(self, data:list, header:str = "Table of data",numList:bool = False, frame:bool = True):
        """Prints a given list, can optionally print the key as column title, else it uses the given titles"""

        #get the dataType for 
        sectionData_list = [
            {"header": [header]},
            {"list": data}
        ]

        self.__compiledSections =  PrintHandler().sectionHandler(sectionData_list)
        #prints the compiled sections
        self.__printScreen(frame)

    def printOptions(self, data:list, header:str = "List of choices", frame:bool = True):
        """Makes printing enumerated tables easy"""
        # compile the sections
        sectionData_list = [
            {"header": [header]},
            {"options": data}
        ]        
        self.__compiledSections = PrintHandler().sectionHandler(sectionData_list)
        #prints the compiled sections
        self.__printScreen(frame)

    def printText(self, data:list, header:str = "Information", frame:bool = True):
        """Prints a list of paragraphs"""
        # compile the sections
        sectionData_list = [
            {"header": [header]},
            {"text": data}
        ]        
        self.__compiledSections = PrintHandler().sectionHandler(sectionData_list)
        #prints the compiled sections
        self.__printScreen(frame)


    def printCustom(self, sectionData:list, frame:bool = True):
        """Lets you customize how the screen appears by providing sectionData, is framed by default"""
        
        self.__compiledSections = PrintHandler().sectionHandler(sectionData)
        #prints the compiled sections
        self.__printScreen(frame)