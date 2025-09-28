import requests
from datetime import datetime

#User Date
month = 1
day = 2

#Fetching weather data
def fetch_weather(year):
    date = f"{year}-{month:02d}-{day:02d}"
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 44.5192,
        "longitude": -88.0198,
        "start_date": date,
        "end_date": date,
        "daily": ["temperature_2m_mean", "wind_speed_10m_max", "precipitation_sum"],
        "timezone": "America/Chicago",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
    }

    response = requests.get(url, params=params)
    data = response.json().get("daily", {})
    return data

#Methods for each variable
def avg_temp_years(weather):
    years = [datetime.today().year - i for i in range(1, 6)]
    temps = []
    for j in years:
        daily = fetch_weather(j)
        temp = daily.get("temperature_2m_mean", [])
        if temp:
            temps.append(temp[0])
    return sum(temps) / len(temps) if temps else None


def max_wind_years(weather):
    years = [datetime.today().year - i for i in range(1, 6)]
    winds = []
    for j in years:
        daily = fetch_weather(j)
        wind = daily.get("wind_speed_10m_max", [])
        if wind:
            winds.append(daily["wind_speed_10m_max"][0])
    return max(winds) if winds else None


def sum_precip_years(weather):
    years = [datetime.today().year - i for i in range(1, 6)]
    precips = []
    for j in years:
        daily = fetch_weather(j)
        precip = daily.get("precipitation_sum", [])
        if precip:
            precips.append(daily["precipitation_sum"][0])
    return sum(precips) if precips else None

