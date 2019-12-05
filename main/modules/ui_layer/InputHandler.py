

class InputHandler:
    def __init__(self):
        self.exitKey = "q"

    def __str__(self):
        return "Handles user input, returns the value to caller \nmethods: numChoices"
    #---------------------- 
    # Handles numbered input, for selecting from listed options
    #---------------------- 
    def numChoices(self, numOfChoices: int, inputQuestion : str = "Pick a number: ", exitKey: str = "q" ):
        """Function that handles getting number input from set range, 
        Returns the input choice-1 (so it can be used as list index if needed)\n
        Required: numer for how many choices are available \n
        optional: string that will be printed for the input \n
        optional: set a key used for exiting the loop, will return false\n
        """
        exitKey = exitKey
        try:
            inputChoice = input(inputQuestion)
            #loop for input while it is not a valid option from range
            while int(inputChoice)-1 not in range(numOfChoices):
                inputChoice = input("Needs to be within range of 1-{} \n".format(numOfChoices) + inputQuestion)
            #return the choice that can be used for list index
            return int(inputChoice)-1

        except Exception:
            if inputChoice == exitKey:
                #user input was the key for exiting the loop
                return False
            else:
                print("Input needs to be a number in range 1-{} \n".format(numOfChoices)+ inputQuestion)
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
    # Input social security number
    #----------------------     
    def ssn(self, type: str = "is"):
        """Input for social security number (kennitala), default type is 'is' for icelandic"""  
        return self.numSetLength(10)

    #---------------------- 
    # Input date and time
    #----------------------   
    def dateTime(self):
        """Input is date and time"""
        return "2019-12-21T09:21:00"

    #---------------------- 
    # Input date only (returns full dateTime format)
    #----------------------   
    def dateOnly(self):
        """Input is only date (without time)"""
        return "2019-12-21T09:21:00"

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


    def names(self):
        """Input for names"""

#InputHandler().numSetLength(7)
#InputHandler().numChoices(4)
#InputHandler().textSetLength(5)