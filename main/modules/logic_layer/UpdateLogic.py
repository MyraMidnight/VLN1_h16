from modules.logic_layer.GetLogic import GetLogic
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.InputHandler import InputHandler

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

        #Show employee info
        filePackage = IOAPI().opener('Crew.csv')
        #asks for the SSN of the employee
        ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")
        if ssn_of_employee_str == False:
            return False

        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            employee_index = filePackage.find(x)
            if x['ssn'] == ssn_of_employee_str:
                employee_info_dict = x
                employee_info_list = [x]

        DisplayScreen().printList(employee_info_list,"Chosen employee:",frame=True)


        #Ask what the motherfucker wants to change for fucks sake
        options_list = [{"Edit choices:":"Role"}, {"Edit choices:":"Rank"},{"Edit choices:": "License"},{"Edit choices:": "Address"}, {"Edit choices:":"Phone number"}, {"Edit choices:": "E-mail"}]
        DisplayScreen().printOptions(options_list, header = "")
        choice_str = InputHandler().multipleNumChoices(options_list, "Enter the number of data you want to update: ")
        
        #Change some shit or fuck off


        editFunctionDict_list = {
                "Address":{ InputHandler().address("Input address: ")
                },
                "Phone number":{ InputHandler().phoneNumber("Input a 7-digit phone number:")
                },
                "E-mail":{ InputHandler().email("Input e-mail address: ")
                },
                "Role":{ InputHandler().role("Choose role: \n 1) "+ ROLE_PILOT +" \n 2) "+ ROLE_CC +" \n")
                },
                "Rank":{ InputHandler().rank(employee_info_dict["role"],"Choose rank: ")
                },
                "License":{ InputHandler().license(airplaneType_list,"Input license: ")
                }}
        #Rank
        self.rank = InputHandler().rank(employee_info_dict["role"], "Possible ranks: \n 1) "+ RANK_CAPTAIN +" \n 2) "+ RANK_COPILOT +" \n" + "Choose rank: ")

        self.rank = InputHandler().rank(employee_info_dict["role"], "Possible ranks: \n 1) " + RANK_FSM + " \n 2) "+ RANK_FA + " \n" + "Choose rank: ")




        #Confirm whether the fucker is co ntent with the fucking changes
        #fuck the fuck off
