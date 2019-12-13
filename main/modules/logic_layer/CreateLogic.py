from modules.logic_layer.VoyageHandler import VoyageHandler

ROLE_PILOT = "Pilot"
ROLE_CC = "Cabin Crew"

RANK_CAPTAIN = "Captain"
RANK_COPILOT = "Co-Pilot"
RANK_FSM = "Flight Service Manager"
RANK_FA = "Flight Attendant"

from modules.ui_layer.InputHandler import InputHandler
from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.DisplayScreen import DisplayScreen

class CreateLogic :
    """Create methods for logic layer"""
    def __init__(self, dataFiles):
        self.dataFiles = dataFiles

    #===================================================================================
    # Create destination
    #===================================================================================

    def createDestination(self):
        """Create destination. Get destinationLand, destinationAirport, destinationFlightTime, 
         destinationDistance, destinationContactPerson and destinationEmergencyPhone."""
         
        # Airports
        # Get a list of dictionaties containing airports and destiations we currently fly to
        airport_data_list = IOAPI().opener(self.dataFiles["DESTINATIONS_FILE"])
        #Creates a list of airports NaN Air flyes to 
        airport_list = []
        for a_line_dict in airport_data_list:
            airport_list.append(a_line_dict["id"])
        #print existing destinations
        destinationSections = [
            {"header": ["Creating new destination", "List of existing destinations "]},
            {"list": airport_data_list},
            {"text": ["Please input the required below for creating new destination"]}
        ]
        DisplayScreen().printCustom(destinationSections)
        destination_dict = {}

        # imput the data
        self.destination = InputHandler().country("Input the city where the new destination is located: ")
        self.destination_airport = InputHandler().airport(airport_list, "\nInput the ID (3 letters) of the new airport: ")
        self.destination_flightTime = InputHandler().timeOnly("\nInput the time it takes to fly to {} from Iceland (HH:MM): ".format(self.airport))
        self.destination_distanceFromIceland = InputHandler().distance("\nInput the distace from Iceland to {} (in km): ".format(self.airport))
        self.destination_contactPerson = InputHandler().fullName("\nInput the full name of the contact person for the new destination, {}: ".format(self.airport))
        self.destination_emergencyPhone = InputHandler().phoneNumber("\nInput the emergency phone number (7 digits) for the new destination, {}: ".format(self.airport))

        destination_dict["id"] = self.destination_airport
        destination_dict["destination"] = self.destination
        destination_dict["flightDuration"] = self.destination_flightTime
        destination_dict["distance"] = self.destination_distanceFromIceland
        destination_dict["contactPerson"] = self.destination_contactPerson
        destination_dict["emergencyPhone"] = self.destination_emergencyPhone
    

        #Displays the input information and check if the user is happy with the info
        DisplayScreen().printList([destination_dict], header = "Creating new destination, check if info correct", frame = True)
        confirmation_bool = InputHandler().yesOrNoConfirmation("Is this information correct (y/n)? ")
        if confirmation_bool:
            IOAPI().appender(self.dataFiles["DESTINATIONS_FILE"], destination_dict)
    
    #===================================================================================
    # Create Employee
    #===================================================================================
    
    def createEmployee(self):
        """Assigns and holds onto the values given by input handler until all 
        information is fullfilled. Asks for confirmation. Turns the information
        into dict format and returns it #Should also write it into data"""
        

        #Personal information
        self.employee_name = InputHandler().fullName("Input full name: ")
        self.employee_ssn =  InputHandler().ssn("Input SSN: ")
        self.employee_address = InputHandler().address("Input address: ")
        self.employee_phonenumber = InputHandler().phoneNumber("Input a 7-digit phone number:")
        self.employee_email = InputHandler().email("Input e-mail address: ")
        #Role

        self.employee_role = InputHandler().role("Choose role: ")

        #Rank

        self.employee_rank = InputHandler().rank(self.employee_role)


        #License
        #Gets a list of dictionaries containing aircraft type specifications
        airplane_data_list = IOAPI().opener(self.dataFiles["AIRCRAFT_TYPE_FILE"])
        #Creates a list of airplane types in the list
        airplaneType_list = []
        for a_line_dict in airplane_data_list:
            airplaneType_list.append(a_line_dict["planeTypeId"])

        #Gets input for license if relevant, sets to "N/A" if role = Cabin Crew
        self.employee_license = InputHandler().license(self.employee_role, airplaneType_list,"Choose license: ")

        #Turns the inputs into a dict
        employee_dict = {}
        employee_dict["ssn"] = self.employee_ssn
        employee_dict["name"] = self.employee_name
        employee_dict["role"] = self.employee_role
        employee_dict["rank"] = self.employee_rank
        employee_dict["licence"] = self.employee_license
        employee_dict["address"] = self.employee_address
        employee_dict["phonenumber"] = self.employee_phonenumber
        employee_dict["email"] = self.employee_email

        #Displays the input information
        
        employeeInfo_str = "{}: {}"
        employeeInfo_list = [employeeInfo_str.format(key,value) for key, value in employee_dict.items()]

        DisplayScreen().printText(["\n".join(employeeInfo_list)],header = "Employee info: ")
        #Asks for confirmation. If negative starts the editing process
        if InputHandler().yesOrNoConfirmation("Is this information correct? (y/n): "):
            edit_bool = False
        else: 
            edit_bool = True

        #Runs editing as long as the user confirmation is negative
        while edit_bool:
            #Creates a list of editing options
            options_list = [{"Edit choices:": "SSN"},{"Edit choices:": "Name"},{"Edit choices:":"Role"}, {"Edit choices:":"Rank"},{"Edit choices:": "License"},{"Edit choices:": "Address"}, {"Edit choices:":"Phone"}, {"Edit choices:": "Email"}]
            #Prints the beforementioned list of options
            DisplayScreen().printOptions(options_list, header = "")
            #Asks user to choose what he wants to edit
            choice_str = InputHandler().multipleNumChoices(options_list, "Choose data to edit: ")

            if choice_str == "SSN":
                employee_dict[choice_str.lower()] = InputHandler().ssn("Input SSN: ")
            elif choice_str == "Name":
                employee_dict[choice_str.lower()] = InputHandler().fullName("Input full name: ")
            elif choice_str == "Address":
                employee_dict[choice_str.lower()] = InputHandler().address("Input address: ")
            elif choice_str == "Phone":
                employee_dict[choice_str.lower()] = InputHandler().phoneNumber("Input a 7-digit phone number: ")
            elif choice_str == "Email":
                employee_dict[choice_str.lower()] = InputHandler().email("Input e-mail address: ")
            elif choice_str == "Role":
                employee_dict["role"], employee_dict["rank"], employee_dict["licence"] = InputHandler().roleUpdate(airplaneType_list)
            elif choice_str == "Rank":
                employee_dict[choice_str.lower()] = InputHandler().rank(employee_dict["role"],"Choose rank: ")
            elif choice_str == "Licence":
                employee_dict[choice_str.lower()] = InputHandler().license(employee_dict["role"], airplaneType_list,"Input licence: ")

            #Prints the results of editing and asks for confirmation
            DisplayScreen().printList([employee_dict], header = "Employee info: ", frame = True)
            if InputHandler().yesOrNoConfirmation("Is this information correct? (y/n): "):
                edit_bool = False

        #Adds the employee to the crew file
        IOAPI().appender(self.dataFiles["CREW_FILE"], employee_dict)


    #===================================================================================
    # Create plane
    #===================================================================================

    def createPlane(self):
        """Method that creates new plane, requests input for planeName, and planeType. 
        Adds the plane to the registry"""

        plane_dict = {}

        #Takes in input for plane insignia and puts it under "planeInsignia" key in plane_dict
        plane_dict["planeInsignia"] = InputHandler().planeInsignia("Input plane insignia (e.g. TF-XXX): ")

        #Input for plane Type ID
        plane_dict["planeTypeId"] = InputHandler().planetype()
        plane_dict["manufacturer"] = InputHandler().strNoCheck("Input plane manufacturer: ")
        plane_dict["capacity"] = InputHandler().digit("Input plane seating capacity: ")
        #Input confirmation
        DisplayScreen().printList([plane_dict])
        confirmation_bool = InputHandler().yesOrNoConfirmation("Is this information correct? (y/n)")
        if confirmation_bool:
        #Appending the input info to aircraft file
            IOAPI().appender(self.dataFiles["AIRCRAFT_FILE"], plane_dict)
        

    #===================================================================================
    # Create Voyage
    #===================================================================================

    def createVoyage(self):
        return VoyageHandler(dataFiles=self.dataFiles).createVoyage()
        
