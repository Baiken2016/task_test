from pydantic import BaseModel


class OwnerCreate(BaseModel):
    owner_id: int
    owner_name: str
    registration_address: str
    actual_address: str = None


class OwnerDelete(BaseModel):
    owner_id: int


class OwnerUpdate(BaseModel):
    owner_id: int
    owner_name: str
    registration: str
    actual_address: str
