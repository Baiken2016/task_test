"""В этом файле хранятся pydantic модели таблицы по данным о моделях машин
для валидации входных и выходных данных"""

from pydantic import BaseModel
from datetime import date


class CarCreate(BaseModel):
    car_id: int
    car_model: str
    car_height: float
    car_width: float
    car_length: float
    car_speed: float
    date_of_creation: date


class CarUpdate(BaseModel):
    car_id: int
    car_model: str
    car_height: float
    car_width: float
    car_length: float
    car_speed: float
    date_of_creation: date


class CarDelete(BaseModel):
    car_id: int
