RANK_CAPTAIN = "Captain"
RANK_COPILOT = "Co-Pilot"
RANK_FSM = "Flight Service Manager"
RANK_FA = "Flight Attendant"
ROLE_PILOT = "Pilot"
ROLE_CC = "Cabin Crew"

def createEmployee():

    #Takes in all the data inputs
    #Note there should be menus changing inbetween each input, but that is part of UI not logic layer

    #Validity checks
    #Checks whether or not user had input both the surname and lastname
    name_str = input("Input full name: ")

    while " " not in name_str:  
        print("Please input both surname and lastname")
        name_str = input("Input full name: ")

    # Checks whether or not the name  consists of only alphabetical characters
    while not name_str.replace(" ","").isalpha():    
        print("Please input correct surname and lastname")
        name_str = input("Input full name: ")

    ssn_str = input("Input SSN: ")
    #Validity check. Checks whether or not SSN has the right amount of numbers
    while len(ssn_str) != 10 or not ssn_str.isdigit():
        print("Please input correct SSN")
        ssn_str = input("Input SSN: ")

    address_str = input("Input address: ")
    while " "  not in address_str:
        print("Please input both the streetname and streenumber")
        address_str = input("Input address: ")

    # homePhone_str = input("Input home phone number: ")
    # while len(homePhone_str) != 7 or not homePhone_str.isdigit():
    #     print(Please input valid phonenumber)
    #     homePhone_str = input("Input home phone number: ")

    mobilePhone_str = input("Input mobile phone number: ")
    while len(mobilePhone_str) != 7 or not mobilePhone_str.isdigit():
        print("Please input valid phonenumber")
        homePhone_str = input("Input home phone number: ")

    email_str = input("Input e-mail address: ")
    while "@" not in email_str or "." not in email_str:
        print("Please input correct e-mail address")
        email_str = input("Input e-mail address: ")

    role_str = input("Choose role: ")   #Chooses between 1 : Pilot and 2 : Flight Attendant
    options = ["1","2"]
    while role_str not in options:
        print("Please input a valid action number")
        role_str = input("Choose role: ")

    if role_str == "1":
        role_str = ROLE_PILOT                              #Changes the role to a "Pilot" str
        license_str = input("Input license: ")
        
        rank_str = input("Choose rank: ")  #Selects rank for employee
        options = ["1","2"]
        while rank_str not in options:
            print("Please input a valid action number")
            rank_str = input("Choose rank: ")

        if rank_str == "1":     
            rank_str = RANK_CAPTAIN
        elif rank_str == "2":
            rank_str = RANK_COPILOT

    elif role_str == "2":   #Changes the role from a number to a "Cabin Crew" str
        role_str = ROLE_CC
        license_str = "N/A"

        rank_str = input()  #Selects rank for employee
        options = ["1","2"]
        while rank_str not in options:a
            print("Please input a valid action number")
            role_str = input("Choose role: ")
            
        if rank_str == "1":
            rank_str = RANK_FSM
        elif rank_str == "2":
            rank_str = RANK_FA

    a_dict[ssn] = ssn_str
    a_dict[name] = name_str
    a_dict[role] = role_str
    a_dict[rank] = rank_str
    a_dict[phonenumber] = mobilePhone_str
    a_dict[license] = license_str
    a_dict[email] = email_str

    return a_dict
