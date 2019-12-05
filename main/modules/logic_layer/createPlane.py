def createPlane(self,AircraftType, AircraftInsignia):
    """Requests input for planeName, and  planeType. Returns the inputs as str"""
    
    #Gets user input and runs a validity check for it
    planeInsignia_str = input("Input plane insignia: ")
    while len(planeInsignia_str) != 6 or planeInsignia_str[2] != "-" or not planeInsignia_str.replace("-","").isalpha() or not planeInsignia_str.replace("-","").isupper() or planeInsignia_str not in AircraftInsignia:
        print("Incorrect input")
        planeInsignia_str = input("Input plane insignia: ")

    #Gets user input and runs a validity check for it by che
    planeTypeId_str = input("Input plane type ID: ")
    validPlaneId_list = AircraftType
    while planeTypeId_str not in validPlaneId_list:
        print("Incorrect input")
        planeTypeId_str = input("Input plane type ID: ")

    a_dict[insignia] = planeInsignia_str
    a_dict[planeTypeId] = planeTypeId_str

    return a_dict

