class WeatherData:
    def __init__(self, latitude, longitude, month, day, year):
        #Provided by User
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.year = year

        #Provided by Weather API
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None
        self.avg_wind = None
        self.min_wind = None
        self.max_wind = None
        self.avg_precip = None
        self.min_precip = None
        self.max_precip = None

import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"

from datetime import datetime

latitude  = 44.5192
longitude = -88.0198
month = 1
day = 2
temps = []
winds = []
precips = []

current_year = datetime.today().year

for i in range(1, 6):
    year = current_year - i
    date_str = f"{year}-{month}-{day}"

    params = {
        "latitude": 44.5192,
        "longitude": -88.0198,
        "start_date": date_str,
        "end_date": "date_str",
        "daily": ["temperature_2m_mean", "wind_speed_10m_max", "precipitation_sum"],
        "timezone": "America/Chicago",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.daily

    try:
        temp = daily.Variables(0).ValuesAsNumpy())[0]
        wind = daily.Variables(1).ValuesAsNumpy()[0]
        precip = daily.Variables(2).ValuesAsNumpy()[0]

        temps.append(temp)
        winds.append(wind)
        precips.append(precip)

        print(f"{date_str}, Temp: {temp}\N{DEGREE SIGN}F, Wind: {wind} mph, Precip: {precip} inches")

    except Exception as e:
        print(f"Error retrieving data for {date_str}: {e}")

    if temps:
        avg_temp = sum(temps) / len(temps)
        max_wind = max(winds)
        total_precip = sum(precips)

        print("\n5-Year Summary for January 2nd:")
        print(f"Average Temperature: {avg_temp:.2f}\N{DEGREE SIGN}F")
        print(f"Max Wind Speed: {max_wind:.2f} mph")
        print(f"Total Precipitation: {total_precip:.2f} inches")
    else:
        print("No data available!")


    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}

    daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
    daily_data["precipitation_sum"] = daily_precipitation_sum

    daily_dataframe = pd.DataFrame(data = daily_data)
    print("\nDaily data\n", daily_dataframe)