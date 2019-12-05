class InputHandler:
  #---------------------- Handles numbered input, for selecting from listed options
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
        inputChoice = input("Needs to be within range of 1-{}: ".format(numOfChoices))
      #return the choice that can be used for list index
      return int(inputChoice)-1

    except Exception:
      if inputChoice == exitKey:
        #user input was the key for exiting the loop
        return False
      else:
        print("Input needs to be a number in range 1-{}: ".format(numOfChoices))
        #repeats the loop with previous parameters
        self.numChoices(numOfChoices,inputQuestion,exitKey)