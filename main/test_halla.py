# Here we will create the main program
# ------------------------  Import classes  ------------------ 
from modules.ui_layer.MenuHandler import MenuHandler

from modules.ui_layer.InputHandler import InputHandler


from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.data_layer.IOAPI import IOAPI

# ------------------------  Global variables  ---------------- 
ROLE_PILOT = "pilot"
ROLE_CAPTAIN = "captain"
ROLE_COPILOT = "coPilot"
ROLE_ATTENDANT = "flightAttendant"
ROLE_LEAD_ATTENDANT = "headFlightAttendant"
MODEL_PLANE = "" #instance of plane
MODEL_EMPLOYEE = "" #instance of employee

# ------------------------  Main program  -------------------- 

def main():
  """The core program"""
  #print the main menu
  MenuHandler().displayMenu()

# ------------------------  Run program  --------------------- 
main()

#data = IOAPI().opener("NewPastFlights.csv")
#print("Þetta er datað", data)

#DisplayScreen().printListFormat(data, 5, 10)
#DisplayScreen().printList(data, 6, 12)

#date = InputHandler().dateTime()
#print(date)