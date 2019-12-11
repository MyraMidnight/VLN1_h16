AIRCRAFT_TYPE_FILE = "AircraftType.csv"
CREW_FILE = "Crew.csv"

from modules.logic_layer.GetLogic import GetLogic
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.InputHandler import InputHandler
from modules.data_layer.IOAPI import IOAPI
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

        #Sets it to True so that the while runs at least once
        employee_in_file_bool = True
        employee_info_list = []
        #goes through all the lines in the employee info
        while employee_in_file_bool:
            for x in filePackage:
                #checks the SSN of the employee
                employee_index = filePackage.index(x)
                if x['ssn'] == ssn_of_employee_str:
                    employee_info_dict = x
                    employee_info_list = [x]
            if employee_info_list != []:
                employee_in_file_bool = False
            else:
                print("Employee not found!")
                ssn_of_employee_str = InputHandler().ssn("Enter the SSN of the employee you\'re looking for: ")

        

        DisplayScreen().printList(employee_info_list,"Chosen employee:",frame=True)

        #Creates a list of editing options
        options_list = [{"Edit choices:":"Role"}, {"Edit choices:":"Rank"},{"Edit choices:": "License"},{"Edit choices:": "Address"}, {"Edit choices:":"Phone number"}, {"Edit choices:": "Email"}]
        #Prints the beforementioned list of options
        DisplayScreen().printOptions(options_list, header = "")
        #Asks user to choose what he wants to edit
        choice_str = InputHandler().multipleNumChoices(options_list, "Choose data to update: ")
        
        #Creates a list of airplane types
        airplane_data_list = IOAPI().opener(AIRCRAFT_TYPE_FILE)
        airplaneType_list = []
        for a_line_dict in airplane_data_list:
            airplaneType_list.append(a_line_dict["planeTypeId"])

        #Changes the requested data
        if choice_str == "Address":
            employee_info_dict[choice_str.lower()] = InputHandler().address("Input address: ")
        elif choice_str == "Phone number":
            employee_info_dict[choice_str.lower()] = InputHandler().phoneNumber("Input a 7-digit phone number:")
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
            elif choice_str == "Phone number":
                employee_info_dict[choice_str.lower()] = InputHandler().phoneNumber("Input a 7-digit phone number:")
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
            #Updates the Crew file with the edited employee info
            filePackage[employee_index] = employee_info_dict
            IOAPI().updater(CREW_FILE, filePackage)
        
