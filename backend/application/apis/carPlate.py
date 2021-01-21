from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from ..database import database
from ..models.models import CarPlateModel
from ..schemas.carPlate_schema import CarPlateSchema
from typing import List
from ..log.log import logger
from datetime import datetime

router = APIRouter()

@router.get("/carPlate", response_model=List[CarPlateSchema], status_code=status.HTTP_200_OK)
@logger.catch
async def read_car_plate():
    query = CarPlateModel.select().order_by(CarPlateModel.c.pk)
    return await database.fetch_all(query)
    

