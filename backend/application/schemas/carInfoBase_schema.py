from pydantic import BaseModel, validator
from typing import List, Optional, Dict
from datetime import datetime, date

class CreateCar(BaseModel):
    username: str
    tracker_id: str
    car_plate: str
    create_date: date
    active: bool

    # @validator("create_date")
    # def date_to_string(cls, v):
    #     return v.isoformat()

class CarSchema(BaseModel):
    pk: int
    user_id: str
    tracker_id: str
    car_plate: str
    create_date: date
    active: bool

class UpdateActive(BaseModel):
    active: bool
