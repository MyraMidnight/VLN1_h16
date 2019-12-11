from modules.logic_layer.GetLogic import GetLogic
from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.ui_layer.InputHandler import InputHandler

from operator import itemgetter #for sorting list of dictionaries by key
class UpdateLogic :
    """Update methods for logic layer"""
    def __init__(self, dataFiles):
        self.dataFiles = dataFiles #gets the file list from LLAPI

    def updateEmployee(self):
        """choose a employee (get a list and choose from the list). Get the info about the chosen 
        employee and then choose what info you want to change. 
        Then the user will be asked if he wants to save the changes. 
        Save the new information about the employee to the list about all employees """
        
        #Show list
        GetLogic(self.dataFiles).getAllCrew()
        #Choose Employee
        GetLogic(self.dataFiles).getSingleEmployee()
        #Show employee info
        #Ask what the motherfucker wants to change for fucks sake
        #Change some shit or fuck off
        #Confirm whether the fucker is co ntent with the fucking changes
        #fuck the fuck off

        
    def updateVoyage(self):
        """ Updates the crew on a voyage """

        departingFlights_dict = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])

        #get the list 
        departingFlights_list = []
        for flight in departingFlights_dict:
            if flight['departingFrom'] == 'KEF':
                departingFlights_list.append(flight)
        
        #give user option to choose how the list is sorted:
        sortOptions = [
            {"sortBy": "departure"}, 
            {"sortBy": "arrivingAt"}, 
            {"sortBy": "flightNumber"}
        ]
        DisplayScreen().printOptions(sortOptions, header="Voyages can be sorted in the following ways")
        sortedChoice_int = int(InputHandler().numChoices(len(sortOptions), "How would you like the voyages to be sorted? :"))
        sortedBy_str = sortOptions[sortedChoice_int-1]["sortBy"]

        #sort the list by departure time
        sortedDepartures_list = sorted(departingFlights_list, key=itemgetter(sortedBy_str), reverse=True)

        #print the upcoming voyages
        DisplayScreen().printOptions(sortedDepartures_list)
        # ask user to select a flight from the list representing the voyage
        selectedFlight_int = int(InputHandler().numChoices(len(departingFlights_list), "Select a voyage from the list: "))
        # create instance of VoyageHandler using the two connected flights
        # Print the crew in selected flight
        # let user pick what role to update
        # print list of employees available for this voyage for this role
        # loop through asking if they want to update staff
        # pressing q will ask for confirmation of saving the data
        # then find the flights that were updated and replace them
        # send the changed list of flights to updater
