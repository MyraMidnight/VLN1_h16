#
import sys
sys.path.insert(1, '../') 

#----- import the inner classes / methods
# from data_layer.IOAPI import IOAPI
from logic_layer.CREATE import CreateLogic
# from logic_layer.GET import GetLogic
# from logic_layer.UPDATE import UpdateLogic

class LLAPI : 
    """Logic layer API handler"""
    def __init__(self):
        self.currentMenu = "main"


    #------- CREATE
    def createDestination(self): 
        """Create a new destination. Requests input for destinationLand, destinationAirport, 
        destinationFlightTime, destinationDistance, destinationContactPerson and destinationEmergencyPhone."""
        return CreateLogic().createDestination()
    

    def createEmployee(self):
        """method that creates employee, requests input for name, ssn, address, homePhone, mobilePhone and email. 
        Adds the employee to the registry. """
    

    def createPlane(self):
        """Method that creates new plane, requests input for planeName, and planeType. Adds the plane to the registry"""


    def createVoyage(self):
        """Creates a voyage by creating two flights and adding them to the registry. (flugin hafa sitthvort flugnúmerið)
            (áfangastaður, dagsetning, brottfaratími frá Íslandi og aftur til baka til Íslands)) """


    #------- GET
    def getSingleEmployee(self):
        """method that gets the information about a single employee from the data layer """
    


    def getAllEmployees(self):
        """get a list of all employees, both pilots and flight attendants and show their rank, licence"""


    def getPilots(self):
        """get a list of all pilots and then make the user choose the pilot the user wants or 
        the user inputs the pilots ssn and gets the info of the pilot"""
    

    def getFlightAttendants(self):
        """get a list of all flight attendants and then make the user choose the flight attendant the user wants or 
        the user inputs the flight attendants ssn and gets the info of the flight attendants"""




    def getPlanes(self):
        """get a list of all planes containing the info fx plane name, plane type, plane seats """


    def getDestinations(self):
        """get a list of all destinations, the airport, the contact person and the emergency phone number """

    def getCrew(self):
        """get a list of the crew"""
    
    def getSchedule(self):
        """Get a list of the upcoming schedule (maybe for some specific day) """

    def getOnShift(self):
        """get a list of employees that are on shift on a specific day. On the list you can see the employees' role and rank and on what voyage they are working on  """

    def getOffShift(self):
        """get a list of employees that are off shift on a specific day. On the list you can see the employees' role and rank"""



    #------- UPDATE
    def updateVoyage(self):
        """see the info about the voyage (see the staff that are working on that voyage). Then you can add or update the role you want to change """
    

    def updateEmployee(self):
        """choose a employee (get a list and choose from the list). Get the info about the chosen employee and then choose what info you want to change. 
        Then the user will be asked if he wants to save the changes. Save the new information about the employee to the list about all employees """
    
    
    def updateDestination(self):
        """get the info about the chosen destination. The user can change the contact person and the emergency phone number """
    
