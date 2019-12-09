import datetime
import re
from modules.ui_layer.DateUtil import DateUtil

class InputHandler:
    def __init__(self):
        self.exitKey = "q"
        self.isoFormat = "%Y-%m-%dT%H:%M:%S%z"

    def __str__(self):
        return "Handles user input, returns the value to caller \nmethods: numChoices"
    #--------------------- - 
    # Handles numbered input, for selecting from listed options
    #---------------------- 
    def numChoices(self, numOfChoices: int, inputQuestion : str = "Pick a number: ", exitKey: str = "" ):
        """Function that handles getting number input from set range, 
        Returns the input choice-1 (so it can be used as list index if needed)\n
        Required: numer for how many choices are available \n
        optional: string that will be printed for the input \n
        optional: set a key used for exiting the loop, will return false\n
        """
        if len(exitKey) == 1:
            exitKey = self.exitKey
        try:
            inputChoice = input(inputQuestion)
            #loop for input while it is not a valid option from range
            while inputChoice != exitKey:
                while int(inputChoice)-1 not in range(numOfChoices):
                    inputChoice = input("Needs to be within range of 1-{} \n".format(numOfChoices) + inputQuestion)
                #return the choice that can be used for list index
                return inputChoice
            else: 
                return False

        except Exception:
            print("Input needs to be a number in range 1-{}".format(numOfChoices))
            #repeats the loop with previous parameters
            self.numChoices(numOfChoices,inputQuestion,exitKey)

    #---------------------- 
    # Input string of numbers of set length
    #---------------------- 
    
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


    #---------------------- 
    # Input full name (createEmployee)
    #---------------------- 
    def fullName(self):
        """Input has to only be alphabetical characters and has to have at least one space in str"""
        
        name_str = input("Input full name: ")

        #Validity checks
        # Checks whether or not the name  consists of only alphabetical characters
        while not name_str.replace(" ","").isalpha():    
            print("Please input alphabetical characters only")
            name_str = input("Input full name: ")

        #Checks whether or not user had input both the surname and lastname
        while " " not in name_str:  
            print("Please input both surname and lastname")
            name_str = input("Input full name: ")

        return name_str


    #---------------------- 
    # Input social security number
    #----------------------     
    def ssn(self, inputQuestion:str = ""):
        """Input for social security number (kennitala)"""  
        return self.numSetLength(10, inputQuestion)

    #---------------------- 
    # Input date and time
    #----------------------   
    def dateTime(self, questionDate:str = "Input a date (DD/MM/YYYY): ", questionTime:str ="Input time (HH:MM): "):
        """Input is date and time"""      
        date = self.dateOnly(questionDate)
        time = self.timeOnly(questionTime)
        if date and time:
            #create a datetime 
            year, month, day = map(int,DateUtil(date).date.split('-'))
            hour,minute,second = map(int,time.split(':'))
            newDate = datetime.datetime(year,month,day,hour,minute,second).isoformat()
            return str(newDate)
        else:
            #if either date or time returned false
            return False

    #---------------------- 
    # Input time
    #----------------------   
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

    #---------------------- 
    # Input date only (returns full dateTime format)
    #----------------------   
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


    def name(self, inputQuestion:str = "Input a name: "):
        """Input for names"""
        name = input(inputQuestion)
        return "Jóhann Arnars"
        # while all(letter.isalpha() or letter.isspace() for letter in name):
        #     print("not valid name (needs to be alphabet letter or space)")
        #     name = input(inputQuestion)
        # else:
        #     return name

    def flightId(self):
        """Input for flight ID, just checks if it's a valid format"""
        input("test input: ")
        return "NA1234"

#InputHandler().numSetLength(7)
#InputHandler().numChoices(4)
#InputHandler().textSetLength(5)