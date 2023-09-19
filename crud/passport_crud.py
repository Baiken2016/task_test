import models
from sqlalchemy.orm import Session
from schemas import passports


def get_passport(db: Session, passport_id: int):
    return db.query(models.TechPassport).filter(models.TechPassport.passport_id == passport_id).first()


def create_passport(db: Session, item: passports.PassportCreate):
    db_passport = models.TechPassport(passport_id=item.passport_id, registration_id=item.registration_id,
                                      car_id=item.car_id, date_of_issue=item.date_of_issue,
                                      car_color=item.car_color, owner_id=item.owner_id)
    db.add(db_passport)
    db.commit()
    db.refresh(db_passport)
    return db_passport


def update_passport(db: Session, passport_id: int, data: passports.PassportUpdate):
    passport_to_update = db.query(models.TechPassport).filter(models.TechPassport.passport_id == passport_id).first()
    if passport_to_update:
        for key, value in data.dict().items():
            setattr(passport_to_update, key, value)
        db.commit()
        db.refresh(passport_to_update)
        return passport_to_update
    return None


def delete_passport(db: Session, passport_id: int):
    passport_to_delete = db.query(models.TechPassport).get(passport_id)
    if passport_to_delete:
        db.delete(passport_to_delete)
        db.commit()
    return passport_to_delete
