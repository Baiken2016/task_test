"""В этом файле хранятся pydantic модели таблицы о тех пасспаортах
для валидации входных и выходных данных"""

from datetime import date

from pydantic import BaseModel


class PassportCreate(BaseModel):
    passport_id: int
    registration_id: str
    car_id: int
    date_of_issue: date
    car_color: str
    owner_id: int


class PassportDelete(BaseModel):
    id: int


class PassportUpdate(BaseModel):
    passport_id: int
    registration_id: str
    car_id: int
    date_of_issue: date
    car_color: str
    owner_id: int
