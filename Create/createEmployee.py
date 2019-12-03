class Logic():

class Data():

class Create(Logic, Data):

    def createEmployee(self):
        #Takes in all the data inputs
        #Note there should be menus changing inbetween each input, but that is part of UI not logic layer
        name_str = input("Input full name: ")
        ssn_str = input("Input SSN: ")
        address_str = input("Input address: ")
        homePhone_str = input("Input home phone number: ")
        mobilePhone_str = input("Input mobile phone number: ")
        email_str = input("Input e-mail address: ")
        role_str = input("Choose role: ")   #Chooses between 1 : Pilot and 2 : Flight Attendant

        if role_str == "1":
            role_str = "Pilot"                               #Changes the role to a "Pilot" str
            license_str = input("Input license: ")
            
            rank_str = input()  #Selects rank for employee
            if rank_str == "1":     
                rank_str = "Captain"
            elif rank_str == "2":
                rank_str = "Co-Pilot"

        elif role_str == "2":   #Changes the role from a number to a "Cabin Crew" str
            role_str = "Cabin Crew"
            license = "N/A"

            rank_str = input()  #Selects rank for employee
            if rank_str == "1":
                rank_str = "Flight Service Manager"
            elif rank_str == "2":
                rank_str = "Flight Attendant"

        #Puts all the info in proper order into a single string
        employee_str = (ssn_str + "," + name_str + "," + role_str + "," + rank_str + "," + license_str + "," + address_str + "," + homePhone_str + "," + mobilePhone_str + "," + email_str)

        return employee_str

