
class DisplayScreen:

    def cutString(self, string, limit):
        """Creates a string that is of set length, if string was cut short then it adds dots, else it fills with spaces"""

    def printList(self, data: list, dataType: str = "" ):
        """Prints data lists, takes in a list of dictionaries\n
            optional: can add 'type' parameter for specific format.\n
            Types: employees, cabincrew, pilots, flightattendants, planes, destinations
        """
        #type and dictionary of columns to display and widht limit
        formats = {
            "employees": {
                "name": 20, "ssn": 13, "rank": 20, "licence": 8, "address": 18, "phonenumber": 9
            },
            "pilots": {
                "name": 20, "ssn": 13, "rank": 20, "licence": 8, "address": 18, "phonenumber": 9
            },
            "cabincrew": {
                "name": 18, "ssn": 13, "rank": 20, "address": 20, "phonenumber": 9
            }
        }

        
# {'ssn': '1103647756', 'name': 'Wilma Horne', 'role': 'Cabincrew', 'rank': 'Flight Attendant', 'licence': 'N/A', 'address': 'Fellsmúli 25', 'phonenumber': '8998825'}
# {'ssn': '2807755841', 'name': 'Bernard Carr', 'role': 'Cabincrew', 'rank': 'Flight Attendant', 'licence': 'N/A', 'address': 'Fellsmúli 26', 'phonenumber': '8998826'}
 
        if dataType in formats:
            #create the header row (print the keys)
            for keys in data[0]:
                
            #loop through each line of data
            for line in data:
                row = []
                #prints the columns specified in the 'formats' dict
                for column,limit in formats[dataType].items():
                    #if value is longer than set limit width, then cut 
                    colValue = line[column]
                    if len(colValue) > limit:
                        #cut it to fit the limit
                        cutValue = colValue[:limit] 
                        newValue_str = cutValue[:-3] + "..." #replace last 3 letters with dots to indicate it was cut short
                        row.append(newValue_str)
                    else: 
                        newValue_str = colValue.ljust(limit)
                        row.append(newValue_str)
                #joins the columns together with '|' seperator
                print(" | ".join(row)) 

            # title = formats[dataType]
            # for line in data:
            #     #print the title
            #     print(columnString.format(line[title][:18]), end="")
            #     #then loop through and print rest
            #     for key, value in line.items():
            #         if key != formats[dataType]:
            #             print(columnString.format(value[:18]), end="") 
            #     #break
            #     print()
        else: 
            for line in data:
                for key,value in line.items():
                    print("\t{}: {}".format(key,value))

        
        
