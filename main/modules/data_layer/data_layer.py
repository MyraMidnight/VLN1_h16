import os
import csv

class IOAPI:

    #opens all files in STUDENTDATA
    def opener(self,askedFile):
        #moves presence over to STUDENTDATA file
        os.chdir('main/data/STUDENTDATA')
        filePackage = []
        #goes through every filename in current directory(now STUDENTDATA)
        for filename in os.listdir(os.getcwd()):
            #opens every file in read mode
            if filename == askedFile:
                with open(filename,'r', encoding="utf-8") as file:
                    #uses csv.dictreader which is an inbuilt function that reads every line and converts them into OrderedDicts
                    #the function gets its keys from the first line of the file, an ordered dict is a tuple containing a list
                    #of tuples, those tuples being the key:value items
                    reader = csv.DictReader(file)
                    #collects everything together
                    for row in reader:
                        #change all the ordereddicts into normal dicts as tuples are immutable and we need to be able to edit them
                        temp_dict = dict(row)
                        filePackage.append(temp_dict)
                    #adds the current files list of dicts into the filePackage as a value of the key of its filename
                    file.close() 
                    #code example you can run to better understand the structure of filePackage
                    '''
                    for x in filePackage:
                        print(x)
                        print('-----')
                    '''
                    return filePackage
    

    #any edited filePackage will be sent here, whether it was updated or appended to
    def appender(self,fileName,filePackage):
        csv_columns = [key for key in filePackage]
        #opens the file with filename in write mode
        with open(fileName,'a',newline='') as file:
            #DictWriter is an inbuilt csv function that takes a filestream and fieldnames as mandatory parameters
            #from there you can make it write a header based on the fieldnames and makte it write a row
            #into the file where it takes a dictionary and breaks it down to write to a line
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writerow(filePackage)
    
    def updater(self,fileName,filePackage):
        csv_columns = [key for key in filePackage[0]]
        print(csv_columns)
        #opens the file with filename in write mode
        with open(fileName,'w',newline='',encoding='utf-8') as file:
            #DictWriter is an inbuilt csv function that takes a filestream and fieldnames as mandatory parameters
            #from there you can make it write a header based on the fieldnames and makte it write a row
            #into the file where it takes a dictionary and breaks it down to write to a line
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            #writes the header with the keys
            writer.writeheader()
            for line in filePackage:
                writer.writerow(line)

    


#code example on how to use overWriter
#package = IOAPI().opener('Crew.csv')
#for x in package:
#    print(x)
#package[5] = {'ssn': 'test', 'name': 'test test', 'role': 'test', 'rank': 'test test', 'licence': 'test/test', 'address': 'test 25', 'phonenumber': 'test'}
#test_dict = {'ssn': 'test', 'name': 'test test', 'role': 'test', 'rank': 'test test', 'licence': 'test/test', 'address': 'test 25', 'phonenumber': 'test'}
#IOAPI().updater('Crew.csv',package)
#IOAPI().appender('Crew.csv',test_dict)