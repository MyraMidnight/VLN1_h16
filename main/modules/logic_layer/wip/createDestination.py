class Create():


    def createDestination(self):
        #Create a new destination. Requests input for destinationLand, destinationAirport, destinationFlightTime, 
        # destinationDistance, destinationContactPerson and destinationEmergencyPhone.


        #Get the new destination
        destination_land_str = input("Enter the country where the new destination is located: ")

        #while new_Destination_str not in destination_list:
        #    print("This destination is not new!")
        #    print("b for back")
        #    new_Destination_str = input("Enter the new destination: ")

        # Checks whether or not the destination consists of only alphabetical characters (make sure the input is valid)
        while not destination_land_str.isalpha():    
            print("Please input a valid country")
            destination_land_str = input("Enter the country where the new destination is located: ")
        




        # Get the airport for the new destination
        airport_str = input("Enter the new airport: ")

        # Checks whether or not the airport consists of only alphabetical characters (make sure the input is valid)
        while not airport_str.isalpha():    
            print("Please input a valid airport")
            airport_str = input("Enter the new airport: ")
        




        # Get the time it takes to fly to the new airport
        flighttime_str = input("Enter the flight time (the time it takes to fly from Iceland to {}, {}). Please input the time on the format hh:mm.".format(destination_land_str,airport_str))

        while ":" not in  flighttime_str:
            print("Please input a valid flight time")
            flighttime_str = input("Enter the flight time (the time it takes to fly from Iceland to {}, {}). Please input the time on the format hh:mm.".format(destination_land_str,airport_str))
        

        while flighttime_str.isalpha():
            print("Please input a valid flight time")
            flighttime_str = input("Enter the flight time (the time it takes to fly from Iceland to {}, {}). Please input the time on the format hh:mm.".format(destination_land_str,airport_str))
        



        # Get the distance from Iceland to the new airport
        distance_int = input("Enter the distance from Iceland to {} (meters): ".format(destination_land_str))

        while distance_int.isdigit():
            print("Please enter a valid distance")
            distance_int = input("Enter the distance from Iceland to {} (meters): ".format(destination_land_str))
        
        while distance_int < 0:
            print("Please enter a valid distance")
            distance_int = input("Enter the distance from Iceland to {} (meters): ".format(destination_land_str))




        # Get the contact persons name
        contact_person_str = input("Enter the name of the contact person for the new destination: ")

        #Checks whether or not user the input contains both the surname and lastname
        while " " not in contact_person_str:  
            print("Please input both surname and lastname")
            contact_person_str = input("Enter the name of the contact person for the new destination: ")

        # Checks whether or not the contact persons name consists of only alphabetical characters
        while not contact_person_str.isalpha():    
            print("Please input correct surname and lastname")
            contact_person_str = input("Enter the name of the contact person for the new destination: ")
        


        # Get the contact persons emergency phone number

        emergency_phone_str = input("Enter the emergency phone number for the new destination: ")
        while len(emergency_phone_str) != 7 or not emergency_phone_str.isdigit():
            print("Please enter valid phonenumber")
            emergency_phone_str = input("Enter the emergency phone number for the new destination: ")
