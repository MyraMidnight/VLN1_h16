
class DisplayScreen:
    def __init__(self):
        self.__dataTypes = { #column widths for specific data
        #===================================================================================
        # A dictionary that contains custom column widths and titles for each key
        #
        # The 'templates' are optional layouts available, containing lists of which 
        # columns it should skip printing (perhaps you want the list short and simple)
        # 
        #===================================================================================
            # crew ---------------------------------------
            "crew": { #dataType
                "columns": { #column specifications
                    'ssn': {"colWidth": 10, "title": "SSN"},
                    'name': {"colWidth": 20, "title": "Name"},
                    'role': {"colWidth": 10, "title": "Role"},
                    'rank': {"colWidth": 15, "title": "Rank"},
                    'licence': {"colWidth": 8, "title": "Licence"},
                    'address': {"colWidth": 20, "title": "Address"},
                    'phonenumber': {"colWidth": 14, "title": "Phone"}
                },                
                "templates": { #contain lists of keys of columns to ignore for each template
                    "crew": [], "pilots": [], "cabincrew": []
                }
            },
            # flights ---------------------------------------
            "flights": {
                "columns": {
                    'flightNumber': {"colWidth": 13, "title": "Flight Number"},
                    "departingFrom": {"colWidth": 13, "title": "From"},
                    "arrivingAt": {"colWidth": 10, "title": "To"},
                    "departure": {"colWidth": 15, "title": "Departure"},
                    "arrival": {"colWidth": 15, "title": "Arrival"},
                    "aircraftID": {"colWidth": 10, "title": "Aircraft ID"},
                    "captain": {"colWidth": 10, "title": "Captain"},
                    "copilot": {"colWidth": 10, "title": "Co-pilot"},
                    "fsm": {"colWidth": 10, "title": "Service Manager"},
                    "fa1": {"colWidth": 10, "title": "Flight attendant 1"},
                    "fa2": {"colWidth": 10, "title": "Flight attendant 2"}
                },                
                "templates": {
                    "flights": []
                }
            },
            # destinations ---------------------------------------
            "destinations": {
                "columns": {
                    "id": {"colWidth": 10, "title": "Airport"},
                    "destination": {"colWidth": 18, "title": "Destination"},
                },                
                "templates": {
                    "destinations":[]
                }
            },
            # planes  ---------------------------------------
            "planes": {
                "columns": {
                    "planeInsignia": {"colWidth": 15, "title": "Insignia"},
                    "planeTypeId":  {"colWidth": 20, "title": "Type"}
                },
                "templates": {
                    "planes":[]
                }
            },
            # plane types ---------------------------------------
            "planeTypes": { 
                "columns": {
                    "planeTypeId":  {"colWidth": 10, "title": "Type"},
                    "manufacturer":  {"colWidth": 10, "title": "Manufacturer"},
                    "model":  {"colWidth": 10, "title": "Model"},
                    "capacity":  {"colWidth": 10, "title": "Capacity"},
                    "emptyWeight":  {"colWidth": 10, "title": "Weight (empty)"},
                    "maxTakeoffWeight":  {"colWidth": 10, "title": "Weight limit"},
                    "unitThrust":  {"colWidth": 10, "title": "Thrust"},
                    "serviceCeiling":  {"colWidth": 10, "title": "Serv.Ceiling"},
                    "length":  {"colWidth": 10, "title": "Length"},
                    "height":  {"colWidth": 10, "title": "Height"},
                    "wingspan": {"colWidth": 10, "title": "Wingspan"}
                },
                "templates": {
                    "planeTypes":[]
                }
            },
            # voyages ---------------------------------------
            "voyages": {
                "columns": {
                    "fnDeparting":  {"colWidth": 10, "title": "Departing"},
                    "fnReturning":  {"colWidth": 10, "title": "Returning"},
                    "captain":  {"colWidth": 10, "title": "Captain"},
                    "copilot":  {"colWidth": 10, "title": "Co-pilot"},
                    "fsm":  {"colWidth": 10, "title": "Service Manager"},
                    "fa1":  {"colWidth": 10, "title": "Flight attendant 1"},
                    "fa2":  {"colWidth": 10, "title": "Flight attendant 2"}
                },                
                "templates": {
                    "voyages":[]
                }
            }
        }
 
    def __detectDataType(self):
        """Figures out what type of data is being provided"""
        #get dataType references as a dictionary
        


    def cutString(self, string, limit:int = 10):
        """Creates a string that is of set length, if string was cut short then it adds dots, else it fills with spaces""" 
        if len(string) > limit:
            #cut it to fit the limit
            cutString = string[:limit] 
            newString = cutString[:-3] + "..." #replace last 3 letters with dots to indicate it was cut short
            return newString
        else: 
            #fill in the empty space
            newString = string.ljust(limit)
            return newString

    def printList(self, data:list, rowLimit:int = 0,colWidth:int = 10):
        #create the header row (print the keys)
        headerKeys = []
        print()
        #counter = 0
        for column in data[0]:
            headerKeys.append(self.cutString(column,colWidth))
            #title = self.__printTemplates["titles"][counter]
            #headerKeys.append(self.cutString(title, colWidth))
            #counter += 1

        headerRow = " | ".join(headerKeys)
        print(headerRow)
        print("-"*len(headerRow))
        #loop through each line of data

        if rowLimit == 0:
            rowLimit = len(data)

        for line in data[:rowLimit]:
            row = []
            #prints the columns specified in the 'formats' dict
            for column in line:
                #if value is longer than set limit width, then cut 
                colValue = line[column]
                row.append(self.cutString(colValue,colWidth))
            #joins the columns together with '|' seperator
            print(" | ".join(row)) 

            
    def printListFormat(self, data: list, formatTemplate: str = "", rowLimit:int = 0, enumerate:bool = False):
        """Prints data lists, takes in a list of dictionaries\n
            optional: can add 'type' parameter for specific format.\n
            Types: employees, cabincrew, pilots, flightattendants, planes, destinations
        """

        if rowLimit == 0:
            rowLimit = len(data)
            
        if formatTemplate in self.__printTemplates:
            template = self.__printTemplates[formatTemplate]
            #set the row limit
            #create the header row (print the keys)
            headerKeys = []
            print()
            counter = 0
            for column in template["columns"]:
                title = template["titles"][counter]
                stringLimit = self.__stringLimits[template["dataType"]][column]

                trimmedKey = self.cutString(title,stringLimit)
                headerKeys.append(trimmedKey)
                counter += 1 
            headerRow = " | ".join(headerKeys)
            horizonalDiv = "-"*len(headerRow)

            # add space before table if enumerated list
            if enumerate == True:
                enumSpace = "".ljust(5)
                headerRow = enumSpace + headerRow
                horizonalDiv = enumSpace + horizonalDiv
            print(headerRow)
            print(horizonalDiv)

            #loop through each line of data
            rowCounter_int = 0
            for line in data[:rowLimit]:
                row = []
                if enumerate == True:
                    rowCounter_int += 1
                    choiceIndex = "{})".format(str(rowCounter_int))
                    print(choiceIndex.ljust(5), end="")

                #prints the columns specified in the 'formats' dict
                for column in template["columns"]:
                    #if value is longer than set limit width, then cut 
                    colValue = line[column]
                    row.append(self.cutString(colValue,self.__stringLimits[template["dataType"]][column]))
                #joins the columns together with '|' seperator
                print(" | ".join(row)) 
        else: 
            self.printList(data,rowLimit=rowLimit)

    def printOptions(self, data:list, formatTemplate: str):
        """Makes printing enumerated tables easy"""
        self.printListFormat(data, formatTemplate=formatTemplate, enumerate= True)