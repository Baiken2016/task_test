"""В данном файле хранятся модели таблиц для хранения данных в postgresql.
   Файл содержит 3 модели:
   OwnerData: модель представляет данные о владельце авто
   CarModels: модель представляет данные о моделяех машины
   TechPassport: модель представляет данные о тех пасспортах"""
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date

Base = declarative_base


class OwnerData(Base):
    """Здесь хранятся личный ID владельца, его ФИО,
    адрес регистрации местожительства, актуальный адрес проживания"""

    __tablename__ = 'owner_data'
    owner_id = Column(Integer, primary_key=True)
    owner_name = Column(String, nullable=False)
    registration_address = Column(String, nullable=False)
    actual_address = Column(String)


class CarModels(Base):
    """Здесь хранится ID модели, название модели,
    высота, ширина, длина и скорость машины, и дата производства"""

    __tablename__ = 'car_models_data'
    car_id = Column(Integer, primary_key=True)
    car_model = Column(String, nullable=False)
    car_height = Column(Float, nullable=False)
    car_width = Column(Float, nullable=False)
    car_length = Column(Float, nullable=False)
    car_speed = Column(Float, nullable=False)
    date_of_creation = Column(Date, nullable=False)


class TechPassport(Base):
    """Здесь хранится ID пасспорта, регистрационный номер машины,
    ID модели машины, дата регистрации пасспорта, цвет машины, ID ладельца"""

    __tablename__ = 'tech_passport_data'
    passport_id = Column(Integer, primary_key=True)
    registration_id = Column(String, nullable=False)
    car_id = Column(Integer, ForeignKey(CarModels.car_id))
    date_of_issue = Column(Date, nullable=False)
    car_color = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey(OwnerData.owner_id))
