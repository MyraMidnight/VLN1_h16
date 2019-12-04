
#----- import the inner classes / methods
from .CREATE import CreateLogic
from .GET import GetLogic
from .UPDATE import UpdateLogic

class LLAPI : 
    """Logic layer API handler"""
    def __init__(self):
        self.currentMenu = "main"

    #------- CREATE
    def createDestination(self): 
        return CreateLogic().createDestination()

    #------- GET

    #------- UPDATE