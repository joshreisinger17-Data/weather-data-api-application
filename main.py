from C1 import WeatherData
from C2 import avg_temp_years, max_wind_years, sum_precip_years

#Instance of class created in C1
weather_data = WeatherData(42.8865, -78.8784, 12, 25, 2023)

#Calling Methods from C2
avg_temp = avg_temp_years(weather_data)
max_wind = max_wind_years(weather_data)
sum_precip = sum_precip_years(weather_data)

#prints results from calls
print(f"{weather_data.latitude, weather_data.longitude} on {weather_data.month:02d}-{weather_data.day:02d}.")
print(f"Average Temperature: {avg_temp:.2f}\u00b0F")
print(f"Max Wind: {max_wind:.2f} mph")
print(f"Total Precipitation: {sum_precip:.2f} inches")





