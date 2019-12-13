from modules.logic_layer.GetLogic import GetLogic
from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.InputHandler import InputHandler
from modules.models.Voyage import Voyage #model class

from modules.ui_layer.DateUtil import DateUtil
import datetime

from operator import itemgetter #for sorting list of dictionaries by key
class UpdateLogic :
    """Update methods for logic layer"""
    def __init__(self, dataFiles):
        self.dataFiles = dataFiles #gets the file list from LLAPI
        self.getLogic = GetLogic(self.dataFiles)

    def updateEmployee(self):
        """choose a employee (get a list and choose from the list). Get the info about the chosen 
        employee and then choose what info you want to change. 
        Then the user will be asked if he wants to save the changes. 
        Save the new information about the employee to the list about all employees """
        
        #Show list
        GetLogic(self.dataFiles).getAllCrew()
        #Choose Employee
        #Show employee info
        #Ask what the motherfucker wants to change for fucks sake
        #Change some shit or fuck off
        #Confirm whether the fucker is co ntent with the fucking changes
        #fuck the fuck off
 
        #Show employee info
        filePackage = IOAPI().opener(self.dataFiles["CREW_FILE"])
        #asks for the SSN of the employee
        ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")

        #Sets it to True so that the while runs at least once
        employee_in_file_bool = True
        employee_info_list = []
        #goes through all the lines in the employee info
        while employee_in_file_bool:
            for x in filePackage:
                #checks the SSN of the employee
                if x['ssn'] == ssn_of_employee_str:
                    employee_index = filePackage.index(x)
                    employee_info_dict = x
                    employee_info_list = [x]
            if employee_info_list != []:
                employee_in_file_bool = False
            else:
                print("Employee not found!")
                ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")

        
        DisplayScreen().printList(employee_info_list,"Chosen employee:",frame=True)

        #Creates a list of editing options
        options_list = [{"Edit choices:":"Role"}, {"Edit choices:":"Rank"},{"Edit choices:": "License"},{"Edit choices:": "Address"}, {"Edit choices:":"Phone"}, {"Edit choices:": "Email"}]
        #Prints the beforementioned list of options
        DisplayScreen().printOptions(options_list, header = "")
        #Asks user to choose what he wants to edit
        choice_str = InputHandler().multipleNumChoices(options_list, "Choose data to update: ")
        
        #Creates a list of airplane types
        airplane_data_list = IOAPI().opener(self.dataFiles["AIRCRAFT_TYPE_FILE"])
        airplaneType_list = []
        for a_line_dict in airplane_data_list:
            airplaneType_list.append(a_line_dict["planeTypeId"])

        #Changes the requested data
        if choice_str == "Address":
            employee_info_dict[choice_str.lower()] = InputHandler().address("Input address: ")
        elif choice_str == "Phone":
            employee_info_dict["phonenumber"] = InputHandler().phoneNumber("Input a 7-digit phone number: ")
        elif choice_str == "Email":
            employee_info_dict[choice_str.lower()] = InputHandler().email("Input e-mail address: ")
        elif choice_str == "Role":
            employee_info_dict["role"], employee_info_dict["rank"], employee_info_dict["licence"] = InputHandler().roleUpdate(airplaneType_list)
        elif choice_str == "Rank":
            employee_info_dict[choice_str.lower()] = InputHandler().rank(employee_info_dict["role"],"Choose rank: ")
        elif choice_str == "Licence":
            employee_info_dict[choice_str.lower()] = InputHandler().license(employee_info_dict["role"], airplaneType_list,"Input licence: ")

        #Prints the data and asks for confirmation
        DisplayScreen().printList([employee_info_dict], header = "")
        continue_bool = InputHandler().yesOrNoConfirmation("Do you want to change anything else? (y/n): ")
        while continue_bool:
            #Prints out editing options
            DisplayScreen().printOptions(options_list, header = "")
            #Asks to choose what the user wants to edit
            choice_str = InputHandler().multipleNumChoices(options_list, "Choose data to update: ")

            #Changes the requested data
            if choice_str == "Address":
                employee_info_dict[choice_str.lower()] = InputHandler().address("Input address: ")
            elif choice_str == "Phone":
                employee_info_dict["phonenumber"] = InputHandler().phoneNumber("Input a 7-digit phone number: ")
            elif choice_str == "Email":
                employee_info_dict[choice_str.lower()] = InputHandler().email("Input e-mail address: ")
            elif choice_str == "Role":
                employee_info_dict["role"], employee_info_dict["rank"], employee_info_dict["licence"] = InputHandler().roleUpdate(airplaneType_list)
            elif choice_str == "Rank":
                employee_info_dict[choice_str.lower()] = InputHandler().rank(employee_info_dict["role"],"Choose rank: ")
            elif choice_str == "Licence":
                employee_info_dict[choice_str.lower()] = InputHandler().license(employee_info_dict["role"], airplaneType_list,"Input licence: ")

            #Prints the results of editing and asks for confirmation
            DisplayScreen().printList([employee_info_dict], header = "")
            continue_bool = InputHandler().yesOrNoConfirmation("Do you want to change anything else? (y/n): ")
        else:
            if InputHandler().yesOrNoConfirmation("Do you want to save the changes? (y/n): "):
                #Updates the Crew file with the edited employee info
                filePackage[employee_index] = employee_info_dict
                IOAPI().updater(self.dataFiles["CREW_FILE"], filePackage)
                print("Data has been updated")
        
   
    def updateDestination(self):
        """The user chooses a destination (get a list of all the destinations and then choose the airport id fromt the list). Get the info
        about the chosen destination and then choose what info the user wnat to change.
        Then the user will be asked if he wants to save the changes.
        Save the new info about the destination to the list of all destinations. (if the user does not want to save then the old info about
        the destination will be kept in the list of all destinations)"""

        #get and show the user the list of all destinations
        GetLogic(self.dataFiles).getDestinations()
        #choose a destination the user wants to change
        #GetLogic(self.dataFiles).getOneDestination()

        #fetches destinations info
        filePackage = IOAPI().opener(self.dataFiles['DESTINATIONS_FILE'])

        #Creates a list of airports NaN Air flyes to 
        airport_list = []
        for a_line_dict in filePackage:
            airport_list.append(a_line_dict["id"])

        #asks for the ID of the destination
        id_of_destination_str = InputHandler().destinationID(airport_list, "Enter the ID of the airport you want to change: ")
        
        #Set id_in_file_bool to True so that the while runs at least once
        id_in_file_bool = True
        airport_info_list = []
        #goes through all the lines in the destination info
        while id_in_file_bool:
            for x in filePackage:
                #checks the ID of the destinations
                airport_index = filePackage.index(x)
                if x["id"] ==id_of_destination_str:
                    airport_info_dict = x
                    airport_info_list = [x]
            if airport_info_list != []:
                id_in_file_bool = False
            else:
                print("Airport not found!")
                id_of_destination_str = InputHandler().destinationID(airport_list, "Enter the ID of the airport you want to change: ")


        DisplayScreen().printList(airport_info_list, "Chosen airport: ", frame = True)

        #creates a list of editing optins
        options_list = [{"Edit choices:":"Contact Person"}, {"Edit choices:":"Emergency number"}]
        #Prints the before mentioned list of options
        DisplayScreen().printOptions(options_list, header = "")
        #Asks the user to choose what he/she wants to edit
        choice_str = InputHandler().multipleNumChoices(options_list, "Choose data you want to update: ")

        #Changes the requested data
        if choice_str == "Contact Person":
            airport_info_dict["contactPerson"] = InputHandler().fullName("Enter the name of the new contact person: ")
        
        elif choice_str == "Emergency number":
            airport_info_dict["emergencyPhone"] = InputHandler().phoneNumber("Input a 7 digit phone number for the new emergency phone number: ")
        

        #Prints the data and asks for confirmation
        DisplayScreen().printList([airport_info_dict], header = "")
        continue_bool = InputHandler().yesOrNoConfirmation("Do you want to change anything else? (y/n): ")
        
        while continue_bool:
            #Prints out editing options again
            DisplayScreen().printOptions(options_list, header = "")
            #Asks the user to choose what he/she wants to edit
            choice_str = InputHandler().multipleNumChoices(options_list, "Choose data you want to update: ")

            #Changes the requested data
            if choice_str == "Contact Person":
                airport_info_dict["contactPerson"] = InputHandler.fullName("Enter the name of the new contact person: ")
        
            elif choice_str == "Emergency number":
                airport_info_dict["emergencyPhone"] = InputHandler.phoneNumber("Input a 7 digit phone number for the new emergency phone number: ")
        
            #Prints the results of editing and asks for confirmation
            DisplayScreen().printList([airport_info_dict], header = "")
            continue_bool = InputHandler().yesOrNoConfirmation("Do you want to change anything else? (y/n): ")

        else:
            #Updates the Destination file with the edited destion info
            filePackage[airport_index] = airport_info_dict
            IOAPI().updater(self.dataFiles["DESTINATIONS_FILE"], filePackage)
            print("Data has been updated")

        
    def updateVoyage(self):
        """ Updates the crew on a voyage """
        departingFlights_data = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        allEmployees_data = IOAPI().opener(self.dataFiles["CREW_FILE"])

        def findVoyage(flightData:list):
            """Find the voyage"""
            #get the list 
            departingFlights_list = []
            for flight in departingFlights_data:
                if flight['departingFrom'] == 'KEF':
                    departingFlights_list.append(flight)
            
            #give user option to choose how the list is sorted:
            sortOptions = [
                {"sortBy": "departure"}, 
                {"sortBy": "arrivingAt"}, 
                {"sortBy": "flightNumber"}
            ]
            DisplayScreen().printOptions(sortOptions, header="Search for voyages from list")
            sortedChoice_int = int(InputHandler().numChoices(len(sortOptions), "How would you like the voyages to be sorted? :"))
            sortedBy_str = sortOptions[sortedChoice_int-1]["sortBy"]

            #sort the list by departure time
            sortedDepartures_list = sorted(departingFlights_list, key = lambda i: i[sortedBy_str])

            #print the upcoming voyages
            DisplayScreen().printOptions(sortedDepartures_list)
            # ask user to select a flight from the list representing the voyage
            selectedFlight_int = int(InputHandler().numChoices(len(sortedDepartures_list), "Select a voyage from the list: "))
            selectedFlight_dict = sortedDepartures_list[selectedFlight_int-1]
        
            # find the two connecting flights, by finding the index of selected flight
            flightIndex = departingFlights_data.index(selectedFlight_dict)
            return {"out":[flightIndex, departingFlights_data[flightIndex]], "in": [flightIndex+1, departingFlights_data[flightIndex+1]]}

 
        # Find the currently listed crew and roles (for printOptions)
        def selectRoleForUpdate(flightPair:list):
            currentVoyage = Voyage(flightPair)
            rolesForUpdate_list = []
            for role, employee in currentVoyage.addCrew().items():
                #find the employee info, should find name
                crewInRole = {"role": role, "employee": employee} 
                rolesForUpdate_list.append(crewInRole.copy())

                
            DisplayScreen().printOptions(rolesForUpdate_list, "Crew assigned to this voyage" )
            selectedRole = InputHandler().numChoices(len(rolesForUpdate_list), "Select a role to update: ")
            return rolesForUpdate_list[int(selectedRole)-1]["role"]

        #========================
        def assignCrew(availableCrew_list:list, selectedRole_str:str, flightPair:list ):
            """Finds the crew to """
            currentVoyage = Voyage(flightPair)
            currentCrew = currentVoyage.addCrew()
            #get the available employees for current voyage

            roleList = {
                "captain": {"rank": "Captain"} ,
                "copilot":{ "rank":"Copilot"},
                "fsm": {"rank":"Flight Service Manager"},
                "fa1": {"rank":"Flight Attendant"},
                "fa2": {"rank":"Flight Attendant"},
            }
            
            # filter out only of right rank
            rankOnlyList = []
            for employee in availableCrew_list:
                if employee["rank"] == roleList[selectedRole_str]["rank"]:
                    rankOnlyList.append(employee)

            #ask what employee they wish to assign to role
            if len(availableCrew_list) != 0:
                DisplayScreen().printOptions(rankOnlyList)
                inputChoice = InputHandler().numChoices(len(rankOnlyList), "Select an employee: ")
                selectedEmployee = rankOnlyList[int(inputChoice)-1]
                currentCrew[selectedRole_str] = selectedEmployee["ssn"]
            else:
                DisplayScreen().printText(["No available crew for this role during this voyage"], "Finding {} for voyage".format(roleList[selectedRole_str]["rank"]))
                return flightPair
            #update the voyage info
            currentVoyage.addCrew(currentCrew)
            #get the flights with updated info
            newFlights = currentVoyage.getFlights()
            return newFlights

        #========================
        #find the days that the crew would be occupied during voyage
        def findDaysDuration(departureFlight, arrivalFlight):
            """Finds the days that the voyage will cover"""
            departureDate = departureFlight["departure"]
            returnDate = arrivalFlight["arrival"]
            departureDate_obj = DateUtil(departureDate).createObject()
            returnDate_obj = departureDate_obj + datetime.timedelta(days =1)
            compiledDates_list = [departureDate, returnDate_obj.isoformat()]

            return compiledDates_list

        # Find available employees
        def findAvailableCrew(daysOfWoyage, employeeList):
            """Just loops through the given days to return available staff"""
            availableCrew = []
            availablePerDay = []
            availableForVoyage = []
            #make list of all employees availeble on these days
            for date in daysOfVoyage: 
                availablePerDay.append(self.getLogic.getAway(date, noPrint=True)) 


            #make a list of all employees that appear on these lists
            for day in availablePerDay:
                for employee in day:
                    if employee not in availableCrew:
                        availableCrew.append(employee)

            # #check if employee is available all days of voyage
            # for employee in availableCrew:
            #     freeForAll = []
            #     for day in availablePerDay:
            #         if employee in day:
            #             freeForAll.append(True)
            #         else: 
            #             freeForAll.append(False)
            #     if all(freeForAll) = True:
            #         availableForVoyage.append(employee)
                
            # check if they are free for the duration
            return availableCrew
            

        def updateFlights(allFlights, updatedFlights, voyageData):
            """Sends the updated list to the updater"""

            departingIndex = voyageData["out"][0]
            returningIndex = voyageData["in"][0]

            #update departing
            allFlights[departingIndex] = updatedFlights[0]
            allFlights[returningIndex] = updatedFlights[1]

            #update returning
            IOAPI().updater(self.dataFiles["UPCOMING_FLIGHTS_FILE"], allFlights)
        #voyage data, keeping index for later references
        voyageData = findVoyage(departingFlights_data)

        #get the flight data
        voyageFlightPair = [voyageData["out"][1], voyageData["in"][1]]

        # create instance of VoyageHandler using the two connected flights        
        daysOfVoyage = findDaysDuration(voyageFlightPair[0], voyageFlightPair[1])

        #find list of employees available for work
        availableCrew_list = findAvailableCrew(daysOfVoyage, allEmployees_data)

        #get the role to update
        selectedRole = selectRoleForUpdate(voyageFlightPair)

        #get the updated flights after assigning a role
        newFlights = assignCrew(availableCrew_list, selectedRole, voyageFlightPair)

        # then find the flights that were updated and replace them
        updateFlights(departingFlights_data, newFlights, voyageData)

