from modules.data_layer.IOAPI import IOAPI     #need this to be able to fetch info
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.DateUtil import DateUtil
import datetime

class GetLogic :
    """Get methods for logic layer"""

    def getSingleEmployee(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #asks for the SSN of the employee
        ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")
        if ssn_of_employee_str == False:
            return False
        
        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            if x['ssn'] == ssn_of_employee_str:
                list_to_print = [x]
                return DisplayScreen().printList(list_to_print,"Chosen employee:",frame=True)
                
    
    def getPilots(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #goes through all the lines in the employee info
        list_to_print = []
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Pilot":
                list_to_print.append(x)
        return DisplayScreen().printList(list_to_print)
                
    
    def getFlightAttendants(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #goes through all the lines in the employee info
        list_to_print = []
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Cabincrew":
                list_to_print.append(x)
<<<<<<< HEAD
        return DisplayScreen().printList(list_to_print,colWidth = 17)
=======
        return DisplayScreen().printList(list_to_print)
>>>>>>> FannarHrafn
                
    
    def getAllCrew(self):
        GetLogic().getPilots()
        GetLogic().getFlightAttendants()

    def getPlanes(self):
        #fetches aircraft info
        filePackage = IOAPI().opener('Aircraft.csv')
<<<<<<< HEAD
        return DisplayScreen().printList(filePackage,colWidth = 17)
=======
        return DisplayScreen().printList(filePackage)
>>>>>>> FannarHrafn

    def getDestinations(self):
        #fetches destination info
        filePackage = IOAPI().opener('Destinations.csv')
<<<<<<< HEAD
        return DisplayScreen().printList(filePackage,colWidth = 17)
=======
        return DisplayScreen().printList(filePackage)
>>>>>>> FannarHrafn
    
    def getVoyages(self):
        #fetch voyage info
        filePackage = IOAPI().opener('NewUpcomingFlights.csv')
<<<<<<< HEAD
        return DisplayScreen().printList(filePackage,colWidth = 17)
=======
        return DisplayScreen().printList(filePackage)
>>>>>>> FannarHrafn
    
    def getAway(self):
        #fetch employee info
        employeePackage = IOAPI().opener('Crew.csv')
        #fetch Voyage info
        voyagePackage = IOAPI().opener('NewUpcomingFlights.csv')
        #ask for datetime from user
        user_input = InputHandler().dateOnly()
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

<<<<<<< HEAD
        return DisplayScreen().printList(away_list,colWidth = 17)
=======
        return DisplayScreen().printList(away_list)
>>>>>>> FannarHrafn
    
    def getWorking(self):
        #fetch employee info
        employeePackage = IOAPI().opener('Crew.csv')
        #fetch Voyage info
        voyagePackage = IOAPI().opener('NewUpcomingFlights.csv')
        #fetch destination info
        destinationPackage = IOAPI().opener('Destinations.csv')
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
            print("No employee is working on the specified day")
            return False
        working_list = []
        #finds the employees who were on the flights and finds the destination name based on the 3 letter arrival
        for employee in employeePackage:
            for x in combo_list:
                if x[0] == employee['ssn']:
                    #puts all the info together in one dict and adds to the list
                    temp_dict = employee
                    dest_dict = next(item for item in destinationPackage if item["id"] == x[1])
                    temp_dict["destination"] = dest_dict["destination"]
                    working_list.append(temp_dict)
        
        return DisplayScreen().printList(working_list)
    
    def getWeekWork(self):
        #fetch employee info
        employeePackage = IOAPI().opener('Crew.csv')
        #fetch Voyage info
        voyagePackage = IOAPI().opener('NewUpcomingFlights.csv')
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
        refDate_str = InputHandler().dateOnly()
        refDate_obj = DateUtil(refDate_str).createObject()
        #collect the days of a week
        checkWeek_list = []
        checkWeek_list.append(refDate_str)
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
        
        return DisplayScreen().printList(schedule_list)

    def getPilotsByLicence(self):
        #fetch employee info
        employeePackage = IOAPI().opener('Crew.csv')
        #fetch plane info
        planePackage = IOAPI().opener('Aircraft.csv')
        #get all the pilots in one list
        pilotPackage = []
        for employee in employeePackage:
            if employee['role'] == "Pilot":
                pilotPackage.append(employee)
        #show the planes to user
        DisplayScreen().printList(planePackage)
        #ask user for a plane type
        user_input = InputHandler().planetype()
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
            return DisplayScreen().printList(licence_pilots)
        #else it alerts the user and returns false
        else:
            print("No pilots were found with that licence")
            return False

    def printPilotsByLicence(self):
        #fetch employee info
        employeePackage = IOAPI().opener('Crew.csv')
        #get all the pilots in one list
        pilotPackage = []
        for employee in employeePackage:
            if employee['role'] == "Pilot":
                pilotPackage.append(employee)
        #fetch plane info
        planePackage = IOAPI().opener('Aircraft.csv')
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
        return DisplayScreen().printList(pilotPlaneList)
    
    def licenceByCount(self):
        #fetch employee info
        employeePackage = IOAPI().opener('Crew.csv')
        #get all the pilots in one list
        pilotPackage = []
        for employee in employeePackage:
            if employee['role'] == "Pilot":
                pilotPackage.append(employee)
        #fetch plane info
        planePackage = IOAPI().opener('Aircraft.csv')
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

        return DisplayScreen().printList(licenceCountList)