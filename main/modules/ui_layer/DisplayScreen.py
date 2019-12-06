
class DisplayScreen:
    def __init__(self):
        self.stringLimits = { #string length limit
            "crew": {'ssn': 10, 'name': 20, 'role': 10, 'rank': 15, 'licence': 8, 'address': 20, 'phonenumber': 14},
        }

    def cutString(self, string, limit:int = 10):
        """Creates a string that is of set length, if string was cut short then it adds dots, else it fills with spaces""" 
        if len(string) > limit:
            #cut it to fit the limit
            cutString = string[:limit] 
            newString = cutString[:-3] + "..." #replace last 3 letters with dots to indicate it was cut short
            return newString
        else: 
            newString = string.ljust(limit)
            return newString
  
# {'ssn': '1103647756', 'name': 'Wilma Horne', 'role': 'Cabincrew', 'rank': 'Flight Attendant', 'licence': 'N/A', 'address': 'Fellsmúli 25', 'phonenumber': '8998825'}
# {'ssn': '2807755841', 'name': 'Bernard Carr', 'role': 'Cabincrew', 'rank': 'Flight Attendant', 'licence': 'N/A', 'address': 'Fellsmúli 26', 'phonenumber': '8998826'}
    def printList(self, data:list, colLimit:int = 10):
        #create the header row (print the keys)
        headerKeys = []
        print()
        for column in data[0]:
            headerKeys.append(self.cutString(column,colLimit))
        headerRow = " | ".join(headerKeys)
        print(headerRow)
        print("-"*len(headerRow))
        #loop through each line of data
        for line in data:
            row = []
            #prints the columns specified in the 'formats' dict
            for column in line:
                #if value is longer than set limit width, then cut 
                colValue = line[column]
                row.append(self.cutString(colValue,colLimit))
            #joins the columns together with '|' seperator
            print(" | ".join(row)) 

            
    def printListFormat(self, data: list, formatTemplate: str = "" ):
        """Prints data lists, takes in a list of dictionaries\n
            optional: can add 'type' parameter for specific format.\n
            Types: employees, cabincrew, pilots, flightattendants, planes, destinations
        """
        defaultStringLimit = 10
        templates = { #what columns should be printed, first item is reference to 
            "employees": { 
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
             }
        }

        if formatTemplate in templates:
            template = templates[formatTemplate]
            #create the header row (print the keys)
            headerKeys = []
            print()
            for column in template["columns"]:
                headerKeys.append(self.cutString(column,self.stringLimits[template["dataType"]][column]))
            headerRow = " | ".join(headerKeys)
            print(headerRow)
            print("-"*len(headerRow))
            #loop through each line of data
            for line in data:
                row = []
                #prints the columns specified in the 'formats' dict
                for column in template["columns"]:
                    #if value is longer than set limit width, then cut 
                    colValue = line[column]
                    row.append(self.cutString(colValue,self.stringLimits[template["dataType"]][column]))
                #joins the columns together with '|' seperator
                print(" | ".join(row)) 
        else: 
            self.printList(data,defaultStringLimit)