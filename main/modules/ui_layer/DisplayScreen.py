
class DisplayScreen:
    def __init__(self):
        self.stringLimits = { #column widths for specific data
            "crew": {'ssn': 10, 'name': 20, 'role': 10, 'rank': 15, 'licence': 8, 'address': 20, 'phonenumber': 14},
            "flights": {'flightNumber': 10, "departingFrom": 10, "arrivingAt": 10 , "departure": 10, "arrival": 10, "aircraftID": 10, "captain": 10, "copilot": 10, "fsm": 10, "fa1": 10, "fa2": 10},
            "destinations": {"id": 10, "destination": 10},
            "plane": {"planeInsignia":10, "planeTypeId": 10},
            "planeType": {"planeTypeId": 10,"manufacturer": 10,"model": 10,"capacity": 10,"emptyWeight": 10,"maxTakeoffWeight": 10,"unitThrust": 10,"serviceCeiling": 10,"length": 10,"height": 10,"wingspan":10},
            "voyages": {"fnDeparting": 10, "fnReturning": 10,"captain": 10, "copilot": 10, "fsm": 10, "fa1": 10, "fa2": 10}

        }
        #specifies what type of stringLimits and what columns to print
        self.printTemplates = {
            "crew": { 
                "dataType": "crew", 
                "columns": [ "name", "ssn", "rank", "licence", "address", "phonenumber"]
            },
            "pilots": { 
                "dataType": "crew", 
                "columns": ["name", "ssn", "rank", "licence", "address", "phonenumber"]
            },
            "cabincrew": { 
                "dataType": "crew", 
                "columns": ["name", "ssn", "rank", "address", "phonenumber"]
            },
            "flights": {
                "dataType": "flights",
                "columns" : ["flightNumber", "departingFrom", "arrivingAt", "departure", "arrival", "aircraftID", "captain", "copilot", "fsm", "fa1", "fa2"]
            },
            "destinations": {
                "dataType": "destinations",
                "columns" : ["id", "destination"]
            },
            "planes": {
                "dataType": "planes",
                "columns" : ["planeInsignia", "planeTypeId"]
            },
            "voyages": {
                "dataType": "voyages",
                "columns" : ["fnDeparting","fnReturning","captain", "copilot", "fsm", "fa1", "fa2"]
            },
        }

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

    def printList(self, data:list, rowLimit:int = 0,colWidth:int = 10, colLimit:int = 0):
        #create the header row (print the keys)
        headerKeys = []
        print()
        for column in data[0]:
            headerKeys.append(self.cutString(column,colWidth))
        headerRow = " | ".join(headerKeys)
        print(headerRow)
        print("-"*len(headerRow))
        #loop through each line of data

        if rowLimit == 0:
            rowLimit = len(data)
        if colLimit == 0:
            colLimit = len(data[0])

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
            
        if formatTemplate in self.printTemplates:
            template = self.printTemplates[formatTemplate]
            #set the row limit
            #create the header row (print the keys)
            headerKeys = []
            print()
            for column in template["columns"]:
                headerKeys.append(self.cutString(column,self.stringLimits[template["dataType"]][column]))
            headerRow = " | ".join(headerKeys)
            print(headerRow)
            print("-"*len(headerRow))
            #loop through each line of data
            for line in data[:rowLimit]:
                row = []
                #prints the columns specified in the 'formats' dict
                for column in template["columns"]:
                    #if value is longer than set limit width, then cut 
                    colValue = line[column]
                    row.append(self.cutString(colValue,self.stringLimits[template["dataType"]][column]))
                #joins the columns together with '|' seperator
                print(" | ".join(row)) 
        else: 
            self.printList(data,rowLimit=rowLimit)

    def printOptions(self, data: list, rowLimit:int = 0):
        """Prints a enumerated list that the user can choose from."""
        self.printListFormat(data=data, formatTemplate, rowLimit=rowLimit, enumerate = True)