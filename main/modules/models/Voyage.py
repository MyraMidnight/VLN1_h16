from modules.ui_layer.InputHandler import InputHandler
from modules.ui_layer.DisplayScreen import DisplayScreen
from modules.data_layer.IOAPI import IOAPI
from modules.ui_layer.DateUtil import DateUtil
import datetime


class Voyage:
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

        self.__attributes = {
            'destination': self.__destination,
            'departingFrom': self.__departingFrom,
            'departure': self.__departure,
            'return': self.__return,
            'aircraftID': self.__aircraftID,
            'captain': self.__captain, 
            'copilot': self.__copilot, 
            'fsm': self.__fsm, 
            'fa1': self.__fa1, 
            'fa2': self.__fa2,
        }
        #will run setVoyage if flight data is provided on init
        if len(flights) != 0:
            self.setVoyage(flights)
    
    def __str__(self):
        """Fancy print info"""

        listAttributes = ["Voyage information:\n"]
        formatString = "{}: {}"
        for attribute, value in self.__attributes.items():
            listAttributes.append(formatString.format(attribute, value))
        
        return "\n".join(listAttributes)

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
            

    def addCrew(self, crew:dict = {}):
        """Takes a dictionary with crew roles as keys and updates the crew of instance"""
        if len(crew.keys()) != 0:
            #go through the given crew and assign to the Voyage
            for role, employee in crew.items():
                self.__attributes[role] = employee
        else:
            #compile the current crew and return it
            roles = ['captain', 'copilot', 'fsm', 'fa1', 'fa2']
            for role in roles:
                crew[role] = str(self.__attributes[role])
        return crew #returns the updated crew
        
    #===================================================================================
    # Exporting data
    #===================================================================================

    def getFlights(self, refFlightNumber:str):
        """returns list of flights related to this voyage, will create the flights if missing"""

        #if voyage already has created flights with fightNumbers, then it returns those flights
        flightData = self.__flightOut[0] 
        
        if len(flightData) != 0:
            #gets the flight objects and returns them in a list
            return [self.__flightOut[1], self.__flightIn[1]]

        #else it creates new flightNumbers
        else:         
            self.createFlights(refFlightNumber)

    def createFlights(self, refFlightNumber:str):
        """Creates a pair of flights that make up the voyage, requires the last flightNumber 
        created (for reference when creating new flightNumbers)"""

        # get the latest flightNumber created, for reference
        self.latestFlight = refFlightNumber

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
