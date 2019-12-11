from modules.logic_layer.VoyageHandler import VoyageHandler

ROLE_PILOT = "Pilot"
ROLE_CC = "Cabin Crew"

RANK_CAPTAIN = "Captain"
RANK_COPILOT = "Co-Pilot"
RANK_FSM = "Flight Service Manager"
RANK_FA = "Flight Attendant"

AIRCRAFT_TYPE_FILE = "AircraftType.csv"
CREW_FILE = "Crew.csv"
DESTINATIONS_FILE = "NewDestinations.csv"

from modules.ui_layer.InputHandler import InputHandler
from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.DisplayScreen import DisplayScreen

class CreateLogic :
    """Create methods for logic layer"""

    def createDestination(self, ):
        """Create destination. Get destinationLand, destinationAirport, destinationFlightTime, 
         destinationDistance, destinationContactPerson and destinationEmergencyPhone."""

        print("\n  Creating new destination")
        destination_dict = {}

        self.destination = InputHandler.country("Input the new destination: ")
         
        # Airports
        # Get a list of dictionaties containing airports and destiations we currently fly to
        airport_data_list = IOAPI().opener(DESTINATIONS_FILE)
        #Creates a list of airports NaN Air flyes to 
        airport_list = []
        for a_line_dict in airport_data_list:
            airport_list.append(a_line_dict["id"])

        self.airport = InputHandler().airport(airport_list, "Input the ID (3 letters) of the new airport: ")
        self.flightTime = InputHandler().timeOnly("\nInput the time it takes to fly to {} from Iceland (HH:MM): ".format(self.airport))
        self.distanceFromIceland = InputHandler().distance("\nInput the distace from Iceland to {} (in km): ".format(self.airport))
        self.contactPerson = InputHandler().fullName("\nInput the full name of the contact person for the new destination, {}: ".format(self.airport))
        self.emergencyPhone = InputHandler().phoneNumber("\nInput the emergency phone number (7 digits) for the new destination, {}: ".format(self.airport))

        destination_dict["id"] = self.airport
        destination_dict["destination"] = self.destination
        destination_dict["flightDuration"] = self.flightTime
        destination_dict["distance"] = self.distanceFromIceland
        destination_dict["contactPerson"] = self.contactPerson
        destination_dict["emergencyPhone"] = self.emergencyPhone
    

        #Displays the input information and check if the user is happy with the info
        DisplayScreen().printList([destination_dict], colWidth = 14)
        confirmation_bool = InputHandler().yesOrNoConfirmation("Is this information correct (y/n)? ")
        if confirmation_bool:
            IOAPI().appender(DESTINATIONS_FILE, destination_dict)
    
    
    def createEmployee(self):
        """Assigns and holds onto the values given by input handler until all 
        information is fullfilled. Asks for confirmation. Turns the information
        into dict format and returns it #Should also write it into data"""
        
        employee_dict = {}

        #Personal information
        self.name = InputHandler().fullName("Input full name: ")
        self.ssn =  InputHandler().ssn("Input SSN: ")
        self.address = InputHandler().address("Input address: ")
        self.phonenumber = InputHandler().phoneNumber("Input a 7-digit phone number:")
        self.email = InputHandler().email("Input e-mail address: ")
        #Role
        self.role = InputHandler().role("Possible roles: \n 1) "+ ROLE_PILOT +" \n 2) "+ ROLE_CC +" \n" + "Choose role: ")

        #Rank
        if self.role == ROLE_PILOT:
            self.rank = InputHandler().rank(self.role, "Possible ranks: \n 1) "+ RANK_CAPTAIN +" \n 2) "+ RANK_COPILOT +" \n" + "Choose rank: ")
        else:
            self.rank = InputHandler().rank(self.role, "Possible ranks: \n 1) " + RANK_FSM + " \n 2) "+ RANK_FA + " \n" + "Choose rank: ")

        #License
        #Gets a list of dictionaries containing aircraft type specifications
        airplane_data_list = IOAPI().opener(AIRCRAFT_TYPE_FILE)
        #Creates a list of airplane types in the list
        airplaneType_list = []
        for a_line_dict in airplane_data_list:
            airplaneType_list.append(a_line_dict["planeTypeId"])

        #Gets input for license if relevant, sets to "N/A" if role = Cabin Crew
        if self.role == ROLE_PILOT:
            self.license = InputHandler().license(airplaneType_list,"Input license: ")
        else:
            self.license = "N/A"

        #Turns the inputs into a dict
        employee_dict["ssn"] = self.ssn
        employee_dict["name"] = self.name
        employee_dict["role"] = self.role
        employee_dict["rank"] = self.rank
        employee_dict["license"] = self.license
        employee_dict["address"] = self.address
        employee_dict["phonenumber"] = self.phonenumber
        employee_dict["email"] = self.email

        #Displays the input information
        DisplayScreen().printList([employee_dict], colWidth = 14)
        confirmation_bool = InputHandler().yesOrNoConfirmation("Is this information correct? (y/n)")
        if confirmation_bool:
            IOAPI().appender(CREW_FILE, employee_dict)
        #BEWARE.... C - krafa below
            # DisplayScreen().printList([employee_dict], colWidth = 15)
            # choiceNum_str = InputHandler().edit("Choose the column number to edit data \n Name: 1, SSN: 2, Address: 3, Phone number: 4, E-mail: 5, Role: 6, Rank: 7, License: 8")
            # editFunctionDict_list = {
            #     "1": {
            #         InputHandler().fullName("Input full name: "), employee_dict["Name"] 
            #     },
            #     "2":{ InputHandler().ssn("Input SSN: "), employee_dict["SSN"]
            #     },
            #     "3":{ InputHandler().address("Input address: ")
            #     },
            #     "4":{ InputHandler().phoneNumber("Input a 7-digit phone number:")
            #     },
            #     "5":{ InputHandler().email("Input e-mail address: ")
            #     },
            #     "6":{ InputHandler().role("Choose role: \n 1) "+ ROLE_PILOT +" \n 2) "+ ROLE_CC +" \n")
            #     },
            #     "7":{
            #     },
            #     "8":{ InputHandler().license(airplaneType_list,"Input license: ")
            #     }}
            # editFunctionDict_list[choiceNum_str][0]
        
    def createVoyage(self):
        return VoyageHandler().createVoyage()
        
