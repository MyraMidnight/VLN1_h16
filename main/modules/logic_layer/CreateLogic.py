from modules.models.Voyage import Voyage

class CreateLogic :
    """Create methods for logic layer"""

    def createDestination(self, ):
        """create destination"""
    
    
    def createEmployee(self, action = "", inputHandler = ""):
        """Takes in an action and output from inputHandler. 
        Assigns and holds onto the values given by input handler until all 
        information is fullfilled. Asks for confirmation. Turns the information
        into dict format and returns it #Should also write it into data"""
        #Still lacks the append to data function

        a_dict = {}

        if action == "name" and inputHandler != "":
            self.name = inputHandler
        elif action == "ssn" and inputHandler != "":
            self.ssn = inputHandler
        elif action == "role"  and inputHandler != "":
            self.role = inputHandler
        elif action == "rank" and inputHandler != "":
            self.rank = inputHandler
        elif action == "phonenumber" and inputHandler != "":
            self.phonenumber = inputHandler
        elif action == "license" and inputHandler != "":
            self.license = inputHandler
        elif action == "email" and inputHandler != "":
            self.email = inputHandler
        elif action == "address" and inputHandler != "":
            self.address = inputHandler
        elif action == "confirmation":
            a_dict[ssn] = self.ssn
            a_dict[name] = self.name
            a_dict[role] = self.role
            a_dict[rank] = self.rank
            a_dict[address] = self.address
            a_dict[phonenumber] = self.phonenumber
            a_dict[license] = self.license
            a_dict[email] = self.email

        # print(self.name + self.ssn + self.role + self.rank + self.address + self.phonenumber + self.license + self.email)

        return a_dict

    def createVoyage(self):
        return Voyage().createVoyage()
        
