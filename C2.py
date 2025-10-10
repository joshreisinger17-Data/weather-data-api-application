import requests
from datetime import datetime

#Fetching weather data from API
def fetch_weather(weather, year):
    date = f"{year}-{weather.month:02d}-{weather.day:02d}"
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": weather.latitude,
        "longitude": weather.longitude,
        "start_date": date,
        "end_date": date,
        "daily": ["temperature_2m_mean", "wind_speed_10m_max", "precipitation_sum"],
        "timezone": "America/Chicago",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
    }

    response = requests.get(url, params=params, timeout=20)
    data = response.json().get("daily", {})
    return data

#Methods for each variable
def avg_temp_years(weather):
    years = [datetime.today().year - i for i in range(1, 6)]
    temps = []
    for j in years:
        daily = fetch_weather(weather, j)
        temp = daily.get("temperature_2m_mean", [])
        if temp:
            temps.append(temp[0])
    mean_temp = (sum(temps) / len(temps)) if temps else None
    weather.avg_temp = mean_temp
    return mean_temp

def max_wind_years(weather):
    years = [datetime.today().year - i for i in range(1, 6)]
    winds = []
    for j in years:
        daily = fetch_weather(weather, j)
        wind = daily.get("wind_speed_10m_max", [])
        if wind:
            winds.append(wind[0])
    max_wind = max(winds) if winds else None
    weather.max_wind = max_wind
    return max_wind

def sum_precip_years(weather):
    years = [datetime.today().year - i for i in range(1, 6)]
    precips = []
    for j in years:
        daily = fetch_weather(weather, j)
        precip = daily.get("precipitation_sum", [])
        if precip:
            precips.append(precip[0])
    sum_precip = sum(precips) if precips else None
    weather.sum_precip = sum_precip
    return sum_precip



