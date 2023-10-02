"""В этом файле хранятся pydantic модели таблицы о тех пасспаортах
для валидации входных и выходных данных"""

from datetime import date
from pydantic import BaseModel


class PassportCreate(BaseModel):
    """
    Pydantic модель для передачи данных при создании новой записи
    в базу данных, в таблице TechPassport

    Атрибуты:
        passport_id (int): уникальный идентификатор пасспорта
        registration_id (str): гос. номер автомобиля (пример: 123AAA01)
        car_id (int): идентификатор модели автомобиля (берется из таблицы CarModels)
        date_of_issue (date): дата выпуска пасспорта (формат даты: YYYY-MM-DD)
        car_color (str): цвет автомобиля
        owner_id (int): идентификатор владельца автомобиля (берется из таблицы OwnerData)
    """
    passport_id: int
    registration_id: str
    car_id: int
    date_of_issue: date
    car_color: str
    owner_id: int


class PassportDelete(BaseModel):
    """
    Pydantic модель для запроса на удаление записи из базы данных,
    таблицы TechPassport по идентификатору тех. пасспорта

    Атрибуты:
        passport_id (int): уникальный идентификатор пасспорта
    """
    id: int


class PassportUpdate(BaseModel):
    """
    Pydantic модель для передачи обновленных данных
    в базу данных, в таблице TechPassport

    Атрибуты:
        passport_id (int): уникальный идентификатор пасспорта
        registration_id (str): гос. номер автомобиля (пример: 123AAA01)
        car_id (int): идентификатор модели автомобиля (берется из таблицы CarModels)
        date_of_issue (date): дата выпуска пасспорта (формат даты: YYYY-MM-DD)
        car_color (str): цвет автомобиля
        owner_id (int): идентификатор владельца автомобиля (берется из таблицы OwnerData)
    """
    passport_id: int
    registration_id: str
    car_id: int
    date_of_issue: date
    car_color: str
    owner_id: int
