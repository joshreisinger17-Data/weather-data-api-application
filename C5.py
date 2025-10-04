from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from C4 import WeatherRecord

#Connects to DB
engine = create_engine('sqlite:///weather.db', future=True)
SessionLocal = sessionmaker(bind=engine)

#Opens session
session = SessionLocal()

#Input User Data
record = WeatherRecord(
    location_latitude = 44.5192,
    location_longitude = -88.0198,
    month = 1,
    day_of_month = 2,
    year = 2025,
    avg_temp_F = 0.00,
    min_temp_F = None,
    max_temp_F = None,
    avg_wind_mph = None,
    min_wind_mph = None,
    max_wind_mph = 25.64,
    sum_precip_in = 12.80,
    min_precip_in = None,
    max_precip_in = None
)