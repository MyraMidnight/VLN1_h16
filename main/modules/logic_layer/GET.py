import sys, os
sys.path.insert(1, '../') 
#sys.path.append(os.path.abspath(os.path.join('..','VLN1_H16/main/modules/data_layer')))
#if visual studio underlines the from with red then just ignore it, it works anyways for me at least
from data_layer.IOAPI import IOAPI
from logic_layer.MenuHandler import MenuHandler

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
                returnString_str = 'SSN:' + x['ssn'] + "\n" + "Name:" + x['name'] + "\n" + "Role:" + x['role'] + "\n" + "rank:" + x['rank']
                #if the employee is a pilot then they will have a licence but otherwise not
                if x['licence'] != "N/A":
                    returnString_str += "\n" + "licence:" + x["licence"]
                #add the rest of the info
                returnString_str += "\n" + "address:" + x["address"] + "\n" + "phonenumber:" + x["phonenumber"]
                print(returnString_str)
                print("-----------")
        MenuHandler().displayMenu("get")
    
    def getPilots(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        print("filepackage: ",filePackage)
        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Pilot":
                #contruct a string from the dict to return
                returnString_str = 'SSN:' + x['ssn'] + "\n" + "Name:" + x['name'] + "\n" + "Role:" + x['role'] + "\n" + "rank:" + x['rank'] + "\n" + "licence:" + x["licence"] + "\n" + "address:" + x["address"] + "\n" + "phonenumber:" + x["phonenumber"]
                print(returnString_str)
                print("---------")
        MenuHandler().displayMenu("get")
    
    def getFlightAttendants(self):
        #fetches employee info
        filePackage = IOAPI().opener('Crew.csv')
        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            if x['role'] == "Cabincrew":
                #contruct a string from the dict to return
                returnString_str = 'SSN:' + x['ssn'] + "\n" + "Name:" + x['name'] + "\n" + "Role:" + x['role'] + "\n" + "rank:" + x['rank'] + "\n" + "address:" + x["address"] + "\n" + "phonenumber:" + x["phonenumber"]
                print(returnString_str)
                print("---------")
        MenuHandler().displayMenu("get")
    
    def getAllCrew(self):
        GetLogic().getPilots()
        GetLogic().getFlightAttendants()
        MenuHandler().displayMenu("get")

    def getPlanes(self):
        #fetches aircraft info
        filePackage = IOAPI().opener('Aircraft.csv')
        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            returnString_str = 'planeInsignia:' + x['planeInsignia'] + "\n" + "planeTypeId:" + x["planeTypeId"]
            print(returnString_str)
            print("----------")
        MenuHandler().displayMenu("get")

    
    def getDestinations(self):
        #fetches destination info
        filePackage = IOAPI().opener('Destinations.csv')
        #goes through all the lines in the employee info
        for x in filePackage:
            #checks the SSN of the employee
            returnString_str = 'id:' + x['id'] + "\n" + "destination:" + x["destination"]
            print(returnString_str)
            print("----------")
        MenuHandler().displayMenu("get")
        