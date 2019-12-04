#model classes
class Voyage:
    def __init__(self, captainId, copilots, headAttendantId, 
    flightAttendants, flightOut, flightIn, destination, dateOut, dateIn):
        self.captainId = captainId
        self.copilots = copilots
        self.headAttendantId = headAttendantId
        self.flightAttendants = flightAttendants
        self.flightIn = flightIn
        self.flightOut = flightOut
        self.destination = destination
        self.dateOut = dateOut
        self.dateIn = dateIn
    
class Staff:

    def __init__(self, name, socialId, address, phoneHome, phoneMobile, email):
        self.name = name
        self.socialId = socialId
        self.address = address
        self.phoneHome = phoneHome
        self.phoneMobile = phoneMobile
        self.email = email

class Pilot(Staff):

    def __init__(self, name, socialId, address, phoneHome, phoneMobile, email, role, rank, license):
        Staff.__init__(self, name, socialId, address, phoneHome, phoneMobile, email)
        self.role = role
        self.rank = rank
        self.license = license

class Destination:
    
    def __init__(self, id, country, airport, flightTime, flightDistance, contact, contactPhone):
        self.id = id
        self.country = country
        self.airport = airport
        self. flightTime = flightTime
        self.flightDistance = flightDistance
        self.contact = contact
        self.contact = contactPhone
