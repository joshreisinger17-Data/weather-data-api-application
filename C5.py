from os.path import exists

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from C4 import WeatherRecord

#Connects to the DB
engine = create_engine('sqlite:///weather.db', future=True)
SessionLocal = sessionmaker(bind=engine)

#Input User Data from chosen location
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

if __name__ == '__main__':
    session = SessionLocal()
    try:
        exists = session.query(WeatherRecord).filter_by(
            location_latitude = record.location_latitude,
            location_longitude = record.location_longitude,
            month = record.month,
            day_of_month = record.day_of_month,
            year = record.year,
        ).first()

        if not exists:
            session.add(record)
            session.commit()
            print("Inserted record.")

        else:
            print("Record already exists.")
    finally:
        session.close()