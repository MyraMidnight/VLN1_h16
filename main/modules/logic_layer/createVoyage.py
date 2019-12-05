class Create():
    

    def createVoyage(self):
        '''Create a new voyage, voyage contains of two flights with different flight numbers.
            have to get destination that we already fly to, date that the voyage will occur and than when the flight back home to Iceland is '''


        #create voyage make sure to check everything is right 

    # (áfangastaður, dagsetning, brottfaratími frá Íslandi og aftur til baka til Íslands))



        #Get a list of destinations NaN Air flies to

        destination_list = [] # fall sem nær í lista af öllum áfangastöðum sem við förum til
        destination_str = input("Enter the destination for this new voyage: ")

        while destination_str not in destination_list:
            print("Please enter a destination that NaN Air flies to")
            destination_str = input("Enter the destination for this new voyage: ")
        
        

        

        datefromiceland_str = input("Enter the date for the flight from Iceland to {}".format(destination_str))

        #villutékka datefromiceland_str

        eddfromiceland_str = input("Enter the time to departue from Iceland to {}".format(destination_str))


        datebacktoiceland_str = input("Enter the date for the flight from {} to Iceland".format(destination_str))

        #villutékka datetoiceland_str

        eddtoiceland_str = input("Enter the time to departue from {} to Iceland ".format(destination_str))



        # Get a list of all possible planes that are free over the time the voyage occurs
        planetype_str = input("Enter the number of the plane you want to use in this voyage from the plane list: ")

        # Make a flightnumber for both flights, the flight numbers are different depending on the destination and how many other flights have gone to the destination on this same day

        # print all the info about the voyage for the user and ask if the info is correct, if not than edit info, else save to data


