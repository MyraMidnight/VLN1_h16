import os
import csv

class IOAPI:

    #opens all files in STUDENTDATA
    def Opener(self):
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
    


IOAPI().Opener()