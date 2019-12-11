from modules.logic_layer.GetLogic import GetLogic

class UpdateLogic :
    """Update methods for logic layer"""
    def updateEmployee(self):
        """choose a employee (get a list and choose from the list). Get the info about the chosen 
        employee and then choose what info you want to change. 
        Then the user will be asked if he wants to save the changes. 
        Save the new information about the employee to the list about all employees """
        
        #Show list
        GetLogic().getAllCrew()
        #Choose Employee
        GetLogic().getSingleEmployee()
        #Show employee info
        #Ask what the motherfucker wants to change for fucks sake
        #Change some shit or fuck off
        #Confirm whether the fucker is co ntent with the fucking changes
        #fuck the fuck off
    
    def updateDestination(self):
        """The user chooses a destination (get a list of all the destinations and then choose the airport id fromt the list). Get the info
        about the chosen destination and then choose what info the user wnat to change.
        Then the user will be asked if he wants to save the changes.
        Save the new info about the destination to the list of all destinations. (if the user does not want to save then the old info about
        the destination will be kept in the list of all destinations)"""

        #get and show the user the list of all destinations
        GetLogic().getDestinations()

        #GetLogic().