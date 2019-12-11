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

        # Let user select a destination from list
        availableDestinations_dict = IOAPI().opener(self.dataFiles["DESTINATIONS_FILE"])

        # prints the destinations on screen
        DisplayScreen().printOptions(availableDestinations_dict, header="List of available destinations")

        # select a destination
        inputDestination_str = "Select a destination by index: "
        destSelection = InputHandler().numChoices(len(availableDestinations_dict), inputDestination_str)
        destination_str = availableDestinations_dict[int(destSelection)-1]["id"]
        
        # list the flights that are departing to selected destination
        departingFlights_dict = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])

        #go through the list and check flights with selected destination
        flightsToDestination_list = []
        for flight in departingFlights_dict:
            if flight['arrivingAt'] == destination_str:
                flightsToDestination_list.append(flight)
                
        #sort the list by departure time
        sortedDepartures_list = sorted(flightsToDestination_list, key=itemgetter('departure'), reverse=True)
        

        # ask user to select a flight from the list representing the voyage
        DisplayScreen().printOptions(flightsToDestination_list, "Select a departing flight from the list")
        # create instance of VoyageHandler using the two connected flights
        # Print the crew in selected flight
        # let user pick what role to update
        # print list of employees available for this voyage for this role
        # loop through asking if they want to update staff
        # pressing q will ask for confirmation of saving the data
        # then find the flights that were updated and replace them
        # send the changed list of flights to updater
