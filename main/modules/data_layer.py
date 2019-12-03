import os
import csv

class IOAPI:

    #connection point of LLAPI and IOAPI
    #filePackage defaults to None when you're fetching
    def dataPipe(self,option,filePackage = None):
        #sends to overWriter, no return
        if option == "Return":
            IOAPI().overWriter(filePackage)
        #sends to opener and returns the new package
        elif option == "Fetch":
            filePackage = IOAPI().opener()
            return filePackage

    #opens all files in STUDENTDATA
    def opener(self):
        #moves presence over to STUDENTDATA file
        os.chdir('main/data/STUDENTDATA')
        filePackage = {}
        #goes through every filename in current directory(now STUDENTDATA)
        for filename in os.listdir(os.getcwd()):
            #opens every file in read mode
            with open(filename,'r') as file:
                #uses csv.dictreader which is an inbuilt function that reads every line and converts them into OrderedDicts
                #the function gets its keys from the first line of the file, an ordered dict is a tuple containing a list
                #of tuples, those tuples being the key:value items
                reader = csv.DictReader(file)
                temp_list = []
                #index 0 will store the 'ValidTag' just as a True or False
                temp_list.append(True)
                #collects everything together
                for row in reader:
                    #change all the ordereddicts into normal dicts as tuples are immutable and we need to be able to edit them
                    temp_dict = dict(row)
                    temp_list.append(temp_dict)
                #adds the current files list of dicts into the filePackage as a value of the key of its filename
                filePackage[filename] = temp_list
        
        #code example you can run to better understand the structure of filePackage 
        '''
        for key, value in filePackage.items():
            print(key)
            for x in value:
                print(x)
            print('-----')
        '''

        return filePackage

    #any edited filePackage will be sent here, whether it was updated or appended to
    def overWriter(self,filePackage):
        #go through all the file contents
        for filename, contents in filePackage.items():
            #checks the validTag
            if contents[0] == False:
                #fetches the column names for the csv file by getting the keys from the first dict
                csv_columns = [key for key in contents[1]]
                #opens the file with filename in write mode
                with open(filename,'w',newline='') as file:
                    #DictWriter is an inbuilt csv function that takes a filestream and fieldnames as mandatory parameters
                    #from there you can make it write a header based on the fieldnames and makte it write a row
                    #into the file where it takes a dictionary and breaks it down to write to a line
                    writer = csv.DictWriter(file, fieldnames=csv_columns)
                    #writer writes the header where it puts the fieldnames like all csv files
                    writer.writeheader()
                    #go through the contents after validtag(as validtag is index 0) and write all the dicts into lines
                    for x in range(1,len(contents)):
                        writer.writerow(contents[x])


#code example on how to use overWriter
'''
package = IOAPI().opener()
package['Crew.csv'][0] = False
package['Crew.csv'][1]['ssn'] = 'Testing overWriter'
package['Crew.csv'][1]['name'] = 'feel free'
package['Crew.csv'][1]['role'] = 'to delete'
package['Crew.csv'][1]['rank'] = 'this line'
package['Crew.csv'][1]['licence'] = 'if I forget to'
IOAPI().overWriter(package)
'''