from sqlalchemy import  Column, String, Integer, Float

from db_config.database_config import  Base

class VehicleImages(Base):
    __tablename__="vehicle_image"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Vehicle(Base):
    __tablename__="vehicle"

    id = Column(String, primary_key=True, index=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    mileage= Column(Float, nullable=False)
    price = Column(Float, nullable=False)