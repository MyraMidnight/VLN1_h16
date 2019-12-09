from modules.ui_layer.DisplayScreen import DisplayScreen
#from modules.data_layer.IOAPI import IOAPI
# from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DateUtil import DateUtil
from modules.ui_layer.MenuHandler import MenuHandler

from modules.models.Voyage import Voyage
from modules.data_layer.IOAPI import IOAPI
from modules.logic_layer.CreateLogic import CreateLogic

# flightData = IOAPI().opener("NewUpcomingFlights.csv")
# DisplayScreen().printList(flightData, rowLimit=8)

# firstVoyage = [flightData[0], flightData[1]]
# voyageFromData = Voyage(firstVoyage)
# print(voyageFromData)



# newVoyage = Voyage()
# newVoyage.createVoyage()
# print(repr(newVoyage))


# import datetime

# dateObject = DateUtil("2020-11-03T10:20:00").createObject()


# print(dateObject)
# newTime = dateObject + datetime.timedelta(hours=4)
# print(newTime)
# newTime = newTime - datetime.timedelta(hours=9)
# print(newTime)
# #print(dateObject.timedelta(hours=3))

MenuHandler("create").displayMenu()