#
#----- import the inner classes / methods
# from data_layer.IOAPI import IOAPI
from modules.logic_layer.CREATE import CreateLogic
from modules.logic_layer.GET import GetLogic
# from logic_layer.UPDATE import UpdateLogic

class LLAPI : 
    """Logic layer API handler"""
    def __init__(self):
        self.currentMenu = "main"


    #------- CREATE
    def createDestination(self): 
        return CreateLogic().createDestination()
    

    def createEmployee(self):
        """method that creates employee, requests input for name, ssn, address, homePhone, mobilePhone and email. 
        Adds the employee to the registry. """
    

    def createPlane(self):
        """Method that creates new plane, requests input for planeName, and planeType. Adds the plane to the registry"""


    def createVoyage(self):
        """ """


    #------- GET
    def getSingleEmployee(self):
        return GetLogic().getSingleEmployee()
    
    def getPilots(self):
        return GetLogic().getPilots()
    
    def getFlightAttendants(self):
        return GetLogic().getFlightAttendants()
    
    def getAllCrew(self):
        return GetLogic().getAllCrew()
    
    def getPlanes(self):
        return GetLogic().getPlanes()
    
    def getDestinations(self):
        return GetLogic().getDestinations()


    #------- UPDATE
    def updateVoyage(self):
        """ """
    

    def updateVoyage(self):
        """ """
    
    
    def updateVoyage(self):
        """ """
    
