import sys, os
sys.path.append(os.path.abspath(os.path.join('..','VLN1_H16/main/modules/data_layer')))
#if visual studio underlines the from with red then just ignore it, it works anyways for me at least
from IOAPI import IOAPI

class GetLogic :
    """Get methods for logic layer"""

    def getSingleEmployee(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #asks for the SSN of the employee
        ssn_of_employee_str = input('Enter the SSN of the employee you\'re looking for: ')
        #if the input contains any letters or if the input is not exactly 10 digits long then it asks again and again
        #until the user inputs a valid SSN
        while ssn_of_employee_str.isdigit() == False or len(ssn_of_employee_str) != 10:    
            print("Please input a valid SSN")
            ssn_of_employee_str = input("Enter the SSN of the employee you\'re looking for: ")
        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            if x['ssn'] == ssn_of_employee_str:
                #contruct a string from the dict to return
                returnString_str = 'SSN:' + str(x['ssn']) + "\n" + "Name:" + str(x['name']) + "\n" + "Role:" + str(x['role']) + "\n" + "rank:" + str(x['name'])
                #if the employee is a pilot then they will have a licence but otherwise not
                if x['licence'] != "N/A":
                    returnString_str += "\n" + "licence:" + str(x["licence"])
                #add the rest of the info
                returnString_str += "\n" + "address:" + str(x["address"]) + "\n" + "phonenumber:" + str(x["phonenumber"])
                return returnString_str

print(GetLogic().getSingleEmployee())