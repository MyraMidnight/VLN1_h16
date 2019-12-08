class Update():

    def updateVoyage(self):
        '''Update and/or put staff in roles in upcoming Voyages'''

        #get list of voyages from data layer
        # the user can choose the voyage he/she wants to update from the list of voyages, the user enters the number of the voyage (flight)

        upcomingVoyage_list = []  #get list from data layer, this is just for now
        numberOfVoyage_int = int(input("Enter the number of the voyage in the list you want to update/change: "))
        theVoyage = upcomingVoyage_list[numberOfVoyage_int]


        # print the info that are currently right for the voyage, if there are any staff members in some roles or if the roles are empty and there needs to fill all the roles
        print(theVoyage)

        # the user inputs the number of the role he/she wants to change/fill.
        roleToChange_int = int(input("Enter the number of the role in the list you want to update/change: "))

        # the user gets a list of all staff members who can play that role and who ara avilable during the voyage's time

        # Get a list of staff members who can do this role from data layer
        rolelist_list = []   #just for now need to get from data layer




        # ask the user if he/she wants to save the changes or if he/she wants to change/fill some other roles
        toChangeOrNotToChange_bool = input("Do you want to save the changes? (y/n) ")
        
        # when he wants to save then save this voyage info in the data layer.
        # if the user wants to quit then no changes were made.

