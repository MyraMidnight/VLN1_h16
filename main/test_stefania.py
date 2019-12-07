#from modules.ui_layer.DisplayScreen import DisplayScreen
#from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DateUtil import DateUtil

# ROLE_PILOT = "pilot"
# ROLE_CAPTAIN = "captain"
# ROLE_COPILOT = "coPilot"
# ROLE_ATTENDANT = "flightAttendant"
# ROLE_LEAD_ATTENDANT = "headFlightAttendant"
# MODEL_PLANE = "" #instance of plane
# MODEL_EMPLOYEE = "" #instance of employee

#ata = IOAPI().opener("Crew.csv")
# for line in data:
#   print(line)
#DisplayScreen().printListFormat(data,rowLimit=3)

date = InputHandler().dateOnly()

parsedDate = DateUtil()
parsedDate.parse(date)

print("day: ",parsedDate.day)
print("month: ",parsedDate.month)
print("year: ",parsedDate.year)
print("time: ",parsedDate.time)
print("hour: ",parsedDate.hour)
print("minute: ",parsedDate.minute)