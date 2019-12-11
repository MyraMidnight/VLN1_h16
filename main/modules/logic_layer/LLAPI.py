#
#----- import the inner classes / methods
# from data_layer.IOAPI import IOAPI
from modules.logic_layer.CreateLogic import CreateLogic
from modules.logic_layer.GetLogic import GetLogic
from modules.logic_layer.UpdateLogic import UpdateLogic
from modules.ui_layer.InputHandler import InputHandler

DATA_FILES = {
    "AIRCRAFT_FILE" : "Aircraft.csv",
    "AIRCRAFT_TYPE_FILE" : "AircraftType.csv",
    "CREW_FILE" : "Crew.csv",
    "DESTINATIONS_FILE" : "NewDestinations.csv",
    "UPCOMING_FLIGHTS_FILE": 'NewUpcomingFlights.csv'
}
class LLAPI : 
    """Logic layer API handler"""

    def __init__(self):
        self.createLogic = CreateLogic(DATA_FILES)
        self.getLogic = GetLogic(DATA_FILES)
        self.updateLogic = UpdateLogic(DATA_FILES)
    
    #------- CREATE
    def createDestination(self): 
        """Create a new destination. Requests input for destinationLand, destinationAirport, 
        destinationFlightTime, destinationDistance, destinationContactPerson and destinationEmergencyPhone."""
        return self.createLogic.createDestination()
    

    def createEmployee(self):
        """Method that creates employee, requests input for name, ssn, address, mobilePhone, email, role, rank and license,. 
        Adds the employee to the registry. """
        return self.createLogic.createEmployee()
    

    def createPlane(self):
        """Method that creates new plane, requests input for planeName, and planeType. Adds the plane to the registry"""
        return self.createLogic.createPlane()

    def createVoyage(self):
        """Creates a voyage by creating two flights and adding them to the registry. (flugin hafa sitthvort flugnúmerið)
            (áfangastaður, dagsetning, brottfaratími frá Íslandi og aftur til baka til Íslands)) """
        return self.createLogic.createVoyage()

    #------- GET
    def getSingleEmployee(self):
        return self.getLogic.getSingleEmployee()
    
    def getPilots(self):
        return self.getLogic.getPilots()
    
    def getFlightAttendants(self):
        return self.getLogic.getFlightAttendants()
    
    def getAllCrew(self):
        return self.getLogic.getAllCrew()
    
    def getPlanes(self):
        return self.getLogic.getPlanes()
    
    def getDestinations(self):
        return self.getLogic.getDestinations()
    
    def getVoyages(self):
        return self.getLogic.getVoyages()

    def getAway(self):
        return self.getLogic.getAway()

    def getWorking(self):
        return self.getLogic.getWorking()
    
    def getWeekWork(self):
        return self.getLogic.getWeekWork()
    
    def getPilotsByLicence(self):
        return self.getLogic.getPilotsByLicence()
    
    def printPilotsByLicence(self):
        return self.getLogic.printPilotsByLicence()
    
    def licenceByCount(self):
        return self.getLogic.licenceByCount()

    #------- UPDATE
    def updateVoyage(self):
        """see the info about the voyage (see the staff that are working on that voyage). Then you can add or update the role you want to change """
        return self.updateLogic.updateVoyage()

    def updateEmployee(self):
        """choose a employee (get a list and choose from the list). Get the info about the chosen employee and then choose what info you want to change. 
        Then the user will be asked if he wants to save the changes. Save the new information about the employee to the list about all employees """
        return self.updateLogic.updateEmployee()
    
    def updateDestination(self):
        """get the info about the chosen destination. The user can change the contact person and the emergency phone number """
    
        # return self.updateLogic.updateDestination()
