import unittest
from datetime import datetime
from C1 import WeatherData
from C2 import fetch_weather, avg_temp_years, max_wind_years

class Test(unittest.TestCase):
    #dummy object/argument for test using class from C1
    def setUp(self):
        self.weather = WeatherData(44.5192, -88.0198, 1, 2, year = datetime.today().year)

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
