import sys
sys.path.insert(1, '../') #to be able to get to sibling directory

from data_layer.IOAPI import IOAPI

class GetLogic :
    """Get methods for logic layer"""

    def getSingleEmployee(self):
        filePackage = IOAPI().opener('Crew.csv')
        print(filePackage)

GetLogic().getSingleEmployee()