from pydantic import BaseModel, validator
from typing import List, Optional, Dict
from datetime import datetime, date


class CoordinateSchema(BaseModel):
    longitude: float
    latitude: float

class CarTripSchema(BaseModel):
    tracker_id: str
    trip_date: date
    trip_id: int
