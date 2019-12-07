class DateUtil:
    def __init__(self ,datetime:str):
        self.parse(datetime)
        
    def parse(self, datetime:str):
        self.date = self.date_parse(datetime)
        self.time = self.time_parse(datetime)
        self.day = self.day_parse(datetime)
        self.month = self.month_parse(datetime)
        self.year = self.year_parse(datetime)
        self.hour = self.hour_parse(datetime)
        self.minute = self.minute_parse(datetime)
        self.second = self.second_parse(datetime)

    def date_parse(self, datetime:str, format:str = "num"):
        """returns date"""
        return datetime[0:10]

    def day_parse(self, datetime:str, format:str = "num"):
        """returns the day"""
        return datetime[8:10]

    def month_parse(self, datetime:str, format:str = "num"):
        """returns the month"""
        return datetime[5:7]

    def year_parse(self, datetime:str, format:str = "num"):
        """returns the year"""
        return datetime[:4]

    def time_parse(self, datetime:str, format:str = "num"):
        """returns the time"""
        return datetime[-8:]

    def hour_parse(self, datetime:str, format:str = "num"):
        """returns the hour"""
        return datetime[11:13]

    def minute_parse(self, datetime:str, format:str = "num"):
        """returns the minute"""
        return datetime[14:16]
    
    def second_parse(self, datetime:str, format:str = "num"):
        """returns the minute"""
        return datetime[17:]

