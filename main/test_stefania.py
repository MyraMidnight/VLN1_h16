from modules.ui_layer.DisplayScreen import DisplayScreen
#from modules.data_layer.IOAPI import IOAPI
# from modules.ui_layer.InputHandler import InputHandler
# from modules.ui_layer.DateUtil import DateUtil
# from modules.ui_layer.MenuHandler import MenuHandler

from modules.models.Voyage import Voyage
from modules.data_layer.IOAPI import IOAPI

flightData = IOAPI().opener("NewUpcomingFlights.csv")
DisplayScreen().printList(flightData, rowLimit=8)

firstVoyage = [flightData[0], flightData[1]]
voyageFromData = Voyage(firstVoyage)
print(voyageFromData)