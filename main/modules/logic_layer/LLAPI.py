import sys
sys.path.insert(1, '../') #to be able to get to sibling directory

from data_layer.IOAPI import IOAPI
#----- import the inner classes / methods
from logic_layer.CREATE import CreateLogic
# from logic_layer.GET import GetLogic
# from logic_layer.UPDATE import UpdateLogic

class LLAPI : 
    """Logic layer API handler"""
    def __init__(self):
        self.currentMenu = "main"

    #------- CREATE
    def createDestination(self): 
        return CreateLogic().createDestination()

    #------- GET

    #------- UPDATE
