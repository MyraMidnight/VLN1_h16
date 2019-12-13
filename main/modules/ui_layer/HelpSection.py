from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.InputHandler import InputHandler

class HelpSection:
    def __init__(self):
        self.__logo = """
                 |     |
                 | ___ |
              ----/___\----
  x--------------(  .  )--------------x
     x|x   |   |  \___/  |   |   x|x
      x    x   |___| |___|   x    x  
    _   __        _   __   ___     _      
   / | / /____ _ / | / /  /   |   (_)_____
  /  |/ // __ `//  |/ /  / /| |  / // ___/
 / /|  // /_/ // /|  /  / ___ | / // /    
/_/ |_/ \__,_//_/ |_/  /_/  |_|/_//_/  
        """

    def __printPage(self, data:list, header:str):
        """Handles pages"""
        DisplayScreen().printText(data,header)
        return InputHandler().confirmation("Press enter to go back to main menu...")



    def getHelp(self):
        """Compiles the basic help page"""
        basicPages = []
        basicPages.append("""
        Welcome to the NaN-Air flight managment tool
        For all your airbourn needs 

        Create voyages, new destinations, new employees and anything else you need
        View the data that has been gathered, such as departing flights
        Update the data you have, add crew to voyages among other things

        hope you enjoy your day, and hopefully made your work a little bit easier

        """)

        self.__printPage(basicPages, "Welcome!") 

