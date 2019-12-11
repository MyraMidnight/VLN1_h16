import os
class PrintHandler:
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
                    'licence': {"colWidth": 15, "title": "Licence"},
                    'address': {"colWidth": 20, "title": "Address"},
                    'phonenumber': {"colWidth": 14, "title": "Phone"},
                    'email': {"colWidth": 8, "title": "email"}
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
                    "flightDuration": {"colWidth": 20, "title": "traveltime"}

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
        self.__currentSections = []
        self.__settings = {}
        self.__terminalSize = self.__getTerminalSize()
    
    def __getTerminalSize(self):
        width ,height= os.get_terminal_size()
        return {"height": height, "width": width}

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

            #checks if all the keys in data are in existing DataType
            # it can contain less keys (for cases of old data with missing columns)
            if all(column in data[0] for column in columns):
                dataForReturn = {dataType: self.__dataTypes[dataType].copy()}
                dataTypeColumns = dataForReturn[dataType]["columns"]
                print(dataForReturn)

                #check if any extra columns in the given data
                for key in data[0].keys():
                    #create the column for the dataType dict
                    if key not in dataTypeColumns.keys():
                        dataTypeColumns[key] = {"colWidth":colWidth, "title":key}

                # return the DataType 
                return dataForReturn

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

    def __sectionHeader(self, data:list):
        """Prints the header section"""
        self.__currentSections.append(data)

    def __sectionList(self, data:list, numList:bool = False):
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

        #----------------------------------------------
        #Enumerated lists

        if numList:
            enumeratedList = []
            rowCounter_int = 0
            choiceColWidth = 5

            #add the space or number to the line
            for line in listForPrint[:2]:
                #first two lines are not counted
                line = " "*choiceColWidth + line
                enumeratedList.append(line)
            for num, line in enumerate(listForPrint[2:],1):
                choiceIndex = "{})".format(str(num))
                line = choiceIndex.ljust(5) + line
                enumeratedList.append(line)

            self.__currentSections.append(enumeratedList)
        else:           
            self.__currentSections.append(listForPrint)

    def __sectionText(self, data:list):
        """Prints the list section """
        compiledParagraphs = []
        for paragraph in data:
            compiledParagraphs.append(paragraph)
            compiledParagraphs.append("")
            
        self.__currentSections.append(compiledParagraphs)

    def __sectionShortCuts(self, data:list):
        """Prints the list section """
        shortCuts = " - ".join(data)

        self.__currentSections.append([shortCuts])


    def __sectionOptions(self, data:list):
        """Prints a enumerated list"""
        #just uses the sectionList method, with added enumeration
        self.__sectionList(data, numList=True)

    #===================================================================================
    # the section handler (compiles the sections)
    #===================================================================================

    def sectionHandler(self, sectionData:list):
        # Types of sections: header, list, text, shortcuts
        # sectionData is list of sections, which are dictionaries of section key and data
        # the data are lists of strings usually, or dictionaries if it is a table
        
        #the actual sectionData given in parameters
        sectionData_list = sectionData

        #print handler
        screenSections_dict = {
            "header": self.__sectionHeader,
            "list": self.__sectionList,
            "text": self.__sectionText,
            "shortcuts": self.__sectionShortCuts,
            "options": self.__sectionOptions
        }



        #print the body of frame
        #Each section will return a list of strings, each being a line for print
        for section in sectionData_list:
            for sectionKey, sectionData_list in section.items():
                #the parameters that will go into the screenSelections_dict methods 
                sectionParameters = [sectionData_list]
                #run the method with parameters
                listForPrint = screenSections_dict[sectionKey.lower()](*sectionParameters)
            

        #print the bottom
        return self.__currentSections
