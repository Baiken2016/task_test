import models
from sqlalchemy.orm import Session
from schemas import owners


def get_owner(db: Session, item_id: int):
    return db.query(models.OwnerData).filter(models.OwnerData.owner_id == item_id).first()


def create_owner(db: Session, item: owners.OwnerCreate):
    db_item = models.OwnerData(owner_id=item.owner_id, owner_name=item.owner_name,
                               registration_address=item.registration_address,
                               actual_address=item.actual_address
                               )

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_owner(db: Session, record_id: int, data: owners.OwnerUpdate):
    item_to_update = db.query(models.OwnerData).filter(models.OwnerData.owner_id == record_id).first()

    if item_to_update:
        for key, value in data.dict().items():
            setattr(item_to_update, key, value)
        db.commit()
        db.refresh(item_to_update)
        return item_to_update
    return None


def delete_owner(db: Session, item_id: int):
    item_to_delete = db.query(models.OwnerData).get(item_id)
    if item_to_delete:
        db.delete(item_to_delete)

        db.commit()
    return item_to_delete
