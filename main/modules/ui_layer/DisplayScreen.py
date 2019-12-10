
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
                    'flightNumber': {"colWidth": 13, "title": "Flight nr."},
                    "departingFrom": {"colWidth": 5, "title": "From"},
                    "arrivingAt": {"colWidth": 5, "title": "To"},
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
        self.__currentTemplate = ""
    
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
            if set(data[0]) == set(columns):
                return {dataType: self.__dataTypes[dataType]}

            else:
                #continue checking through the data types
                continue
        #if no matches are found, return a custom dataType dict
        return { 
            dataType: {
                "columns": {
                    key:{"colWidth":colWidth, "title":key} for key in data[0].keys()
                },
                "templates": {dataType: []}
            }
        }

    #trims the strings to be specific length
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
        print(data[0])

    def __sectionList(self, data:list, screenWidth:int, frame:str):
        """Prints the list section """
        #get the dataType
        dataType_dict = self.detectDataType(data)
        dataType_str = list(dataType_dict.keys())[0]
        ignoredColumns = dataType_dict[dataType_str]["templates"][dataType_str]
        columnData_dict = dataType_dict[dataType_str]["columns"]
        
        #the dividers when joining the columns
        divider_str = " | "
        horizontalDiv_str = "-|-"

        #create the row strings
        listForPrint = []
        for row in data:
            firstRow = row == data[0]
            compiledRow = []
            titleRow = []
            dividerRow = []
            for column, value in row.items():
                #checki if column should be ignored

                if column not in ignoredColumns:
                    colWidth = columnData_dict[column]["colWidth"]
                    value_str = self.cutString(value,colWidth)

                    #create the title row if this is the first round
                    if firstRow:
                        title_str = columnData_dict[column]["title"]
                        title_str = self.cutString(title_str, colWidth)
                        titleRow.append(title_str) #titles
                        dividerRow.append("-"*colWidth) #horizontal divider

                    #add each column to the compiledRow
                    compiledRow.append(value_str)

            if firstRow:
                #add the titlerow before any other row
                titleRow_str = divider_str.join(titleRow)
                listForPrint.append(titleRow_str)
                listForPrint.append(horizontalDiv_str.join(dividerRow))
                
            row_str = divider_str.join(compiledRow)
            listForPrint.append(row_str)
        print("\n".join(listForPrint))
        return listForPrint

        
        #create the lines

        #return the list of lines
        
        # _------------------------------------------------------
        # def processTable():
        #     """Cuts/fills the strings for each column""", 

        #     #creates a list of column keys in order
        #     columnOrder =dataType["columns"].keys()
        #     print(columnOrder)


        #     #process each column value to fit the colWidth
        #     formattedList = []

        #     #add the title row:
        #     titleRow = self.__formatRow([data[0]], titles=dataType)
        #     formattedList.append(titleRow.copy())
        #     #process the table
        #     for row in data: 
        #         trimmedRow_dict = self.__formatRow(row)
        #         #append a copy of the row in formatedList
        #         formattedList.append(trimmedRow_dict.copy())

        #     #if enumerated, add

        #     return formattedList

        # def formatRow(rowData):
        #     """Processes the strings per column"""

        #     formattedRow_dict = {}
        #     for column,value in rowData.items():
        #         #if the row is header/title row, then use titles
        #         # if len(titles) != 0:
        #         #     value = titles["titles"][column]

        #         #if value length is longer than colWith limit, then trim
        #         if len(value) > colWidth:
        #             value_str = value[:colWidth]

        #         #else it fills in the empth space
        #         else:
        #             value_str = self.cutString(value,colWidth)
        #         formattedRow_dict[column] = value_str


    def __sectionText(self, data:list, screenWidth:int, frame:str):
        """Prints the list section """

    def __sectionShortCuts(self, data:list, screenWidth:int, frame:str):
        """Prints the list section """

    #===================================================================================
    # the screen printer
    #===================================================================================

    def __printScreen(self, screenData:list, screenWidth: int):
        
        # Types of sections: header, list, text, shortcuts
        # screenData is list of sections, which are dictionaries of section key and data
        # the data are lists of strings usually, or dictionaries if it is a table
        
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
        #Each section will return a list of strings, each being a line for print
        for section in screenData_list:
            for sectionKey, sectionData_list in section.items():
                #the parameters that will go into the screenSelections_dict methods 
                sectionParameters = [sectionData_list, screenWidth, frame_str]
                #run the method with parameters
                screenSections_dict[sectionKey.lower()](*sectionParameters)

        #print the bottom
        print(frameBottom_str)
    
    #===================================================================================
    # Processing methods
    #===================================================================================





    #===================================================================================
    # Methods that compile the screens for print
    #===================================================================================

    def printList(self, data:list, rowLimit:int = 0,colWidth:int = 10, formatTemplate: str = "", keys: bool = False):
        """Prints a given list, can optionally print the key as column title, else it uses the given titles"""
        #get the dataType for 

        screenData = [
            {"header": ["Header of screen"]},
            {"list": data}
        ]

        self.__printScreen(screenData,100)

        # if rowLimit == 0:
        #     rowLimit = len(data)

        # for line in data[:rowLimit]:
        #     row = []
        #     #prints the columns specified in the 'formats' dict
        #     for column in line:
        #         #if value is longer than set limit width, then cut 
        #         colValue = line[column]
        #         row.append(self.cutString(colValue,colWidth))
        #     #joins the columns together with '|' seperator
        #     print(" | ".join(row)) 

            
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