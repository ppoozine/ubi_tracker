from pydantic import BaseModel, validator
from typing import List, Optional, Dict
from datetime import datetime, date

class CarPlateSchema(BaseModel):
    pk: int
    car_plate: str
    start_date: date
    end_date: Optional[date]