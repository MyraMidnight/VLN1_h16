RANK_CAPTAIN = "Captain"
RANK_COPILOT = "Co-Pilot"
RANK_FSM = "Flight Service Manager"
RANK_FA = "Flight Attendant"
ROLE_PILOT = "Pilot"
ROLE_CC = "Cabin Crew"

import datetime
import re
from modules.ui_layer.DateUtil import DateUtil

class InputHandler:
    def __init__(self):
        self.exitKey = "q"

    def __str__(self):
        """Fancy print, gives some basic info about instance of InputHandler"""
        return "exitKey: {}".format(self.exitKey)
 
    #===================================================================================
    # Get index of chosen option (numChoices)
    #===================================================================================

    def numChoices(self, numOfChoices: int, inputQuestion : str = "Pick a number: " ):
        """Function that handles getting number input from set range, 
        Returns the input choice-1 (so it can be used as list index if needed)\n
        Required: numer for how many choices are available \n
        optional: string that will be printed for the input \n
        optional: set a key used for exiting the loop, will return false\n
        """

        while True:
            inputChoice = ""
            try:
                inputChoice = input(inputQuestion).strip()

                #check if input was exit key
                if inputChoice.lower() == self.exitKey:
                    return False
                    
                #check if number is in range
                if int(inputChoice) - 1  in range(numOfChoices):
                    return str(inputChoice)
                #return the choice that can be used for list index
                else:
                    raise ValueError

            except (ValueError, TypeError): 
                print("Input needs to be a number in range 1-{}".format(numOfChoices))
                pass

    def confirmation(self, inputQuestion:str = "Press enter to continue", acceptedInput:list = ["yes"]):
        """Just a confirmation"""
        return input(inputQuestion)

    #===================================================================================
    # Dates and Times!
    #===================================================================================
    
    # get date and time

    #---------------------- 
    # Input full name (createEmployee)
    #---------------------- 
    def fullName(self, inputQuestion : str = ""):
        """Input has to only be alphabetical characters and has to have at least one space in str"""
        
        name_str = input(inputQuestion)

        #Validity checks
        # Checks whether or not the name  consists of only alphabetical characters
        while not name_str.replace(" ","").isalpha():    
            print("Please input alphabetical characters only")
            name_str = input(inputQuestion)

        #Checks whether or not user had input both the surname and lastname
        while " " not in name_str:  
            print("Please input both surname and lastname")
            name_str = input(inputQuestion)

        return name_str

    #---------------------- 
    # Input social security number
    #----------------------     
    def ssn(self, inputQuestion:str = ""):
        """Input for social security number (kennitala)"""  
        return self.numSetLength(10, inputQuestion)


    #---------------------- 
    # Input address (createEmployee)
    #----------------------  

    def address(self, inputQuestion: str = ""):
        """Input for address"""
        address_str = input(inputQuestion)

        #Validity check, checks whether the address is in correct format
        while " "  not in address_str:
            print("Please input both the streetname and streetnumber")
            address_str = input(inputQuestion)
        
        #Separates the string into streetname and street number
        address_list = address_str.split()
        streetName_str = address_list[0]
        streetNumber_str = address_list[-1]

        while not streetName_str.isalpha() or not streetNumber_str.isdigit():
            print("Invalid input. Please input both the streetname and streetnumber")
            address_str = input(inputQuestion)
            while " "  not in address_str:
                print("Please input both the streetname and streenumber")
                address_str = input(inputQuestion)
            streetName_str = (address_str.split())[0]
            streetNumber_str = (address_str.split())[1]

        return address_str


    #---------------------- 
    # Input phone number (createEmployee)
    #----------------------  
    def phoneNumber(self, inputQuestion: str = ""):
        """Input for phone number. Returns a 7-digit phone number"""
        return self.numSetLength(7, inputQuestion)


    #---------------------- 
    # Input e-mail (createEmployee)
    #----------------------  
    def email(self, inputQuestion: str = ""):
        """Input for email"""

        email_str = input(inputQuestion)
        #Validity check, checks whether there is an "@" and "." and whether they are placed in correct order
        while "@" not in email_str or "." not in email_str or email_str.find("@") > email_str.find("."):
            print("Please input correct e-mail address")
            email_str = input(inputQuestion)
        
        return email_str


    #---------------------- 
    # Input role (createEmployee)
    #----------------------  
    def role(self, inputQuestion: str = ""):
        """Input for employee role"""
        #Asks for a single digit input to choose between roles
        role_str = self.numSetLength(1, inputQuestion)
        valid_options_list = ["1","2"] #These are valid inputs
        #Validity check for the input
        while role_str not in valid_options_list:
            print("Please choose a valid input")
            role_str = self.numSetLength(1, inputQuestion)
        
        #Changes the numbers into coresponding strings
        if role_str == "1":
            role_str = ROLE_PILOT
        else:
            role_str = ROLE_CC

        return role_str


    #---------------------- 
    # Input rank (createEmployee)
    #----------------------  
    def rank(self, role, inputQuestion: str = ""):
        """Input for employee rank"""
        #Calls for a single digit input
        rank_str = self.numSetLength(1, inputQuestion)
        valid_options_list = ["1","2"] #These are valid inputs
        #Validity checks the input
        while rank_str not in valid_options_list:
            print("Please choose a valid input")
            rank_str = self.numSetLength(1, inputQuestion)
        
        #Turns the input number into a string with rank name according to the role
        if role == ROLE_PILOT:  #Ranks for the Pilots
            if rank_str == "1":
                rank_str = RANK_CAPTAIN
            else:
                rank_str = RANK_COPILOT
            return rank_str
        else:   #Ranks for the Cabin Crew
            if rank_str == "1":
                rank_str = RANK_FSM
            else:
                rank_str = RANK_FA
        
        return rank_str


    #---------------------- 
    # Input license (createEmployee)
    #----------------------  
    def license(self, aircraftType_list: list, inputQustion: str = ""):
        """Input for pilots license. Returns a validated license"""
        print("Possible Plane types: \n", aircraftType_list)
        license_str = input(inputQustion)
        #Validity check, checks if there are plane types in pur system corresponding to the input license
        while license_str not in aircraftType_list:
            print("Invalid input")
            print("Possible Plane types: \n", aircraftType_list)
            license_str = input(inputQustion)

        return license_str


    #---------------------- 
    # Input confirmation (createEmployee)
    #----------------------  
    def yesOrNoConfirmation(self, inputQuestion: str = ""):
        """Returns True if user confirms the input question. 
        Returns False if user does not confirm the input question."""
        confirmation_str = input(inputQuestion)
        #Possible inputs
        valid_input_list = ["y", "Y","n", "N"]
        affirmative_list = ["y", "Y"]
        negative_list = ["n", "N"]
        #Validity check
        while confirmation_str not in valid_input_list:
            print("Invalid input")
            confirmation_str = input(inputQuestion)

        if confirmation_str in affirmative_list:
            return True
        elif confirmation_str in negative_list:
            return False


    #---------------------- 
    # Choose input to edit (createEmployee) (C-krafa)
    #----------------------   
    # def edit(self, inputQuestion: str = ""):
    #     choice_str = self.numSetLength(1, inputQuestion)
    #     while int(choice_str) not in range(1,9):
    #         print("Invalid input")
    #         choice_str = self.numSetLength(1, inputQuestion)
        
    #     return choice_str



    #---------------------- 
    # Get country name (create destination)
    #----------------------   

    def country(self, inputQuestion : str = "Input the new destination: "):
        """Input has to only be alphabetical characters"""
        country_str = input(inputQuestion)

        #Validity checks
        # Checks whether or not the country consists of only alphabetical characters
        while not country_str.replace(" ","").isalpha():    
            print("Please input alphabetical characters only.")
            country_str = input(inputQuestion)
        return country_str
    
    #---------------------- 
    # Get new airport  (create destination)
    #----------------------   


    def airport(self, airport_list: list, inputQustion: str = ""):
        """Input for new destination airport. Returns a validated airport"""
        #print("\nNaN Air already flyes to these airports: \n", airport_list)
        print("\nNaN Air already flies to these airports: ")
        for airport in airport_list:
            if airport != airport_list[-1]:
                print(airport, end = ", ")
            elif airport == airport_list[-1]:
                print(airport, end = "\n")
        airport_str = input(inputQustion)

        # Checks whether or not the airport consists of only alphabetical characters
        while not airport_str.isalpha() or len(airport_str) != 3:
            print("Please input 3 alphabetical characters only.")
            airport_str = input(inputQustion)


        #Validity check, checks if there are plane types in pur system corresponding to the input license
        while airport_str in airport_list:
            print("This is not a new destination. \n")
            print("NaN Air already flyes to these airports: \n", airport_list)
            airport_str = input(inputQustion)

        return airport_str.upper()


    def distance(self, inputQuestion : str = ""):
        """Input has to only be digits """
        
        distance_str = input(inputQuestion)

        while not distance_str.isdigit():
            print("Invalid input, try again. The input must be digits, the length of the distance in km.")
            distance_str = input(inputQuestion)
        
        #while km_str.lower() != "km" or km_str.lower() != "":
        #    print("Invalid input, try again. The input must be digits, the length of the distance in km.")
        #    distance_str = input(inputQuestion)
        
        return distance_str


    def planeInsignia(self, inputQuestion: str = ""):
        """Input and validity check for plane insignia"""
        insignia_str = input(inputQuestion)
        #Validity checks the input
        while insignia_str[2] != "-" or insignia_str[:2] != "TF" or len(insignia_str) != 6:
            print("Invalid input")
            insignia_str = input(inputQuestion)
        
        return insignia_str


    def strNoCheck(self, inputQuestion: str = ""):
        return input(inputQuestion)


    def digit(self, inputQuestion:str = ""):
        num_str = input(inputQuestion)
        while not num_str.isdigit():
            print("Invalid input")
            num_str = input(inputQuestion)
        
        return num_str


    #---------------------- 
    # Multiple Num Choice 
    #---------------------- 
        # def multipleNumChoices(self, choiceAmount : int, data: list, inputText : str = ""):




    #---------------------- 
    # Input date and time
    #----------------------   
    def dateTime(self, questionDate:str = "Input a date (DD/MM/YYYY): ", questionTime:str ="Input time (HH:MM): "):
        """Input is date and time"""      
        print("")
        date = self.dateOnly(questionDate)
        print("")
        time = self.timeOnly(questionTime)
        print("")
        if date and time:
            #create a datetime 
            year, month, day = map(int,DateUtil(date).date.split('-'))
            hour,minute,second = map(int,time.split(':'))
            newDate = datetime.datetime(year,month,day,hour,minute,second).isoformat()
            return str(newDate)
        else:
            #if either date or time returned false
            return False

    # Get only the time (timeOnly)
    def timeOnly(self, inputQuestion:str = "Input time (HH:MM): "):
        """Checks input for HH:MM time, returns string HH:MM:SS """
        try:
            time_str = input(inputQuestion)
            pattern ='\d{2}:\d{2}'
            #loop while the pattern is not a match
            while re.match(pattern, time_str) is None:
                print("Invalid input, try again")
                time_str = input(inputQuestion).strip()
            else:
                hour,minute = map(int,time_str.split(':'))
                #check if valid time
                time = datetime.time(hour=hour,minute=minute)
                return str(time)
        except ValueError:
            #if datetime.date() was not valid
            print("Not a valid time, try again")
            self.timeOnly()

    # Get only the date
    def dateOnly(self, inputQuestion:str = "Input a date (DD/MM/YYYY): "):
        """Checks input for date, DD/MM/YYYY, returns datetime object"""
        try:
            date_str = input(inputQuestion).strip()
            pattern = '\d{2}/\d{2}/\d{4}'
            #loop while the pattern is not a match
            while re.match(pattern, date_str) is None:
                print("Invalid input, try again")
                date_str = input(inputQuestion).strip()
            else:
                day,month,year = map(int,date_str.split('/'))
                #check if valid date
                date = datetime.datetime(day= day, month= month, year= year).isoformat()
                return str(date)
        except ValueError:
            #if datetime.date() was not valid
            print("Not a valid date, try again")
            self.dateOnly()
            
    #===================================================================================
    # Get strings of specific length and format
    #===================================================================================
 
    # any text of X length
    def textSetLength(self, numLength:int, inputQuestion:str = ""):
        """Input is only a text string of set length"""
        if len(inputQuestion) == 0:
            inputQuestion = "Input a string of {} length: ".format(str(numLength))
            
        input_string = input(inputQuestion)
        while len(input_string) != numLength:
            if input_string == self.exitKey:
                return False
            else:
                input_string = input("Invalid input\n" + inputQuestion)


    # only numbers of x length
    def numSetLength(self,numLength:int, inputQuestion: str = ""):
        """Input can only be numbers of a set length (numLength)"""
        if len(inputQuestion) == 0:
            inputQuestion = "Please insert {} numbers without spaces: ".format(str(numLength)) 
        num_string = input(inputQuestion)
        while len(num_string) != numLength or not num_string.isdigit():
            if num_string == self.exitKey:
                return False
            else: 
                num_string = input("Invalid input \n"+ inputQuestion)
        else:
            #once the input meets requirements
            return num_string

    #===================================================================================
    # Specific input (names, ssn, ID... )
    #===================================================================================
 
    # Name string, only allows alpha and spaces 
    def name(self, inputQuestion:str = "Input a name: "):
        """Input for names"""
        name = input(inputQuestion)
        name = "Jóhann Arnars"
        return name
        # while all(letter.isalpha() or letter.isspace() for letter in name):
        #     print("not valid name (needs to be alphabet letter or space)")
        #     name = input(inputQuestion)
        # else:
        #     return name

    def planetype(self, inputQuestion:str = "Input a type of plane: "):
        planetype = input(inputQuestion)
        while planetype[:2] != "NA":
            print("Please input a valid planetype")
            planetype = input(inputQuestion)
        return planetype
    
    # flightNumber format
    def flightId(self):
        """Input for flight ID, just checks if it's a valid format"""
        input("test input: ")
        return "NA1234"
