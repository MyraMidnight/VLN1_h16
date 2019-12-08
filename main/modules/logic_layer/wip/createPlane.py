class Logic():
    pass
class Data():
    pass

class Create(Logic, Data):
    
    def createPlane(self):
        """Requests input for planeName, and  planeType. Adds the plane to the registry"""
        
        planeInsignia_str = input("Input plane insignia: ")

        planeTypeId_str = input("Input plane type ID: ")

        plane_str = (planeInsignia_str + "," + planeTypeId_str)

        return plane_str