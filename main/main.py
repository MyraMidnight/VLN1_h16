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
import os

print(os.name)
os.system('mode con: cols=300 lines=50')  # works on M$ Windows
os.system("printf '\e[8;50;300t'")        # works on MacOS
pause = input("Press any key to continue...")

def main():
  """The core program"""
  #print the main menu
  MenuHandler().displayMenu()

# ------------------------  Run program  --------------------- 
main()