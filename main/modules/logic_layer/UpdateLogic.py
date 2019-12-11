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