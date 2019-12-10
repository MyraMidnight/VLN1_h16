
class DisplayScreen:
    def __init__(self):
        #===================================================================================
        # A dictionary that contains custom column widths and titles for each key
        #
        # the order of the columns in dictionary decides the order they appear in
        #
        # The 'templates' are optional layouts available, lists the columns to hide
        # 
        #===================================================================================
        self.__dataTypes = { #column widths for specific data
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
        self.__allTemplates = self.__listAllTemplates()
    
    def __listAllTemplates(self):
        """Just creates a dictionary of all available templates that references it's dataType"""
        allTemplates_list = {}
        for dataType, value in self.__dataTypes.items():
            for template in value["templates"].keys():
                allTemplates_list[template] = dataType

        return allTemplates_list

    def detectDataType(self, data:dict, colWidth:int = 10):
        """Figures out what type of data is being provided"""

        #Create list of keys for each dataType from self.__dataTypes
        refDataTypes_dict = {}
        for dataType, value in self.__dataTypes.items():
            refDataTypes_dict[dataType] = value["columns"]
        
        #Compare the keys of given data with refDataTypes
        for dataType, columns in refDataTypes_dict.items():

            #if match is found, return the results
            if data[0].keys() == columns.keys():
                return self.__dataTypes[dataType]

            #else create a dictionary from the given data
            else:
                return {{key:{"colWidth":colWidth, "title":key}} for key in data[0].keys()}


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

    #===================================================================================
    # Sections for printFrame
    #===================================================================================

    def __sectionHeader(self, data:list, screenWidth:int, frame:str):
        """Prints the header section"""

    def __sectionList(self, data:list, screenWidth:int, frame:str):
        """Prints the list section """
        for row in data:
            #if titleRow
            if row == data[0]:
                for title in data[0].values():
                    print(" | ".join(title))


    def __sectionText(self, data:list, screenWidth:int, frame:str):
        """Prints the list section """

    def __sectionShortCuts(self, data:list, screenWidth:int, frame:str):
        """Prints the list section """

    #===================================================================================
    # the screen printer
    #===================================================================================

    def printFrame(self, screenData:list, screenWidth: int):
        #example of screen data types, the order can be decided by the caller
        screenData_list = [
            {"header": [""]}, #a string that will be printed as header
            {"list": [{},{}]}, #first line is titleRow
            {"text": ["",""]}, #lines seperated into a list
            {"shortcuts": ["",""]} #list of strings for each shortcut
        ]

        #the actual screenData given in parameters
        screenData_list = screenData

        #print handler
        screenSections_dict = {
            "header": self.__sectionHeader,
            "list": self.__sectionList,
            "text": self.__sectionText,
            "shortcuts": self.__sectionShortCuts
        }

        #print the screenData
        frameTop_str = "#"*screenWidth
        frameBottom_str = frameTop_str
        frame_str = "|{}|"

        #print the top
        print(frameTop_str)

        #print the body of frame
        for section in screenData_list:
            for sectionType_str, sectionData_list in section.items():
                #run the section method with given data
                screenSections_dict[sectionType_str.lower()](sectionData_list, screenWidth, frame_str)
        #print the bottom
        print(frameBottom_str)
    
    #===================================================================================
    # Processing methods
    #===================================================================================

    def __formatRow(self, rowData:dict, colWidth, titles:bool = False):
        """Processes the strings per column"""

        formattedRow_dict = {}
        for column,value in rowData.items():

            #if the row is header/title row, then use titles
            if titles == True:
                value = dataType["titles"][column]

            #if value length is longer than colWith limit, then trim
            if len(value) > colWidth:
                value_str = value[:colWidth]

            #else it fills in the empth space
            else:
                value_str = self.cutString(value,colWidth)
            formattedRow_dict[column] = value_str

    def processTable(self, data:list, colWidth:int):
        """Cuts/fills the strings for each column""", 
        dataType = self.detectDataType(data)

        #creates a list of column keys in order
        columnOrder = [column for dataType["columns"].keys()]


        #process each column value to fit the colWidth
        formattedList = []
        #create the title row
        formattedList.append(self.__formatRow(data[0], colWidth, True))

        #process the table
        for row in data: 
            trimmedRow_dict = self.__formatRow(row)
            #append a copy of the row in formatedList
            formattedList.append(trimmedRow_dict.copy())

        return formattedList


    #===================================================================================
    # Methods that compile the screens for print
    #===================================================================================
    
    def printList(self, data:list, rowLimit:int = 0,colWidth:int = 10, formatTemplate: str = "", keys: bool = False):
        """Prints a given list, can optionally print the key as column title, else it uses the given titles"""
        #get the dataType for 
        dataType_dict = self.detectDataType(data)

        #create the header row (print the keys)
        columnTitles = []
        
        for colKey, info in dataType_dict.items():
            if len(colKey) > colWidth:
                colTitle = colKey[:colWidth]
            else:
                colTitle = self.cutString(colKey,colWidth)
            columnTitles.append()
            #title = self.__printTemplates["titles"][counter]
            #columnTitles.append(self.cutString(title, colWidth))
            #counter += 1

        headerRow = " | ".join(columnTitles)
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
            
        if formatTemplate in self.__allTemplates:
            #find the correct template and info for reference
            dataType_str = self.__allTemplates[formatTemplate]
            template_list = self.__dataTypes["templates"][formatTemplate]
            columnInfo_dict = self.__dataTypes[dataType_str]["columns"]

            #set the row limit
            #create the header row (print the keys)
            columnTitles = []
            print()
            for column in data:
                if column not in template_list:
                    title = columnInfo_dict["titles"][column]
                    colWidth = columnInfo_dict[column]

                    trimmedKey = self.cutString(title,colWidth)
                    columnTitles.append(trimmedKey)
                    counter += 1 
            headerRow = " | ".join(columnTitles)
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
                    row.append(self.cutString(colValue,self.__colWidths[template["dataType"]][column]))
                #joins the columns together with '|' seperator
                print(" | ".join(row)) 
        else: 
            self.printList(data,rowLimit=rowLimit)

    def printOptions(self, data:list, formatTemplate: str):
        """Makes printing enumerated tables easy"""
        self.printListFormat(data, formatTemplate=formatTemplate, enumerate= True)