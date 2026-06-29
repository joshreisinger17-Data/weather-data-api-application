import unittest
from datetime import datetime
from weather_data import WeatherData
from weather_analysis import fetch_weather, avg_temp_years, max_wind_years

class Test(unittest.TestCase):
    #test object/argument for tests using class from C1
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
        self.assertGreaterEqual(test_avg_temp, -150)
        self.assertLessEqual(test_avg_temp, 150)

    def test_max_wind_years(self):
        test_max_wind = max_wind_years(self.weather)
        self.assertIsInstance(test_max_wind, (float, int))
        self.assertGreaterEqual(test_max_wind, 0)
        self.assertLessEqual(test_max_wind, 300)

if __name__ == '__main__':
    unittest.main()
