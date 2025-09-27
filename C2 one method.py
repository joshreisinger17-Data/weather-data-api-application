import requests
from datetime import datetime

# Location
latitude = 44.5192
longitude = -88.0198
month = 1
day = 2

# Lists for Variables
temps = []
winds = []
precips = []

current_year = datetime.today().year

for i in range(1,6):
    year = current_year - i
    date = f"{year}-{month:02d}-{day:02d}"

    url = (
        f"https://archive-api.open-meteo.com/v1/archive"
        )
    params = {
        "latitude": 44.5192,
        "longitude": -88.0198,
        "start_date": "2025-09-10",
        "end_date": "2025-09-24",
        "daily": ["temperature_2m_mean", "wind_speed_10m_max", "precipitation_sum"],
        "timezone": "America/Chicago",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
    }

    # GET request using parameters
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        try:
            daily = data["daily"]
            temp = daily["temperature_2m_mean"][0]
            wind = daily["wind_speed_10m_max"][0]
            precip = daily["precipitation_sum"][0]

            temps.append(temp)
            winds.append(wind)
            precips.append(precip)

        except KeyError:
            print("No weather data available!")
    else:
        print("Request failed!")

# Print results
if len(temps) > 0:
    avg_temp = sum(temps) / len(temps)
    max_wind = max(winds)
    total_precip = sum(precips)

    print(f"Weather data: (Green Bay, Wisconsin) Latitude:{latitude}, Longitude:{longitude} Date:{month}/{day}/2020-20205 (From last Five years)")
    print(f"Average Temperature: {avg_temp: .2f}\u00b0F")
    print(f"Max Wind: {max_wind: .2f} mph")
    print(f"Total Precipitation: {total_precip: .2f} inches")
else:
    print("No weather data available!")

