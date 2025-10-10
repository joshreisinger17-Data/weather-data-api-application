import unittest
from datetime import datetime
from C2 import fetch_weather, avg_temp_years, max_wind_years

#dummy class for tests
class Weather:
    def __init__(self, latitude, longitude, month, day):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day

class Test(unittest.TestCase):
    #dummy object/argument for test
    def dummy(self):
        self.weather = Weather(44.5192, -88.0198, 1, 2)

    #Shows our fetch data is non-empty
    def test_fetch_weather(self):
        year = datetime.today().year
        weather_data = fetch_weather(self.weather, year)
        self.assertIsNotNone(weather_data)
        self.assertTrue(len(weather_data) > 0)

    def test_avg_temp_years(self):
        test_avg_temp = avg_temp_years(self.weather)
        self.assertIsInstance(test_avg_temp, (float, int))

    def test_max_wind_years(self):
        test_max_wind = max_wind_years(self.weather)
        self.assertIsInstance(test_max_wind, (float, int))

if __name__ == '__main__':
    unittest.main()
