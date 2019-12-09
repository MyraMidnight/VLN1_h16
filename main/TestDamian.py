# Here we will create the main program
# ------------------------  Import classes  ------------------ 
from modules.ui_layer.MenuHandler import MenuHandler
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