from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.DateUtil import DateUtil

FILE_DESTINATIONS = "Destinations.csv"
FILE_FLIGHTS_UPCOMING = "NewPastFlights.csv"

class Voyage:
    def __init__(self, flights:list = []):
        self.__flightOut = ["", {}]
        self.__flightIn = ["", {}]
        # destination and airport
        self.__destination = None
        self.__departingFrom = "KEF"
        # times of departure and arrival
        self.__departure = None
        self.__return = None
        # other information
        self.__aircraftID = None
        self.__captain = None
        self.__copilot = None
        self.__fsm = None
        self.__fa1 = None
        self.__fa2 = None

        #will run setVoyage if flight data is provided on init
        if len(flights) != 0:
            self.setVoyage(flights)
    
    def __str__(self):
        """Fancy print info"""
        voyageInfo = [
            self.__destination,
            self.__departure,
            self.__return,
            self.__captain,
            self.__copilot,
            self.__fsm,
            self.__fa1,
            self.__fa2
        ]
        voyage_str = "Base info -----------------\n"
        voyage_str += " Destination: {}\n"
        voyage_str += " Departure: {}\n"
        voyage_str += " Returning: {}\n"
        voyage_str += "Crew ----------------------\n"
        voyage_str += " Captain: {}\n"
        voyage_str += " Copilot: {}\n"
        voyage_str += " Flight Service Manager: {}\n"
        voyage_str += " Flight attendant 1: {}\n"
        voyage_str += " Flight attendant 2: {}\n"
        return voyage_str.format(*voyageInfo)

    def __repr__(self):
        """String"""
        return "flights"

    #===================================================================================
    #  Initialize a voyage from existing data
    #===================================================================================
    def setVoyage(self, data:list):
        """Takes list of 2 flights (first out, second in) and creates a voyage"""
        #The flights
        outFlight = data[0]
        inFlight = data[1]
        self.__flightOut = self.processFlight(outFlight)
        self.__flightIn = self.processFlight(inFlight)

        #extract voyage data from outgoing flight

        # destination and airport
        self.__destination = outFlight["arrivingAt"]
        # times of departure and arrival
        self.__departure = outFlight["departure"]
        self.__return = inFlight["departure"]
        # other information
        self.__aircraftID = outFlight["aircraftID"]
        self.__captain = outFlight["captain"]
        self.__copilot = outFlight["copilot"]
        self.__fsm = outFlight["fsm"]
        self.__fa1 = outFlight["fa1"]
        self.__fa2 = outFlight["fa2"]
    #===================================================================================
    # Processing/creating data for use in methods
    #===================================================================================
    def processFlight(self, flight:dict):
        """Returns a list with two values: flightnumber and data dictionary"""
        flightData = [flight["flightNumber"], flight]
        return flightData

    def findDepartingFlights(self):
        """Returns a list of dictionaries of only departing flights"""
        return []

    def findAircrafts(self):
        """Returns a list of available aircrafts"""
        return []

    def createFlightNumber(self,destination:str,latestFlightNumber: str):
        """Creates a new flightNumber based on destination and latest flightNumber"""
        # We have been given permission to ignore any requirments of flightNumber format.
        flightNumRef = int(latestFlightNumber[2:])
        #returns a number that is 1 higher
        return "NA{}".format(str(flightNumRef+1))


    #===================================================================================
    # INPUT selection
    #===================================================================================
    # --------- Aircraft ---------------------------------------------------------------
    def selectAircraft(self):
        """Displays list of available aircrafts and selects one from input"""
        #Get and print list of available aircrafts
        availableAircrafts_list = self.findAircrafts
        DisplayScreen().printOptions(availableAircrafts_list)

        # Select a aircraft from list
        inputAircraft_str = "Enter the number of the plane you want to use in this voyage from the plane list: "
        self.__aircraftID = InputHandler().numOptions(inputAircraft_str)
    # --------- Destination ---------------------------------------------------------------
    def selectDestination(self):
        """Displays list of available destinations and selects one from input"""

        # Get and print list of available destinations
        destination_list = IOAPI().opener(FILE_DESTINATIONS) 
        DisplayScreen().printOptions(destination_list, "destinations")

        # Seect a destination
        destination_str =  InputHandler().numOptions("Select a destination for this voyage: ")
        self.__destination = destination_list[int(destination_str)-1]

    # --------- Departure Time ---------------------------------------------------------------
    def selectDepartureTime(self,questionDate:str, questionTime:str, errorMessage:str):
        """Prompts the user to input date and time"""
        selectedDateTime = InputHandler().dateTime(questionDate,questionTime)

        #ERROR Check if there is any departing from Iceland at this dateTime
        departingFlights_list = self.findDepartingFlights() #list of upcoming flights departing from Iceland
        while selectedDateTime in departingFlights_list:
            newTime_str = InputHandler().timeOnly(errorMessage)

            #update the time of departure
            newDateTime_str = DateUtil().updateTime(selectedDateTime, newTime_str)
            selectedDateTime = newDateTime_str
        
        return selectedDateTime

    def selectArrivalTime(self):
        """Gets a valid arrival time for voyage"""

        inputArrivalDate_str = "Enter the date for the flight from {} to Iceland".format(self.__destination)
        self.__return = InputHandler().dateOnly(inputArrivalDate_str)

        #calculate a date that is departure + flightTime, 


    #===================================================================================
    # Create New Voyage
    #===================================================================================
    def createVoyage(self):
        '''Create a new voyage, voyage contains of two flights with different flight numbers.
            have to get destination that we already fly to, date that the voyage will occur and than when the flight back home to Iceland is '''

        # get destination from input
        self.selectDestination()
        # Departure messages for inputHandler
        inputDepartureDate_str = "Enter the date for the flight from Iceland to {}".format(self.__destination)
        inputDepartureTime_str = "Enter departure time"
        ErrorDepartureTime_str = "ERROR: Airport is occupied at selected time \nplease input a new departure time: "

        # get the departure time from inputHandler
        self.__departure = self.selectDepartureTime(inputDepartureDate_str, inputDepartureTime_str, ErrorDepartureTime_str)

        # Find a date and time for arrival
        self.selectArrivalTime()

        # Find available aircraft
        self.selectAircraft()

        # print all the info about the voyage for the user and ask if the info is correct, if not than edit info, else save to data

        # Make a flightnumber for both flights, the flight numbers are different depending on the destination and how many other flights have gone to the destination on this same day
        self.createFlights()
            # To make a flightnumber you need the list of all destination and get the number for our destination, then check if there is another flight
            # on this day going to our destination. If there is another flight to our destination then the number is NA XX2 otherwise NAXX0

        # check if the user wants to use this template of voyage at other days

        print("Do you want to replicate this voyage? (y/n)")

    #===================================================================================
    # Update Crew
    #===================================================================================
    def updateCrew(self):
        '''Update and/or put staff in roles in upcoming Voyages'''

        #get list of voyages from data layer
        # the user can choose the voyage he/she wants to update from the list of voyages, the user enters the number of the voyage (flight)

        upcomingVoyage_list = []  #get list from data layer, this is just for now
        numberOfVoyage_int = int(InputHandler().dateOnly("Enter the number of the voyage in the list you want to update/change: "))
        theVoyage = upcomingVoyage_list[numberOfVoyage_int]

        # print the info that are currently right for the voyage, if there are any staff members in some roles or if the roles are empty and there needs to fill all the roles
        print(theVoyage)

        # the user inputs the number of the role he/she wants to change/fill.
        roleToChange_int = int(InputHandler().dateOnly("Enter the number of the role in the list you want to update/change: "))

        # the user gets a list of all staff members who can play that role and who ara avilable during the voyage's time

        # Get a list of staff members who can do this role from data layer
        rolelist_list = []   #just for now need to get from data layer

        # ask the user if he/she wants to save the changes or if he/she wants to change/fill some other roles
        toChangeOrNotToChange_bool = InputHandler().dateOnly("Do you want to save the changes? (y/n) ")
        
        # when he wants to save then save this voyage info in the data layer.
        # if the user wants to quit then no changes were made.

    #===================================================================================
    # Exporting data
    #===================================================================================
    def getFlights(self):
        self.createFlights()
    def createFlights(self):
        """Creates a pair of flights that make up the voyage, requires the last flightNumber created (for reference when creating new flightNumbers)"""
        #if voyage already has created flights with fightNumbers, then it returns those flights
        if len(self.__flightOut[0]) != 0:
            #gets the flight objects and returns them in a list
            return [self.__flightOut[1], self.__flightIn[1]]
        #else it creates new flightNumbers
        else: 
            # create a dictionary with all info shared in both flights
            flightInfo = {
                "aircraftID": self.__aircraftID,
                "captain": self.__captain,
                "copilot": self.__copilot,
                "fsm": self.__fsm,
                "fa1": self.__fa1,
                "fa2": self.__fa2
            }
            #the list of flights that will be given to IOAPI
            createdFlights = []

            # get the latest flightNumber created, for reference
            allFlights_list = IOAPI().opener(FILE_FLIGHTS_UPCOMING)
            latestFlight = allFlights_list[len(allFlights_list)]["flightNumber"]

            #create the flight out
            flightOut = flightInfo.copy()
            flightOut["flightNumber"] = self.createFlightNumber(latestFlight)
            flightOut["destination"] = self.__departingFrom
            flightOut["arrivingAt"] = self.__arrivingAt
            flightOut["departure"] = self.__departure
            flightOut["arrival"] = self.__return #departure + flightTime

            createdFlights.append(flightOut)

            #create the flight home
            flightIn = flightInfo.copy()
            flightOut["flightNumber"] = self.createFlightNumber(latestFlight)
            flightOut["destination"] = self.__departingFrom
            flightOut["arrivingAt"] = self.__arrivingAt
            flightOut["departure"] = self.__return
            flightOut["arrival"] = self.__return #departure + flightTime

            createdFlights.append(flightIn)

            #give the IOAPI the flight data to save
            return createdFlights
            

