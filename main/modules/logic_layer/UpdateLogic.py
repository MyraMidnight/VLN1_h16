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

        #GetLogic().

        
    def updateVoyage(self):
        """ Updates the crew on a voyage """

        departingFlights_data = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        allEmployees_data = IOAPI().opener(self.dataFiles["CREW_FILE"])
        currentCrew_dict = {}

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
        sortedDepartures_list = sorted(departingFlights_list, key=itemgetter(sortedBy_str), reverse=True)

        #print the upcoming voyages
        DisplayScreen().printOptions(sortedDepartures_list)
        # ask user to select a flight from the list representing the voyage
        selectedFlight_int = int(InputHandler().numChoices(len(departingFlights_list), "Select a voyage from the list: "))
        selectedFlight_dict = sortedDepartures_list[selectedFlight_int-1]
    
        # find the two connecting flights, by finding the index of selected flight
        flightIndex = departingFlights_list.index(selectedFlight_dict)
        voyageFlightPair = [departingFlights_data[flightIndex], departingFlights_data[flightIndex+1]]

        # create instance of VoyageHandler using the two connected flights
        currentVoyage_obj = Voyage(voyageFlightPair)
        currentCrew_dict = currentVoyage_obj.addCrew({})
        
        #========================
        #find the days that the crew would be occupied during voyage
        def findDaysDuration(departureFlight, arrivalFlight):
            """Finds the days that the voyage will cover"""
            departureDate = departureFlight["departure"]
            returnDate = arrivalFlight["arrival"]
            departureDate_obj = DateUtil(departureDate).createObject()
            returnDate_obj = departureDate_obj + datetime.timedelta(days =1)
            compiledDates_list = [departureDate, returnDate_obj.isoformat()]

            # #while the date is not the same
            # #while dateObject.isoformat()[:10] != returnDate[:10]:
            # print("Departure: ", DateUtil(dateObject.isoformat()).date)
            # print("Return: ",DateUtil(returnDate).date)
            # while DateUtil(dateObject.isoformat()).date != DateUtil(returnDate).date:
            #     dateObject =   dateObject + datetime.timedelta(days=1)
            #     compiledDates_list.append(dateObject.isoformat())
            # # create a range of days
            return compiledDates_list

        daysOfVoyage = findDaysDuration(voyageFlightPair[0], voyageFlightPair[1])
        print(daysOfVoyage)

        # Find available employees
        def findAvailableCrew(daysOfWoyage, employeeList):
            """Just loops through the given days to return available staff"""
            availableCrew = []
            # find all the people not working those days
            # check if they are free for the duration
            return availableCrew

        availableCrew_list = findAvailableCrew(daysOfVoyage, allEmployees_data)

        # Find the currently listed crew and roles (for printOptions)
        def currentCrew(employeeList):
            rolesForUpdate_list = []
            for role, employee in currentCrew_dict.items():
                #find the employee info, should find name
                crewInRole = {"role": role, "employee": employee} 
                rolesForUpdate_list.append(crewInRole.copy())
            return rolesForUpdate_list

        rolesForUpdate_list = currentCrew(allEmployees_data)
        # loop through selecting a role to change
        
        # print list of employees available for this voyage for this role
        # loop through asking if they want to update staff

        #========================
        def selectCrewRole(options):
            DisplayScreen().printOptions(options, "Crew assigned to this voyage" )
            selectedRole = InputHandler().numChoices(len(options), "Select a role to update: ")
            return options[int(selectedRole)-1]["role"]

        #========================
        def assignCrew(availableCrew_list):
            """Finds the crew to """
            
            while True:
                try: 
                    selectedRole_str = selectCrewRole(rolesForUpdate_list)

                    roleList = {
                        "captain": self.getLogic.getPilots,
                        "copilot": self.getLogic.getPilots,
                        "fms": self.getLogic.getFlightAttendants,
                        "fa1": self.getLogic.getFlightAttendants,
                        "fa2": self.getLogic.getFlightAttendants,
                    }

                    filteredCrew = roleList[selectedRole_str](availableCrew_list)
                    # filter out only of right rank
                    
                    DisplayScreen().printOptions(filteredCrew)
                    InputHandler().numChoices(len(filteredCrew), "Select an employee")
                except Exception:
                    continue
                #end the loop
                break

        assignCrew(availableCrew_list)
        
        # pressing q will ask for confirmation of saving the data
        # then find the flights that were updated and replace them
        # send the changed list of flights to updater
