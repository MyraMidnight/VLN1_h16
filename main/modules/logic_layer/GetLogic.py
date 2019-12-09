from modules.data_layer.IOAPI import IOAPI     #need this to be able to fetch info
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayScreen import DisplayScreen

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
        print(list_to_print)
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
    
    #def getAway(self):
        #fetch employee info
        #employeePackage = IOAPI().opener('Crew.csv')
