#
import sys
sys.path.insert(1, '../') 

#----- import the inner classes / methods
from data_layer.IOAPI import IOAPI
from logic_layer.CREATE import CreateLogic
from logic_layer.GET import GetLogic
from logic_layer.UPDATE import UpdateLogic

class LLAPI : 
    """Logic layer API handler"""
    def __init__(self):
        self.currentMenu = "main"

    #------- CREATE
    def createDestination(self): 
        return CreateLogic().createDestination()

    #------- GET

    #------- UPDATE
