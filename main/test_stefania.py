from modules.ui_layer.DisplayScreen import DisplayScreen
# # from modules.ui_layer.InputHandler import InputHandler
# from modules.ui_layer.DateUtil import DateUtil
from modules.ui_layer.MenuHandler import MenuHandler

# from modules.models.Voyage import Voyage
from modules.data_layer.IOAPI import IOAPI
# from modules.logic_layer.CreateLogic import CreateLogic

#--------------- Testing voyage
flightData = IOAPI().opener("NewUpcomingFlights.csv")
import datetime
# from modules.models.Voyage import Voyage

# newVoyage = Voyage(flightData[:2])
# for flight in flightData[:2]:
#   print(flight)

# newCrew = {'captain': '3009907461', 'copilot': '3009907461', 'fsm': '3009907461', 'fa1': '3009907461', 'fa2': '3009907461'}

# print(newVoyage.getFlights())
# print(newVoyage.addCrew())
# print(newVoyage)
# print("_-------_ added new crew")
# print(newVoyage.addCrew(newCrew))
# print(newVoyage)
print(datetime.date(month=12, year=2050, day=6).strftime("%d/%m/%Y"))
