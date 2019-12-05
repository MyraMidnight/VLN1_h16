import sys, os
sys.path.append(os.path.abspath(os.path.join('..','VLN1_H16/main/modules/data_layer')))

from IOAPI import IOAPI

class GetLogic :
    """Get methods for logic layer"""

    def getSingleEmployee(self):
        filePackage = IOAPI().opener('Crew.csv')
        ssn_of_employee = input('SSN: ')
        for x in filePackage:
            if x['ssn'] == ssn_of_employee:
                print(x)
                break

GetLogic().getSingleEmployee()
print('test')