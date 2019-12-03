# Beinagrind af prógramminu okkar :)

## UI layer
#### displayMenu()
> #handles displaying the menu options 

#### displaySchedule()
>displays who is on shift (or not on shift) on specified days, user inputs start date and then can fetch 1-7 days. 

#### displayAllPlanes()
>displays the list of planes and their status, displaying details if available, else display destination

#### displayPlane()
>displays specific plane based on ID

#### displayEmployees()
>display full list of all employees, optional parameter to display only flight attendants or pilots (default = all)
* displayFlightAttendants()
>> display a list of all flight attendants
* displayPilots()
>>display a list of all pilots

#### displaySingleEmployee()
>displays all the information about a specific employee, finds them with SSN

#### displayAllDestinations()
>displays list of all available destinations, distance from Iceland, airport

#### displayDestination()
>display all details for specific destination: country, distance from Iceland, flightDuration, airport, contact, emergancyPhone

## Logic layer
### CREATE
#### createEmployee()
> Requests input for name, ssn, address, homePhone, mobilePhone and email. Adds the employee to the registry.

#### createPlane()
>Requests input for planeName, and  planeType. Adds the plane to the registry

#### createVoyage()
>Creates a voyage by creating two flights and adding them to the registry. (flugin hafa sitthvort flugnúmerið)
* createFlight()
>>Creates a flight in a voyage. Requests input for destination, date & time of departure, date & time of return and airplane. Generates a flightnumber for the flight.  Adds the flight to the voyage.

#### createDestination()
>Create a new destination. Requests input for destinationLand, destinationAirport, destinationFlightTime, destinationDistance, destinationContactPerson and destinationEmergencyPhone.

### GET
#### getSingleEmployee()
#### getPilot()
>get a list of all pilots and then make the user choose the pilot the user wants or the user inputs the pilots ssn and gets the info of the pilot
#### getCoPilot()
>get a list of all co-pilots and then make the user choose the do-pilot the user wants or
>the user inputs the co-pilots ssn and gets the info of the co-pilot
>the user inputs the employee ssn and gets the info of the co-pilot


#### getEmployees()
>get a list of all the employees
* getPilots()
>> get a list of all the pilots, optional list pilots by license
* getFlightAttendants()
>> get a list of all the attendants

#### getPlanes()
>Get a list of planes containing 

#### getDestinations()
>creates a list of destinations

#### getVoyages()
>creates a list of Voyages

#### getSchedule()
* getOnShift()
>>cross reference employees with voyages to find emp. On shift
* getOffShift()
>>cross reference employees with voyages to find emp. Not on shift

### UPDATE
#### updateCrew()
>select employee with SSN and then can edit everything but the name and SSN


#### updateDestination()
>select destination with name and then can edit contact name and emergency number of contact

#### updateVoyage()
>assigns crewmembers and changes them around, look at state diagram 


## Data layer
#### openFile()
>opens all files and creates a file package which is a dictionary where key is a filename (e.g. crew.csv) and value is another dictionary, with a validTag which is either True or False and a list of lines from that file.
#### writeFile()
>takes the file package, checks for False validTags and over-writes those files

