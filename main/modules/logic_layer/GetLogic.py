from modules.data_layer.IOAPI import IOAPI     #need this to be able to fetch info
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.DateUtil import DateUtil
import datetime

class GetLogic :
    """Get methods for logic layer"""

    def __init__(self, dataFiles):
        self.dataFiles = dataFiles #gets the file list from LLAPI

    def printData(self, data:list, header:str):
        if len(data) != 0 :
            DisplayScreen().printList(data, header)
        else:
            DisplayScreen().printText([""],header)
        return InputHandler().confirmation("Press enter to continue...")

    #===================================================================================
    # Get single employee
    #===================================================================================

    def getSingleEmployee(self):
        #fetches employee info
        filePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        #asks for the SSN of the employee
        ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")
        #Validity check for SSN
        while ssn_of_employee_str == False:
            print("Invalid input")
            ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")

        #Check for if the SSN is in crew file
        ssn_in_file_bool = True
        list_to_print = []
        while ssn_in_file_bool:
            #goes through all the lines in the employee info
            for x in filePackage:
                #checks the SSN of the employee
                if x['ssn'] == ssn_of_employee_str:
                    list_to_print = [x]
            if list_to_print != []:
                ssn_in_file_bool = False
            else:
                print("No employee found with this SSN")
                ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")



        return DisplayScreen().printList(list_to_print,"Chosen employee:")
                
    
    def getPilots(self, data:list = []):
        #fetches employee info
        if len(data) == 0:
            filePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        else:
            filePackage = data
        #goes through all the lines in the employee info
        list_to_print = []
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Pilot":
                list_to_print.append(x)
        self.printData(list_to_print,header="All pilots:")
        return list_to_print
    
    def getFlightAttendants(self, data:list = []):
        #fetches employee info
        if len(data) == 0:
            filePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        else:
            filePackage = data
        #goes through all the lines in the employee info
        list_to_print = []
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Cabincrew":
                list_to_print.append(x)
        self.printData(list_to_print,header="All Flight Attendants:")
        return list_to_print   
    
    def getAllCrew(self):
        #fetches employee info
        filePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        return self.printData(filePackage,header="All crew:")

    def getPlanes(self):
        #fetches aircraft info
        filePackage = IOAPI().opener(self.dataFiles['AIRCRAFT_FILE'])
        return self.printData(filePackage,header="Planes:")

    def getDestinations(self):
        #fetches destination info
        filePackage = IOAPI().opener(self.dataFiles['DESTINATIONS_FILE'])
        return self.printData(filePackage,header="Destinations:")
    
    def getVoyages(self):
        #fetch voyage info	        #fetch voyage info
        voyagePackage = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        #fetch plane info
        planePackage = IOAPI().opener(self.dataFiles["AIRCRAFT_FILE"])
        list_to_print = []
        for voyage in voyagePackage:
            planeId = voyage["aircraftID"]
            temp_dict = voyage
            for plane in planePackage:
                if plane["planeInsignia"] == planeId:
                    temp_dict["capacity"] = plane["capacity"]
            list_to_print.append(temp_dict)

        return self.printData(list_to_print,header="Voyages:")
    
    def getAway(self, date:str = "", noPrint:bool = False):
        #fetch employee info
        employeePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        #fetch Voyage info
        voyagePackage = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        
        #if no date is given in arguments, then ask for input
        if date == "":
            #ask for datetime from user
            user_input = InputHandler().dateOnly()
        else:
            user_input = date

        user_date = DateUtil(user_input).date
        ssn_list = []
        #goes through all flights, finds flights at the chosen date and compiles a unique list of SSN
        for line in voyagePackage:
            departure = DateUtil(line['departure']).date
            if user_date == departure:
                if line['captain'] != "" and line['captain'] not in ssn_list:
                    ssn_list.append(line['captain'])
                if line['copilot'] != "" and line['copilot'] not in ssn_list:
                    ssn_list.append(line['copilot'])
                if line['fsm'] != "" and line['fsm'] not in ssn_list:
                    ssn_list.append(line['fsm'])
                if line['fa1'] != "" and line['fa1'] not in ssn_list:
                    ssn_list.append(line['fa1'])
                if line['fa2'] != "" and line['fa2'] not in ssn_list:
                    ssn_list.append(line['fa2'])
        #everybody who isn't working is everyone who isn't in the ssn_list
        away_list = []
        for employee in employeePackage:
            if employee['ssn'] not in ssn_list:
                away_list.append(employee)
        
        if noPrint != True:
            self.printData(away_list,header="Employees not working:")
        return away_list
    
    def getWorking(self):
        #fetch employee info
        employeePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        #fetch Voyage info
        voyagePackage = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        #fetch destination info
        destinationPackage = IOAPI().opener(self.dataFiles['DESTINATIONS_FILE'])
        #ask for datetime from user
        user_input = InputHandler().dateOnly()
        user_date = DateUtil(user_input).date
        combo_list = []
        #goes through all flights, finds flights of the chosen date and compiles a list of tuples with the SSN and 3 letter arrival
        for line in voyagePackage:
            departure = DateUtil(line['departure']).date
            if user_date == departure:
                if line['captain'] != "" and line['captain'] not in combo_list:
                    combo_list.append((line['captain'],line["arrivingAt"]))
                if line['copilot'] != "" and line['copilot'] not in combo_list:
                    combo_list.append((line['copilot'],line["arrivingAt"]))
                if line['fsm'] != "" and line['fsm'] not in combo_list:
                    combo_list.append((line['fsm'],line["arrivingAt"]))
                if line['fa1'] != "" and line['fa1'] not in combo_list:
                    combo_list.append((line['fa1'],line["arrivingAt"]))
                if line['fa2'] != "" and line['fa2'] not in combo_list:
                    combo_list.append((line['fa2'],line["arrivingAt"]))
        if len(combo_list) == 0:
            self.printData([], "No employee is working on the specified day")
            return False
        working_list = []
        #finds the employees who were on the flights and finds the destination name based on the 3 letter arrival
        for employee in employeePackage:
            for x in combo_list:
                if x[0] == employee['ssn']:
                    #puts all the info together in one dict and adds to the list
                    temp_dict = employee
                    dest_dict = next((item for item in destinationPackage if item["id"] == x[1]),None)
                    if dest_dict:
                        temp_dict["destination"] = dest_dict["destination"]
                        working_list.append(temp_dict)
                    else:
                        break
        
        return self.printData(working_list,header="employees working and their destination:")
    
    def getWeekWork(self):
        #fetch employee info
        employeePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        #fetch Voyage info
        voyagePackage = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        #ask for SSN
        user_ssn = InputHandler().ssn("Please input the SSN of the Employee you want a schedule of: ")
        for employee in employeePackage:
            if user_ssn == employee['ssn']:
                ssn_exists = True
        
        if ssn_exists:
            pass
        else:
            print("An employee with that SSN does not exist")
            return False
        
        #ask for datetime from user
        refDate_str = InputHandler().dateOnly("Input starting date of week: ")
        refDate_obj = DateUtil(refDate_str).createObject()
        #collect the days of a week
        checkWeek_list = []
        checkWeek_list.append(refDate_str)
        #@ts-ignore
        for day in range(7):
            refDate_obj = refDate_obj + datetime.timedelta(days=1)
            checkWeek_list.append(refDate_obj.isoformat())
        schedule_list = []
        #find all the flights that are in the range of the week and check those flights for the employee ssn and add the flight to the schedule if so
        for flight in voyagePackage:
            departure = DateUtil(flight['departure']).date
            for date in checkWeek_list:
                if date[:10] == departure:
                    if user_ssn == flight['captain'] or user_ssn == flight['copilot'] or user_ssn == flight['fsm'] or user_ssn == flight['fa1'] or user_ssn == flight['fa2']:
                        schedule_list.append(flight)
        
        return self.printData(schedule_list,header="Chosen employee work schedule:")

    #===================================================================================
    # Get pilots by licence
    #===================================================================================

    def getPilotsByLicence(self):
        #fetch employee info
        employeePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        #get all the pilots in one list
        pilotPackage = []
        for employee in employeePackage:
            if employee['role'] == "Pilot":
                pilotPackage.append(employee)
        #show the planes to user
        #License
        #Gets a list of dictionaries containing aircraft type specifications
        airplane_data_list = IOAPI().opener(self.dataFiles["AIRCRAFT_TYPE_FILE"])
        #Creates a list of airplane types in the list
        airplaneType_list = []
        for a_line_dict in airplane_data_list:
            airplaneType_list.append(a_line_dict["planeTypeId"])

        user_input = InputHandler().license("Pilot", airplaneType_list,"Choose license: ")
        #set a flag to false here and then go through and try to find all pilots with the licence the user asked for
        #if no such pilots are found then the flag is never set to true
        anyone_found_flag = False
        licence_pilots = []
        for pilot in pilotPackage:
            if pilot['licence'] == user_input:
                anyone_found_flag = True
                licence_pilots.append(pilot)
        #if anyone is found it returns the relevant info
        if anyone_found_flag:
            return self.printData(licence_pilots,header="Pilots with chosen licence:")
        #else it alerts the user and returns false
        else:
            self.printData([],header="No pilots were found with that licence")
            return False

    def printPilotsByLicence(self):
        #fetch employee info
        employeePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        #get all the pilots in one list
        pilotPackage = []
        for employee in employeePackage:
            if employee['role'] == "Pilot":
                pilotPackage.append(employee)
        #fetch plane info
        planePackage = IOAPI().opener(self.dataFiles['AIRCRAFT_FILE'])
        #gets a list of unique plane types from the planePackage
        planetypeList = []
        for plane in planePackage:
            if plane['planeTypeId'] not in planetypeList:
                planetypeList.append(plane['planeTypeId'])
        planetypeList.sort()
        #goes through all the plane types and finds all the pilots with a licence for that plane type
        #and compiles them in a list
        pilotPlaneList = []
        for planeType in planetypeList:
            for pilot in pilotPackage:
                if pilot['licence'] == planeType and pilot not in pilotPlaneList:
                    pilotPlaneList.append(pilot)
        #returns relevant info
        return self.printData(pilotPlaneList,header="Pilots sorted by licence:")
    
    def licenceByCount(self):
        #fetch employee info
        employeePackage = IOAPI().opener(self.dataFiles['CREW_FILE'])
        #get all the pilots in one list
        pilotPackage = []
        for employee in employeePackage:
            if employee['role'] == "Pilot":
                pilotPackage.append(employee)
        #fetch plane info
        planePackage = IOAPI().opener(self.dataFiles['AIRCRAFT_FILE'])
        #gets a list of unique plane types from the planePackage
        planetypeList = []
        for plane in planePackage:
            if plane['planeTypeId'] not in planetypeList:
                planetypeList.append(plane['planeTypeId'])
        planetypeList.sort()
        #list comprehension to make a list of dicts with the planetype and the count as the dict
        licenceCountList = [{"planeTypeId":planetype, "count":0} for planetype in planetypeList]
        #count how many licences of each planetype the pilots have
        for combo in licenceCountList:
            for pilot in pilotPackage:
                if pilot['licence'] == combo["planeTypeId"]:
                    combo["count"] += 1
        #need to change it to string cause otherwise Displayscreen will Error
        for combo in licenceCountList:
            combo['count'] = str(combo['count'])

        return self.printData(licenceCountList,header="Licences by count:")

    def getWeekVoyages(self):
        #fetch Voyage info
        voyagePackage = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        #ask for datetime from user
        refDate_str = InputHandler().dateOnly("Input starting date of week: ")
        refDate_obj = DateUtil(refDate_str).createObject()
        #collect the days of a week
        checkWeek_list = []
        checkWeek_list.append(refDate_str)
        #@ts-ignore
        for day in range(7):
            refDate_obj = refDate_obj + datetime.timedelta(days=1)
            checkWeek_list.append(refDate_obj.isoformat())
        schedule_list = []
        #find all the flights that are in the range of the week
        for flight in voyagePackage:
            departure = DateUtil(flight['departure']).date
            for date in checkWeek_list:
                if date[:10] == departure:
                    schedule_list.append(flight)
        
        return self.printData(schedule_list,header="Voyages of chosen week:")
    
    def getDayVoyages(self):
        #fetch Voyage info
        voyagePackage = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        #ask for datetime from user
        user_input = InputHandler().dateOnly()
        user_date = DateUtil(user_input).date
        schedule_list = []
        #goes through all flights, finds flights of the chosen date and compiles a list of tuples with the SSN and 3 letter arrival
        for line in voyagePackage:
            departure = DateUtil(line['departure']).date
            if user_date == departure:
                schedule_list.append(line)
        
        return self.printData(schedule_list,header="Voyages of chosen day:")