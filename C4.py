from sqlalchemy import Column, Integer, Float, create_engine
from sqlalchemy.orm import declarative_base

#Base class for ORM
Base = declarative_base()

#Creating a table for weather table
class WeatherRecord(Base):
    __tablename__ = 'weather_record'
    id = Column(Integer, primary_key=True)
    location_latitude = Column(Float)
    location_longitude = Column(Float)
    month = Column(Integer)
    day_of_month = Column(Integer)
    year = Column(Integer)
    avg_temp_F = Column(Float)
    min_temp_F = Column(Float)
    max_temp_F = Column(Float)
    avg_wind_mph = Column(Float)
    min_wind_mph = Column(Float)
    max_wind_mph = Column(Float)
    sum_precip_in = Column(Float)
    min_precip_in = Column(Float)
    max_precip_in = Column(Float)

#Connects SQLite file
engine = create_engine('sqlite:///weather.db')
#Creates table in the DB
Base.metadata.create_all(engine)
