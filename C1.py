class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
        #Provided by User
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        #Provided by Weather API
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None
        self.avg_wind = None
        self.min_wind = None
        self.max_wind = None
        self.sum_precip = None
        self.min_precip = None
        self.max_precip = None