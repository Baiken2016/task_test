"""CRUD модель для работы с базой данных таблицы моделей авто"""
from typing import Type, Any

import models
from sqlalchemy.orm import Session
from schemas import cars


def get_car(db: Session, car_id: int) -> Type[models.CarModels] | None:
    """

    :param db: объект сессиии SQLAlchemy
    :param car_id: идентификатор автомобиля
    :return: возвращает объект модели 'CarModels' по его ID из таблицы

    """
    return db.query(models.CarModels).filter(models.CarModels.car_id == car_id).first()


def create_car(db: Session, item: cars.CarCreate) -> models.CarModels:
    """

    :param db: объект сессии
    :param item: Pydantic модель для валидации данных
    :return: возвращает объект модели 'CarModels', представляющий созданный автомобиль
    """

    db_car = models.CarModels(car_id=item.car_id, car_model=item.car_model,
                              car_height=item.car_height, car_width=item.car_width,
                              car_length=item.car_length, car_speed=item.car_speed,
                              date_of_creation=item.date_of_creation)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def update_car(db: Session, car_id: int, data: cars.CarUpdate) -> Type[models.CarModels] | None:
    """

    :param db: объект сесиии
    :param car_id: идентификатор модели автомобиля, которую нужно обновить
    :param data: Pydantic модель, для валидации
    :return: возвращает обновленный объект модели 'CarModels', если запись обновлена
    """
    car_to_update = db.query(models.CarModels).filter(models.CarModels.car_id == car_id).first()
    if car_to_update:
        for key, value in data.dict().items():
            setattr(car_to_update, key, value)
        db.commit()
        db.refresh(car_to_update)
        return car_to_update
    return None


def delete_car(db: Session, car_id: int) -> models.CarModels | None:
    """

    :param db: объект сесиии
    :param car_id: идентификатор автомобиля, который нужно удалить
    :return: возвращает модель автомобиля который был удален, либо None если запись не найдена
    """
    car_to_delete = db.query(models.CarModels).get(car_id)
    if car_to_delete:
        db.delete(car_to_delete)
        db.commit()
    return car_to_delete
