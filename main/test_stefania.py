from modules.ui_layer.DisplayScreen import DisplayScreen
# # from modules.ui_layer.InputHandler import InputHandler
# from modules.ui_layer.DateUtil import DateUtil
# from modules.ui_layer.MenuHandler import MenuHandler

# from modules.models.Voyage import Voyage
from modules.data_layer.IOAPI import IOAPI
# from modules.logic_layer.CreateLogic import CreateLogic

#--------------- Testing voyage
flightData = IOAPI().opener("NewUpcomingFlights.csv")
# DisplayScreen().printList(flightData, rowLimit=8)

# firstVoyage = [flightData[0], flightData[1]]
# voyageFromData = Voyage(firstVoyage)
# print(voyageFromData)

# newVoyage = Voyage()
# newVoyage.createVoyage()
# print(repr(newVoyage))

#--------------- Testing DateUtil
# import datetime

# dateObject = DateUtil("2020-11-03T10:20:00").createObject()

# print(dateObject)
# newTime = dateObject + datetime.timedelta(hours=4)
# print(newTime)
# newTime = newTime - datetime.timedelta(hours=9)
# print(newTime)
# #print(dateObject.timedelta(hours=3))


# #--------------- creating a function that can print list of methods
# menu = MenuHandler("create")
# methods = dir(MenuHandler)

# def printMethods(menu:object):
#   classMethods = []
#   for method in dir(menu):
#     if method[:2] != "__":
#       classMethods.append(method)

#   for method in classMethods:
#     print(method)

# printMethods(menu)
screenData = [
  {"header": ["Header of screen"]},
  {"list": flightData}
]
dataType = DisplayScreen().printFrame(screenData, 100)
print(dataType)