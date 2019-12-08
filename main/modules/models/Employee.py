from modules.ui_layer.InputHandler import InputHandler

class Employee:
    def __init__(self):
        self.__employeeInfo = {
            "name" : None,
            "ssn" : None,
            "address" : None,
            "phonenumber" : None,
            "email": None,
            "role": None,
            "rank": None,
        }

    def setInfo(self):
        """Compiles the base info:  name, socialId, address, phoneNumber, email"""
        self.__employeeInfo["name"] = InputHandler().name(inputQuestion="Input full name: ")
        
        self.__employeeInfo["ssn"] = InputHandler().ssn("Input SSN: ")
        
        self.__employeeInfo["address"] = InputHandler().address("Input address: ")

        self.__employeeInfo["phonenumber"] = InputHandler().phoneNumber("Input phone number: ")

        self.__employeeInfo["email"] = InputHandler().email("Input e-mail address: ")

        self.__employeeInfo["role"] = self.setRole()

        self.__employeeInfo["rank"] = self.setRank()

    def setRole(self):
        """Handles assigning role"""

        
        while role_str is not "1" or role_str is not "2":
            print("Please input a valid action number")
            role_str = input("Choose role: ")

        if role_str == "1":
            role_str = "Pilot"                               #Changes the role to a "Pilot" str
            license_str = input("Input license: ")
            
            rank_str = input()  #Selects rank for employee
            while rank_str is not "1" or rank_str is not "2":
                print("Please input a valid action number")
                role_str = input("Choose role: ")

            if rank_str == "1":     
                rank_str = "Captain"
            elif rank_str == "2":
                rank_str = "Co-Pilot"

    def setRank(self):
        """Handles assigning rank"""
        # rank requires the role to be set
        elif role_str == "2":   #Changes the role from a number to a "Cabin Crew" str
            role_str = "Cabin Crew"
            license = "N/A"

            rank_str = input()  #Selects rank for employee
            while rank_str is not "1" or rank_str is not "2":
                print("Please input a valid action number")
                role_str = input("Choose role: ")
                
            if rank_str == "1":
                rank_str = "Flight Service Manager"
            elif rank_str == "2":
                rank_str = "Flight Attendant"

    def getData(self):
        """Returns the employeeInfo dictionary"""


#----------------- original code from Halla -----------------------------------------------
    # def setInfo(self):
        # #Takes in all the data inputs
        # #Note there should be menus changing inbetween each input, but that is part of UI not logic layer
        # name_str = input("Input full name: ")

        # #Validity checks
        # #Checks whether or not user had input both the surname and lastname
        # while " " not in name_str:  
        #     print("Please input both surname and lastname")
        #     name_str = input("Input full name: ")

        # # Checks whether or not the name  consists of only alphabetical characters
        # while not name_str.isalpha():    
        #     print("Please input correct surname and lastname")
        #     name_str = input("Input full name: ")

        # ssn_str = input("Input SSN: ")
        # #Validity check. Checks whether or not SSN has the right amount of numbers
        # while len(ssn_str) != 10 or not ssn_str.isdigit():
        #     print(Please input correct SSN)
        #     ssn_str = input("Input SSN: ")

        # address_str = input("Input address: ")
        # while " "  not in address_str:
        #     print("Please input both the streetname and streenumber")
        #     address_str = input("Input address: ")

        # homePhone_str = input("Input home phone number: ")
        # while len(homePhone_str) != 7 or not homePhone_str.isdigit():
        #     print(Please input valid phonenumber)
        #     homePhone_str = input("Input home phone number: ")

        # mobilePhone_str = input("Input mobile phone number: ")
        # while len(mobilePhone_str) != 7 or not mobilePhone_str.isdigit():
        #     print(Please input valid phonenumber)
        #     homePhone_str = input("Input home phone number: ")

        # email_str = input("Input e-mail address: ")
        # while "@" not in email_str or "." not in email_str:
        #     print("Please input correct e-mail address")
        #     email_str = input("Input e-mail address: ")

        # role_str = input("Choose role: ")   #Chooses between 1 : Pilot and 2 : Flight Attendant
        # while role_str is not "1" or role_str is not "2":
        #     print("Please input a valid action number")
        #     role_str = input("Choose role: ")

        # if role_str == "1":
        #     role_str = "Pilot"                               #Changes the role to a "Pilot" str
        #     license_str = input("Input license: ")
            
        #     rank_str = input()  #Selects rank for employee
        #     while rank_str is not "1" or rank_str is not "2":
        #         print("Please input a valid action number")
        #         role_str = input("Choose role: ")

        #     if rank_str == "1":     
        #         rank_str = "Captain"
        #     elif rank_str == "2":
        #         rank_str = "Co-Pilot"

        # elif role_str == "2":   #Changes the role from a number to a "Cabin Crew" str
        #     role_str = "Cabin Crew"
        #     license = "N/A"

        #     rank_str = input()  #Selects rank for employee
        #     while rank_str is not "1" or rank_str is not "2":
        #         print("Please input a valid action number")
        #         role_str = input("Choose role: ")
                
        #     if rank_str == "1":
        #         rank_str = "Flight Service Manager"
        #     elif rank_str == "2":
        #         rank_str = "Flight Attendant"

        # #Puts all the info in proper order into a single string
        # employee_str = (ssn_str + "," + name_str + "," + role_str + "," + rank_str + "," + license_str + "," + address_str + "," + homePhone_str + "," + mobilePhone_str + "," + email_str)

        # return employee_str

