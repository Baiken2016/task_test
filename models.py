from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date


class OwnerData(Base):
    __tablename__ = 'owner_data'
    owner_id = Column(Integer, primary_key=True)
    owner_name = Column(String, nullable=False)
    registration_address = Column(String, nullable=False)
    actual_address = Column(String)


class CarModels(Base):
    __tablename__ = 'car_models_data'
    car_id = Column(Integer, primary_key=True)
    car_model = Column(String, nullable=False)
    car_height = Column(Float, nullable=False)
    car_width = Column(Float, nullable=False)
    car_length = Column(Float, nullable=False)
    car_speed = Column(Float, nullable=False)


class TechPassport(Base):
    __tablename__ = 'tech_passport_data'
    passport_id = Column(Integer, primary_key=True)
    registration_id = Column(String, nullable=False)
    car_id = Column(Integer, ForeignKey(CarModels.car_id))
    date_of_issue = Column(Date, nullable=False)
    car_color = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey(OwnerData.owner_id))
