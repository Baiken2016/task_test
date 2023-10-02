"""CRUD модель для работы с базой данных таблицы о владельцах"""
from typing import Type

import models
from sqlalchemy.orm import Session

from schemas import owners


def get_owner(db: Session, item_id: int) -> Type[models.OwnerData]:
    """
    Функция для получения информации о владельце автомобиля
    из базы данных, из таблицы OwnerData по его уникальному идентификатору

    :param db: объект сесии
    :param item_id: идентификатор владельца
    :return: возвращает объект модели 'OwnerData' по его ID
    """
    return db.query(models.OwnerData).filter(models.OwnerData.owner_id == item_id).first()


def create_owner(db: Session, item: owners.OwnerCreate) -> models.OwnerData:
    """
    Функция для создания новой записи в базе данных, в таблице OwnerData.
    Запись осуществляется с помощью pydantic модели OwnerCreate

    :param db: бъект сесии
    :param item: Pydantic модель для валидации
    :return: возвращает объект модели OwnerData представляющий созданного владельца
    """
    db_item = models.OwnerData(owner_id=item.owner_id, owner_name=item.owner_name,
                               registration_address=item.registration_address,
                               actual_address=item.actual_address
                               )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_owner(db: Session, record_id: int, data: owners.OwnerUpdate) -> Type[models.OwnerData] | None:
    """
    Функция для обновления записи в базе данных, в таблице OwnerData

    :param db: объект сессии
    :param record_id: идентификатор владельца автомобиля, запись котороую нужно обновить
    :param data: Pydantic модель для валидации
    :return: возвращает обновленный объект модели OwnerData, если запись обновлена, либо None
    """
    item_to_update = db.query(models.OwnerData).filter(models.OwnerData.owner_id == record_id).first()

    if item_to_update:
        for key, value in data.dict().items():
            setattr(item_to_update, key, value)
        db.commit()
        db.refresh(item_to_update)
        return item_to_update
    return None


def delete_owner(db: Session, item_id: int) -> models.OwnerData | None:
    """
    Функция для удаления записи из базы данных, таблицы OwnerData
    по идентификатору владельца автомобиля

    :param db: объект сессии
    :param item_id: итендификатор владельца, запись которого нужно удалить
    :return: возвращает модель владельца который был удален, либо None если запись не найдена
    """
    item_to_delete = db.query(models.OwnerData).get(item_id)
    if item_to_delete:
        db.delete(item_to_delete)

        db.commit()
    return item_to_delete
