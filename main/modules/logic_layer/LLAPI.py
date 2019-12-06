import sys
sys.path.insert(1, '../') #to be able to get to siblingn directory

#----- import the inner classes / methods
from logic_layer.CREATE import CreateLogic
# from GET import GetLogic
# from UPDATE import UpdateLogic

class LLAPI : 
    """Logic layer API handler"""
    def __init__(self):
        self.currentMenu = "main"

    #------- CREATE
    def createDestination(self): 
        return (CreateLogic().createDestination())

    #------- GET

    #------- UPDATE
