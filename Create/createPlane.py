class Logic():
    pass
class Data():
    pass

class Create(Logic, Data):
    
    def createPlane(self):
        """Requests input for planeName, and  planeType. Adds the plane to the registry"""
        
        planeInsignia_str = input("Input plane insignia: ")

        planeTypeId_str = input("Input plane type ID: ")
        validPlaneId_list = ["NAFokkerF28", "NAFokkerF100", "NABAE146"]

        #Validity check for planeTypeId
        while planeTypeId_str not in validPlaneId_list:
            print("Please input valid plane type ID")
            planeTypeId_str = input("Input plane type ID: ")

        plane_str = (planeInsignia_str + "," + planeTypeId_str)

        return plane_str