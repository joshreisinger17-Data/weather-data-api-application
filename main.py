from C1 import WeatherData
from C2 import avg_temp_years, max_wind_years, sum_precip_years

#Instance of class created in C1
weather_data = WeatherData(42.8865, -78.8784, 12, 25, 2023)

#Calling Methods from C2
avg_temp = avg_temp_years(weather_data)
max_wind = max_wind_years(weather_data)
sum_precip = sum_precip_years(weather_data)

#prints results from calls
print(avg_temp)
print(max_wind)
print(sum_precip)





