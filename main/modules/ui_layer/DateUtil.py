import datetime

class DateUtil:
    def __init__(self ,datetime:str = ""):
        """automatically parses the datetime.isoformat string when initiated"""
        if len(datetime) != 0:
            self.parse(datetime)
        
    def parse(self, datetime:str):
        """parses a datetime (isoformat) string into accessable parts, can access atributes such as date, time, day, month..."""
        self.date = self.date_parse(datetime)
        self.time = self.time_parse(datetime)
        self.day = self.day_parse(datetime)
        self.month = self.month_parse(datetime)
        self.year = self.year_parse(datetime)
        self.hour = self.hour_parse(datetime)
        self.minute = self.minute_parse(datetime)
        self.second = self.second_parse(datetime)

    def date_parse(self, datetime:str):
        """returns date"""
        return datetime[0:10]

    def day_parse(self, datetime:str):
        """returns the day"""
        return datetime[8:10]

    def month_parse(self, datetime:str, name:str = ""):
        """returns the month, optional parameter will return month names instead of number"""
        #optional print formats: name
        month = datetime[5:7]
        monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        if len(name) != 0:
            #returns the month as name
            if month[0] == "0": #trims off the front 0
                month = month[1:]
            return monthNames[int(month)-1]
        else:
            #returns the month as number
            return month

    def year_parse(self, datetime:str):
        """returns the year"""
        return datetime[:4]

    def time_parse(self, datetime:str):
        """returns time string HH:MM:SS"""
        return datetime[-8:]

    def hour_parse(self, datetime:str):
        """returns the hour"""
        return datetime[11:13]

    def minute_parse(self, datetime:str):
        """returns the minute"""
        return datetime[14:16]
    
    def second_parse(self, datetime:str):
        """returns the minute"""
        return datetime[17:]
    
    def updateTime(self, date:str, time:str):
        """Updates the time of a given datetime string"""
        return date[:11] + time

    def createObject(self):
        """Creates and returns a datetime object"""
        return datetime().datetime(self.year,self.month,self.day,self.hour,self.minute,self.second)