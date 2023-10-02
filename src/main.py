from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from schemas import passports, cars, owners
import uvicorn
from crud import owner_crud, cars_crud, passport_crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()  # Создание объекта сесии из SQLAlchemy sessionmaker

    try:
        yield db
    finally:
        db.close()


# Маршруты для управления и работы с данными
@app.post('/add_owner/', response_model=owners.OwnerCreate)
def create_item(item: owners.OwnerCreate, db: Session = Depends(get_db)):
    """
    Функция для создания нового владельца в базе данных в таблице OwnerData

    :param db: объект сесии
    :param item: Pydantic модель для валидации

    :return: возвращает JSON типа dict с информацией о созданном владельце
    """
    return owner_crud.create_owner(db=db, item=item)


@app.get('/owner_data/{owner_id}', response_model=owners.OwnerCreate)
def get_owner(item_id: int, db: Session = Depends(get_db)):
    """
    Функция для получения информации о владельце автомобиля
    из базы данных, из таблицы OwnerData по его уникальному идентификатору

    :param db: объект сесии
    :param item_id: уникальный идентификатор владельца

    :return: возвращает JSON типа dict который содержит информацию о владельце,
             либо ошибку если владельца не существует
    """
    item = owner_crud.get_owner(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    return item


@app.put('/update_owner/{owner-id}', response_model=owners.OwnerUpdate)
def update_owner(owner_id: int, data: owners.OwnerUpdate, db: Session = Depends(get_db)):
    """
    Функция для обновления информации о владельце в базе данных, в таблице OwnerData

    :param db: объект сессии
    :param owner_id: идентификатор владельца автомобиля, запись котороую нужно обновить
    :param data: Pydantic модель для валидации

    :return: возвращает JSON типа dict с обновленной информацией
    """
    owner = owner_crud.update_owner(db, owner_id, data)
    if owner:
        return owner
    raise HTTPException(status_code=404, detail='Owner not found')


@app.delete('/delete_owner/{owner_id}', response_model=owners.OwnerDelete)
def delete_item(data: owners.OwnerDelete, db: Session = Depends(get_db)):
    """
    Функция для удаления записи из базы данных, таблицы OwnerData
    по идентификатору владельца автомобиля

    :param db: объект сессии
    :param data: Pydantic модель для валидации

    :return: возвращает JSON типа dict который содержит ID владельца если он удален,
             либо ошибку если запись не найдена
    """
    owner_to_delete = owner_crud.delete_owner(db, data.owner_id)
    if owner_to_delete:
        return owner_to_delete
    raise HTTPException(status_code=404, detail='owner not found')


@app.post('/add_passport', response_model=passports.PassportCreate)
def create_passport(item: passports.PassportCreate, db: Session = Depends(get_db)):
    """
    Функция для создания нового тех. пасспорта в базе данных, в таблице TechPassport.


    :param db: бъект сесии
    :param item: Pydantic модель для валидации

    :return: возвращает JSON типа dict  информацией о созданном тех. пасспорте
    """
    return passport_crud.create_passport(db=db, item=item)


@app.get('/get_passport/{passport_id}', response_model=passports.PassportCreate)
def get_passport(passport_id: int, db: Session = Depends(get_db)):
    """
    Функция для получения информации о тех. пасспорте автомобиля
    из базы данных, из таблицы TechPassport по его уникальному идентификатору

    :param db: объект сесии
    :param passport_id: уникальный идентификатор паспорта

    :return: возвращает JSON типа dict с информацией о пасспорте, либо ошибку если пасспорт отсутствует
    """
    passport = passport_crud.get_passport(db, passport_id)
    if passport:
        return passport
    raise HTTPException(status_code=404, detail='passport not found')


@app.put('/update_passport/{passport_id}', response_model=passports.PassportUpdate)
def update_owner(passport_id: int, data: passports.PassportUpdate, db: Session = Depends(get_db)):
    """
    Функция для обновления пасспорта в базе данных, в таблице TechPassport

    :param db: объект сессии
    :param passport_id: идентификатор пасспорта, котороый нужно обновить
    :param data: Pydantic модель для валидации

    :return: возвращает JSON типа dict с обновленной информацией
    """
    passport_to_update = passport_crud.update_passport(db, passport_id, data)
    if passport_to_update:
        return passport_to_update
    raise HTTPException(status_code=404, detail='passport not found')


@app.delete('/delete_passport/{passport_id}', response_model=passports.PassportDelete)
def delete_passport(data: passports.PassportDelete, db: Session = Depends(get_db)):
    """
    Функция для удаления пасспорта из базы данных, таблицы TechPassport
    по идентификатору тех. пасспорта

    :param db: объект сессии
    :param data: Pydantic модель для валидации

    :return: возвращает JSON типа dict с ID пасспорта если он удален, либо ошибку если запись не найдена
    """
    passport_do_delete = passport_crud.delete_passport(db, data.id)
    if passport_do_delete:
        return passport_do_delete
    raise HTTPException(status_code=404, detail='passport not found')


@app.post('/add_car_model', response_model=cars.CarCreate)
def create_car(item: cars.CarCreate, db: Session = Depends(get_db)):
    """
    Функция для создания новой модели автомобиля в базе данных, в таблице CarModels.


    :param db: объект сессии
    :param item: Pydantic модель для валидации данных

    :return: возвращает JSON типа dict с информацией о созданной модели авто
    """
    return cars_crud.create_car(db=db, item=item)


@app.get('/get_car_model/{car_id}', response_model=cars.CarCreate)
def get_car(car_id: int, db: Session = Depends(get_db)):
    """
    Функция для получения информации о модели автомобиля
    из таблицы CarModels по его уникальному идентификатору

    :param db: объект сессиии
    :param car_id: идентификатор автомобиля

    :return: возвращает JSON типа dict с информацией о модели, либо ошибку если данная модель не существует
    """
    car_model = cars_crud.get_car(db, car_id)
    if car_model:
        return car_model
    raise HTTPException(status_code=404, detail='car_model not found')


@app.put('/update_car_model/{car_id}', response_model=cars.CarUpdate)
def update_car(car_id: int, data: cars.CarUpdate, db: Session = Depends(get_db)):
    """
    Функция для обновления модели авто в базе данных, в таблице CarModels

    :param db: объект сесиии
    :param car_id: идентификатор модели автомобиля, которую нужно обновить
    :param data: Pydantic модель, для валидации

    :return: возвращает JSON типа dict с обновленной информацией
    """
    car_to_update = cars_crud.update_car(db, car_id, data)
    if car_to_update:
        return car_to_update
    raise HTTPException(status_code=404, detail='car_model not found')


@app.delete('/delete_car_model/{car_id}', response_model=cars.CarDelete)
def delete_car(data: cars.CarDelete, db: Session = Depends(get_db)):
    """
    Функция для удаления модели авто из базы данных, таблицы CarModels
    по идентификатору модели автомобиля

    :param db: объект сесиии
    :param data: Pydantic модель для валидации

    :return: возвращает JSON типа dict с ID если модель удалена, либо ошибку если запись не найдена
    """
    car_to_delete = cars_crud.delete_car(db, data.car_id)
    if car_to_delete:
        return car_to_delete
    raise HTTPException(status_code=404, detail='car_model not found')


if __name__ == '__main__':
    uvicorn.run(app)
