#from modules.ui_layer.DisplayScreen import DisplayScreen
#from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.InputHandler import InputHandler

ROLE_PILOT = "pilot"
ROLE_CAPTAIN = "captain"
ROLE_COPILOT = "coPilot"
ROLE_ATTENDANT = "flightAttendant"
ROLE_LEAD_ATTENDANT = "headFlightAttendant"
MODEL_PLANE = "" #instance of plane
MODEL_EMPLOYEE = "" #instance of employee

#ata = IOAPI().opener("Crew.csv")
# for line in data:
#   print(line)
#DisplayScreen().printListFormat(data,rowLimit=3)

date = InputHandler().name()
print(date)