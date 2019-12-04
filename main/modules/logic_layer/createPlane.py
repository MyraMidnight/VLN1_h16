def createPlane():
    """Requests input for planeName, and  planeType."""
    
    planeInsignia_str = input("Input plane insignia: ")
    while len(planeInsignia_str) != 6 or planeInsignia_str[2] != "-" or not planeInsignia_str.replace("-","").isalpha() or not planeInsignia_str.replace("-","").isupper():
        print("Incorrect input")
        planeInsignia_str = input("Input plane insignia: ")

    planeTypeId_str = input("Input plane type ID: ")
    validPlaneId_list = ["NAFokkerF28", "NAFokkerF100", "NABAE146"]
    while planeTypeId_str not in validPlaneId_list:
        print("Incorrect input")
        planeTypeId_str = input("Input plane type ID: ")

    return planeInsignia_str, planeTypeId_str

