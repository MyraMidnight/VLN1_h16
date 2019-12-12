from modules.ui_layer.DisplayScreen import DisplayScreen
# # from modules.ui_layer.InputHandler import InputHandler
# from modules.ui_layer.DateUtil import DateUtil
from modules.ui_layer.MenuHandler import MenuHandler

# from modules.models.Voyage import Voyage
from modules.data_layer.IOAPI import IOAPI
# from modules.logic_layer.CreateLogic import CreateLogic

#--------------- Testing voyage
flightData = IOAPI().opener("NewUpcomingFlights.csv")

from modules.models.Voyage import Voyage

newVoyage = Voyage(flightData[:2])
for flight in flightData[:2]:
  print(flight)

print(newVoyage)
print(newVoyage.getFlights())