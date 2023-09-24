"""CRUD модель для работы с базой данных таблицы о пасспортах"""
from typing import Type

import models
from sqlalchemy.orm import Session
from schemas import passports


def get_passport(db: Session, passport_id: int) -> Type[models.TechPassport]:
    """

    :param db: объект сесии
    :param passport_id: идентификатор паспорта
    :return: возвращает объект модели 'TechPassport' по его ID
    """
    return db.query(models.TechPassport).filter(models.TechPassport.passport_id == passport_id).first()


def create_passport(db: Session, item: passports.PassportCreate) -> models.TechPassport:
    """

    :param db: бъект сесии
    :param item: Pydantic модель для валидации
    :return: возвращает объект модели TechPassport представляющий созданный пасспорт
    """
    db_passport = models.TechPassport(passport_id=item.passport_id, registration_id=item.registration_id,
                                      car_id=item.car_id, date_of_issue=item.date_of_issue,
                                      car_color=item.car_color, owner_id=item.owner_id)
    db.add(db_passport)
    db.commit()
    db.refresh(db_passport)
    return db_passport


def update_passport(db: Session, passport_id: int, data: passports.PassportUpdate) -> Type[models.TechPassport] | None:
    """

    :param db: объект сессии
    :param passport_id: идентификатор пасспорта автомобиля, запись котороую нужно обновить
    :param data: Pydantic модель для валидации
    :return: возвращает обновленный объект модели TechPassport, если запись обновлена, либо None
    """
    passport_to_update = db.query(models.TechPassport).filter(models.TechPassport.passport_id == passport_id).first()
    if passport_to_update:
        for key, value in data.dict().items():
            setattr(passport_to_update, key, value)
        db.commit()
        db.refresh(passport_to_update)
        return passport_to_update
    return None


def delete_passport(db: Session, passport_id: int) -> models.TechPassport | None:
    """

    :param db: объект сессии
    :param passport_id: итендификатор пасспорта, запись которую нужно удалить
    :return: возвращает модель пасспорта который был удален, либо None если запись не найдена
    """
    passport_to_delete = db.query(models.TechPassport).get(passport_id)
    if passport_to_delete:
        db.delete(passport_to_delete)
        db.commit()
    return passport_to_delete
