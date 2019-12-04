
#----- import the inner classes / methods
from CREATE import Create
from GET import Get
from UPDATE import Update

class LLAPI : 
    """Logic layer API handler"""
    #------- CREATE
    def createDestination(self): 
        return Create().createDestination()

    #------- GET

    #------- UPDATE