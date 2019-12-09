from modules.data_layer.IOAPI import IOAPI     #need this to be able to fetch info
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.DateUtil import DateUtil

class GetLogic :
    """Get methods for logic layer"""

    def getSingleEmployee(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #asks for the SSN of the employee
        ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for:")
        if ssn_of_employee_str == False:
            return False
        
        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            if x['ssn'] == ssn_of_employee_str:
                list_to_print = [x]
                return DisplayScreen().printList(list_to_print,colWidth=20)
                
    
    def getPilots(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #goes through all the lines in the employee info
        list_to_print = []
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Pilot":
                list_to_print.append(x)
        return DisplayScreen().printList(list_to_print, colWidth = 15)
                
    
    def getFlightAttendants(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #goes through all the lines in the employee info
        list_to_print = []
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Cabincrew":
                list_to_print.append(x)
        return DisplayScreen().printList(list_to_print,colWidth=17)
                
    
    def getAllCrew(self):
        GetLogic().getPilots()
        GetLogic().getFlightAttendants()

    def getPlanes(self):
        #fetches aircraft info
        filePackage = IOAPI().opener('Aircraft.csv')
        return DisplayScreen().printList(filePackage,colWidth=17)

    def getDestinations(self):
        #fetches destination info
        filePackage = IOAPI().opener('Destinations.csv')
        return DisplayScreen().printList(filePackage,colWidth=17)
    
    def getVoyages(self):
        #fetch voyage info
        filePackage = IOAPI().opener('NewUpcomingFlights.csv')
        return DisplayScreen().printList(filePackage,colWidth=17)
    
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

        return DisplayScreen().printList(away_list,colWidth=17)
    
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
        
        return DisplayScreen().printList(working_list,colWidth=17)
    
    def getWeekWork(self):
        #fetch employee info
        employeePackage = IOAPI().opener('Crew.csv')
        #fetch Voyage info
        voyagePackage = IOAPI().opener('NewUpcomingFlights.csv')
        #ask for SSN
        user_ssn = InputHandler.ssn("Please input the SSN of the Employee you want a schedule of: ")
        #ask for datetime from user
        user_input = InputHandler().dateOnly()
        check_date = DateUtil(user_input)
        '''
        for x in range(7):
            for flight in voyagePackage:
                departure = DateUtil(line['departure']).date
                if check_date.date == departure:
                    if user_ssn == flight['captain'] or user_ssn == flight['copilot'] and user_ssn == flight['fsm'] and user_ssn ==
                    '''



        