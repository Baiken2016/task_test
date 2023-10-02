"""Здесь хранится pydantic модель таблицы о владельцах авто
для валидации входных и выходных данных"""

from pydantic import BaseModel


class OwnerCreate(BaseModel):
    """
    Pydantic модель для передачи данных при создании новой записи
    в базу данных, в таблице OwnerData

    Атрибуты:
        owner_id (int): уникальный идентификатор владельца
        owner_name (str): Имя и фамилия владельца
        registration_address (str): адрес регистрации местожительства владельца
        actual_address (str): адрес проживания владельца
    """
    owner_id: int
    owner_name: str
    registration_address: str
    actual_address: str = None


class OwnerDelete(BaseModel):
    """
    Pydantic модель для запроса на удаление записи из базы данных,
    таблицы OwnerData по идентификатору владельца

    Атрибуты:
        owner_id (int): уникальный идентификатор владельца
    """
    owner_id: int


class OwnerUpdate(BaseModel):
    """
    Pydantic модель для передачи обновленных данных
    в базу данных, в таблице OwnerData

    Атрибуты:
        owner_id (int): уникальный идентификатор владельца
        owner_name (str): Имя и фамилия владельца
        registration_address (str): адрес регистрации местожительства владельца
        actual_address (str): адрес проживания владельца
    """
    owner_id: int
    owner_name: str
    registration: str
    actual_address: str
