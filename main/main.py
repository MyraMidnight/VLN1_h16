# Here we will create the main program
# ------------------------  Import classes  ------------------ 
from modules.ui_layer.MenuHandler import MenuHandler
# ------------------------  Global variables  ---------------- 
RANK_CAPTAIN = "Captain"
RANK_COPILOT = "Co-Pilot"
RANK_FSM = "Flight Service Manager"
RANK_FA = "Flight Attendant"
ROLE_PILOT = "Pilot"
ROLE_CC = "Cabin Crew"
MODEL_PLANE = "" #instance of plane
MODEL_EMPLOYEE = "" #instance of employee

# ------------------------  Main program  -------------------- 

def main():
  """The core program"""
  #print the main menu
  MenuHandler().displayMenu()

# ------------------------  Run program  --------------------- 
main()