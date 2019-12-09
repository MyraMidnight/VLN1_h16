#
#----- import the inner classes / methods
# from data_layer.IOAPI import IOAPI
from modules.logic_layer.CreateLogic import CreateLogic
from modules.logic_layer.GetLogic import GetLogic
from modules.logic_layer.UpdateLogic import UpdateLogic
from modules.ui_layer.InputHandler import InputHandler

class LLAPI : 
    """Logic layer API handler"""
    #------- CREATE
    def createDestination(self): 
        """Create a new destination. Requests input for destinationLand, destinationAirport, 
        destinationFlightTime, destinationDistance, destinationContactPerson and destinationEmergencyPhone."""
        return CreateLogic().createDestination()
    

    def createEmployee(self):
        """Method that creates employee, requests input for name, ssn, address, mobilePhone, email, role, rank and license,. 
        Adds the employee to the registry. """
        return CreateLogic().createEmployee()
    

    def createPlane(self):
        """Method that creates new plane, requests input for planeName, and planeType. Adds the plane to the registry"""


    def createVoyage(self):
        """Creates a voyage by creating two flights and adding them to the registry. (flugin hafa sitthvort flugnúmerið)
            (áfangastaður, dagsetning, brottfaratími frá Íslandi og aftur til baka til Íslands)) """
        return CreateLogic().createVoyage()

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
    
    def getVoyages(self):
        return GetLogic().getVoyages()


    #------- UPDATE
    def updateVoyage(self):
        """see the info about the voyage (see the staff that are working on that voyage). Then you can add or update the role you want to change """
    

    def updateEmployee(self):
        """choose a employee (get a list and choose from the list). Get the info about the chosen employee and then choose what info you want to change. 
        Then the user will be asked if he wants to save the changes. Save the new information about the employee to the list about all employees """
    
    
    def updateDestination(self):
        """get the info about the chosen destination. The user can change the contact person and the emergency phone number """
    
