"""В этом файле хранятся pydantic модели таблицы по данным о моделях машин
для валидации входных и выходных данных"""
from pydantic import BaseModel
from datetime import date


class CarCreate(BaseModel):
    """
    Pydantic модель для передачи данных при создании
    новой модели автомобиля в базе данных, в таблице CarModels

    Атрибуты:
        car_id (int): уникальный идектификатор автомобиля
        car_model (str): название и модель автомобиля
        car_height (float): высота автомобиля
        car_width (float): ширина автомобиля
        car_length (float): длина автомобиля
        car_speed (float): максимальная скорость автомобиля (км/час)
        date_of_creation (date): дата выпуска автомобиля (формат даты: YYYY-MM-DD)
    """
    car_id: int
    car_model: str
    car_height: float
    car_width: float
    car_length: float
    car_speed: float
    date_of_creation: date


class CarUpdate(BaseModel):
    """
    Pydantic модель для передачи обновленных данных
    в базу данных, в таблице CarModels

    Атрибуты:
        car_id (int): уникальный идектификатор автомобиля
        car_model (str): название и модель автомобиля
        car_height (float): высота автомобиля
        car_width (float): ширина автомобиля
        car_length (float): длина автомобиля
        car_speed (float): максимальная скорость автомобиля (км/час)
        date_of_creation (date): дата выпуска автомобиля (формат даты: YYYY-MM-DD)
    """
    car_id: int
    car_model: str
    car_height: float
    car_width: float
    car_length: float
    car_speed: float
    date_of_creation: date


class CarDelete(BaseModel):
    """
    Pydantic модель для запроса на удаление записи из базы данных,
    таблицы CarModels по идентификатору автомобиля

    Атрибуты:
        car_id (int): уникальный идектификатор автомобиля
    """
    car_id: int
