from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from schemas import owners, passports, cars

from crud import owner_crud, passport_crud, cars_crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post('/add_owner/', response_model=owners.OwnerCreate)
def create_item(item: owners.OwnerCreate, db: Session = Depends(get_db)):
    return owner_crud.create_owner(db=db, item=item)


@app.get('/owner_data/{owner_id}', response_model=owners.OwnerCreate)
def get_owner(item_id: int, db: Session = Depends(get_db)):
    item = owner_crud.get_owner(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Owner not found")
    return item


@app.put('/update_owner/{owner-id}', response_model=owners.OwnerUpdate)
def update_owner(owner_id: int, data: owners.OwnerUpdate, db: Session = Depends(get_db)):
    owner = owner_crud.update_owner(db, owner_id, data)
    if owner:
        return owner
    raise HTTPException(status_code=404, detail='Owner not found')


@app.delete('/delete_owner/{owner_id}', response_model=owners.OwnerDelete)
def delete_item(data: owners.OwnerDelete, db: Session = Depends(get_db)):
    owner_to_delete = owner_crud.delete_owner(db, data.owner_id)
    if owner_to_delete:
        return owner_to_delete
    raise HTTPException(status_code=404, detail='owner not found')


@app.post('/add_passport', response_model=passports.PassportCreate)
def create_passport(item: passports.PassportCreate, db: Session = Depends(get_db)):
    return passport_crud.create_passport(db=db, item=item)


@app.get('/get_passport/{passport_id}', response_model=passports.PassportCreate)
def get_passport(passport_id: int, db: Session = Depends(get_db)):
    passport = passport_crud.get_passport(db, passport_id)
    if passport:
        return passport
    raise HTTPException(status_code=404, detail='passport not found')


@app.put('/update_passport/{passport_id}', response_model=passports.PassportUpdate)
def update_owner(passport_id: int, data: passports.PassportUpdate, db: Session = Depends(get_db)):
    passport_to_update = passport_crud.update_passport(db, passport_id, data)
    if passport_to_update:
        return passport_to_update
    raise HTTPException(status_code=404, detail='passport not found')


@app.delete('/delete_passport/{passport_id}', response_model=passports.PassportDelete)
def delete_passport(data: passports.PassportDelete, db: Session = Depends(get_db)):
    passport_do_delete = passport_crud.delete_passport(db, passport_id=data.id)
    if passport_do_delete:
        return passport_do_delete
    raise HTTPException(status_code=404, detail='passport not found')


@app.post('/add_car_model', response_model=cars.CarCreate)
def create_car(item: cars.CarCreate, db: Session = Depends(get_db)):
    return cars_crud.create_car(db=db, item=item)


@app.get('/get_car_model/{car_id}', response_model=cars.CarCreate)
def get_car(car_id: int, db: Session = Depends(get_db)):
    car_model = cars_crud.get_car(db, car_id)
    if car_model:
        return car_model
    raise HTTPException(status_code=404, detail='car_model not found')


@app.put('/update_car_model/{car_id}', response_model=cars.CarUpdate)
def update_car(car_id: int, data: cars.CarUpdate, db: Session = Depends(get_db)):
    car_to_update = cars_crud.update_car(db, car_id, data)
    if car_to_update:
        return car_to_update
    raise HTTPException(status_code=404, detail='car_model not found')


@app.delete('/delete_car_model/{car_id}', response_model=cars.CarDelete)
def delete_car(data: cars.CarDelete, db: Session = Depends(get_db)):
    car_to_delete = cars_crud.delete_car(db, data.car_id)
    if car_to_delete:
        return car_to_delete
    raise HTTPException(status_code=404, detail='car_model not found')
