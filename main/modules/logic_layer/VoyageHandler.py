from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.DateUtil import DateUtil
import datetime


class VoyageHandler:
    def __init__(self, flights:list = [], dataFiles:dict = {}):
        self.dataFiles = dataFiles

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
        flightData = "{}\n{}".format(self.__flightOut[1], self.__flightIn[1])
        return flightData

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
    # Create New Voyage
    #===================================================================================

    def createVoyage(self):
        '''Create a new voyage, voyage contains of two flights with different flight numbers.
            have to get destination that we already fly to, date that the voyage will occur and than when the flight back home to Iceland is '''

        # Get and print list of available destinations
        destination_list = IOAPI().opener(self.dataFiles["DESTINATIONS_FILE"]) 
        DisplayScreen().printOptions(destination_list, "destinations")

        # Seect a destination
        destination_str =  InputHandler().numChoices(len(destination_list),"Select index of destination for this voyage: ")
        self.__destination = destination_list[int(destination_str)-1]

        # Departure messages for inputHandler
        inputDepartureDate_str = "Enter departure date from Iceland to {} (DD/MM/YYYY): ".format(self.__destination["destination"])
        inputDepartureTime_str = "Enter departure time (HH:MM): "
        ErrorDepartureTime_str = "ERROR: Airport is occupied at selected time \nplease input a new departure time: "

        # get the departure time from inputHandler
        self.__departure = self.selectDepartureTime(inputDepartureDate_str, inputDepartureTime_str, ErrorDepartureTime_str)

        # Find a date and time for arrival

        inputArrivalDate_str = "Enter return date to Iceland from {}: ".format(self.__destination["destination"])
        self.__return = InputHandler().dateOnly(inputArrivalDate_str)
        # Find available aircraft
        self.selectAircraft()

        # print all the info about the voyage for the user and ask if the info is correct, if not than edit info, else save to data

        # Make a flightnumber for both flights, the flight numbers are different depending on the destination and how many other flights have gone to the destination on this same day
        self.createFlights()
            # To make a flightnumber you need the list of all destination and get the number for our destination, then check if there is another flight
            # on this day going to our destination. If there is another flight to our destination then the number is NA XX2 otherwise NAXX0

        # check if the user wants to use this template of voyage at other days

        print("Do you want to replicate this voyage? (y/n): ")

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
    # methods for local use
    #===================================================================================

    def processFlight(self, flight:dict):
        """Returns a list with two values: flightnumber and data dictionary"""
        flightData = [flight["flightNumber"], flight]
        return flightData

    def createFlightNumber(self,latestFlightNumber: str):
        """Creates a new flightNumber based on destination and latest flightNumber"""
        # We have been given permission to ignore any requirments of flightNumber format.
        flightNum = int(latestFlightNumber[2:])+1
        #returns a number that is 1 higher
        return "NA{}".format(str(flightNum))

    def selectAircraft(self):
        """Displays list of available aircrafts and selects one from input"""
        #Get and print list of available aircrafts
        aircrafts_list = IOAPI().opener(self.dataFiles["AIRCRAFT_FILE"])

        #needs to check if plane is actually available at selected timeframe
        available_planes = aircrafts_list

        # print the available aircrafts
        DisplayScreen().printOptions(available_planes,"planes")

        # Select a aircraft from list
        inputAircraft_str = "Enter the number of the plane you want to use in this voyage from the plane list: "
        self.__aircraftID = InputHandler().numChoices(len(available_planes), inputAircraft_str)

    # --------- Departure Time ---------------------------------------------------------------
    def selectDepartureTime(self,questionDate:str, questionTime:str, errorMessage:str):
        """Prompts the user to input date and time"""

        #ERROR Check if there is any departing from Iceland at this dateTime
        departingFlights_list = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"]) 
        departingOnDate_list = []

        selectedDate = InputHandler().dateOnly(questionDate)
        # just collect the flights departing on same day
        for flight in departingFlights_list:
            if flight['departingFrom'] == self.__departingFrom:
                if flight['departure'][:10] == selectedDate[:10]:
                    departingOnDate_list.append(flight)
        
        # print the list of flights departing on that day
        headerDepartingOnDate_str = "List of other flights departing on same day"
        if len(departingOnDate_list) == 0:
            DisplayScreen().printText(["No departing flights"], headerDepartingOnDate_str) 
        else:
            DisplayScreen().printList(departingOnDate_list,headerDepartingOnDate_str)

        #ask the user for a time before entering the loop
        selectedDepartureTime_str = InputHandler().timeOnly(questionTime)
        while True:
            #check through list of flights and check their departure time
            if len(departingOnDate_list) != 0:
                for flight in departingOnDate_list:
                    flightDeparture = flight['departure']
                    timeCheckDate = DateUtil().updateTime(selectedDate, selectedDepartureTime_str)

                    #if airport was occupied, then print the list again and ask for time input
                    if flightDeparture == timeCheckDate:
                        DisplayScreen().printList(departingOnDate_list,"Departure time not available, please try again")
                        selectedDepartureTime_str = InputHandler().timeOnly("Please select a different time, "+questionTime)
                        continue
                    else:
                        #if everything is alright, then return the dateTime
                        return timeCheckDate
            else:
                DateUtil().updateTime(selectedDate, selectedDepartureTime_str)
        
        
            #repeat the loop until proper time has been selected
                
            

    def calculateArrival(self, departure:str, flightTime:str):
        """Calculates arrival time, requires the datetime of departure and the flightTime"""

        departureTime = DateUtil(departure).createObject()

        #split the flighttime into parts
        hours,minutes,seconds = map(int,flightTime.split(':'))
        
        #get the arrivaltime
        arrival = departureTime + datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

        return str(arrival.isoformat())

    #===================================================================================
    # Exporting data
    #===================================================================================

    def getFlights(self):
        """returns list of flights related to this voyage, will create the flights if missing"""

        #if voyage already has created flights with fightNumbers, then it returns those flights
        flightData = self.__flightOut[0] 
        
        if len(flightData) != 0:
            #gets the flight objects and returns them in a list
            return [self.__flightOut[1], self.__flightIn[1]]

        #else it creates new flightNumbers
        else:         
            self.createFlights()

    def createFlights(self):
        """Creates a pair of flights that make up the voyage, requires the last flightNumber 
        created (for reference when creating new flightNumbers)"""

        # get the latest flightNumber created, for reference
        allFlights_list = IOAPI().opener(self.dataFiles["UPCOMING_FLIGHTS_FILE"])
        self.latestFlight = allFlights_list[len(allFlights_list)-1]["flightNumber"]

        def flightData(direction:str):
            """Creates a data dictionary"""
            startLocation = self.__departingFrom
            endLocation = self.__destination["id"]
            departure = self.__departure
            duration = self.__destination["flightDuration"]
            flightDict = {}
            flightNumber = self.createFlightNumber(self.latestFlight)

            # swap locations depending on direction of flight
            if direction == "in":
                startLocation, endLocation = endLocation, startLocation
                departure = self.__return

            flightDict["flightNumber"] = flightNumber
            flightDict["departingFrom"] = startLocation
            flightDict["arrivingAt"] = endLocation
            flightDict["departure"] = departure
            flightDict["arrival"] = self.calculateArrival(departure,duration)   #departure + flightTime
            flightDict["aircraftID"] = self.__aircraftID
            flightDict["captain"] = self.__captain
            flightDict["copilot"] = self.__copilot
            flightDict["fsm"] = self.__fsm
            flightDict["fa1"] = self.__fa1
            flightDict["fa2"] = self.__fa2

            #update the latest flightnumber
            self.latestFlight = flightNumber
            IOAPI().appender(self.dataFiles["UPCOMING_FLIGHTS_FILE"],flightDict.copy())
            return flightDict.copy()

        #create the flight out
        flightOut_dict = flightData("out")
        self.__flightOut = [flightOut_dict["flightNumber"], flightOut_dict]

        #create the flight in
        flightIn_dict = flightData("in")
        self.__flightIn = [flightIn_dict["flightNumber"], flightIn_dict]

        #give the IOAPI the flight data to save
        return [flightOut_dict, flightIn_dict]
        



