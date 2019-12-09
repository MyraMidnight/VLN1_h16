from modules.models.Voyage import Voyage
from modules.ui_layer.InputHandler import InputHandler

class CreateLogic :
    """Create methods for logic layer"""

    def createDestination(self, ):
        """create destination"""
    
    
    def createEmployee(self):
        """Assigns and holds onto the values given by input handler until all 
        information is fullfilled. Asks for confirmation. Turns the information
        into dict format and returns it #Should also write it into data"""
        
        employee_dict = {}

        self.name = inputHandler().fullName()
        # self.ssn =  
        # self.role = 
        # self.rank =
        # self.address = 
        # self.phonenumber = 
        # self.license = 
        # self.email = 

        #     a_dict[ssn] = self.ssn
        #     a_dict[name] = self.name
        #     a_dict[role] = self.role
        #     a_dict[rank] = self.rank
        #     a_dict[address] = self.address
        #     a_dict[phonenumber] = self.phonenumber
        #     a_dict[license] = self.license
        #     a_dict[email] = self.email

        # # print(self.name + self.ssn + self.role + self.rank + self.address + self.phonenumber + self.license + self.email)

        # return a_dict

    def createVoyage(self):
        return Voyage().createVoyage()
        
