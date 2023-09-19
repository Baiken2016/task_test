from pydantic import BaseModel


class CarCreate(BaseModel):
    car_id: int
    car_model: str
    car_height: float
    car_width: float
    car_length: float
    car_speed: float


class CarUpdate(BaseModel):
    car_id: int
    car_model: str
    car_height: float
    car_width: float
    car_length: float
    car_speed: float


class CarDelete(BaseModel):
    car_id: int
