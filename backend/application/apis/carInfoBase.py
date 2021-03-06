from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from ..database import database
from ..models.models import CarInfoBaseModel, UserInfoBaseModel, CarPlateModel
from ..schemas.carInfoBase_schema import CreateCar, CarSchema, UpdateActive
from ..schemas.common import SuccessCreate, SuccessUpdated, SuccessDeleted
from typing import List
from ..log.log import logger
from datetime import datetime
from sqlalchemy import and_

router = APIRouter()

@router.post("/car", response_model=SuccessCreate, status_code=status.HTTP_201_CREATED)
@logger.catch
async def create_car(create: CreateCar):
    db_car = await database.execute(CarInfoBaseModel.select().where(CarInfoBaseModel.c.tracker_id == create.tracker_id))
    if db_car:
        return JSONResponse(status_code=500, content={"detail": "此追蹤器已被註冊!"})
    else:
        get_user_id = UserInfoBaseModel.select().with_only_columns([UserInfoBaseModel.c.user_id]).where(UserInfoBaseModel.c.username == create.username)
        user_id = await database.fetch_one(get_user_id)

        db_car_plate = await database.execute(CarPlateModel.select().with_only_columns([CarPlateModel.c.end_date]).where(and_(CarPlateModel.c.car_plate == create.car_plate)))
        if db_car_plate is not None:
            insert_car_plate_query = CarPlateModel.insert().values(
                car_plate=create.car_plate,
                start_date=create.create_date,
            )
            await database.execute(insert_car_plate_query)
        
        insert_car_query = CarInfoBaseModel.insert().values(
            user_id=user_id[0],
            tracker_id=create.tracker_id,
            car_plate=create.car_plate,
            create_date=create.create_date,
            active=create.active,
        )
        await database.execute(insert_car_query)

        
        return {"status": "Successfully Created!"}

@router.get("/car", response_model=List[CarSchema], status_code=status.HTTP_200_OK)
@logger.catch
async def read_cars():
    query = CarInfoBaseModel.select().order_by(CarInfoBaseModel.c.pk)
    return await database.fetch_all(query)

@router.delete("/car/{pk}/{car_plate}", response_model=SuccessDeleted, status_code=status.HTTP_200_OK)
@logger.catch
async def delete_user(pk: int, car_plate: str):
    car_plate_end_date = CarPlateModel.update().where(CarPlateModel.c.car_plate == car_plate).values(
        end_date=datetime.today()
    )
    await database.execute(car_plate_end_date)

    query = CarInfoBaseModel.delete().where(CarInfoBaseModel.c.pk == pk)
    await database.execute(query)
    return {"status": "Successfully Deleted!"}

@router.put("/car/{pk}", response_model=SuccessUpdated, status_code=status.HTTP_200_OK)
@logger.catch
async def update_active(pk: int, payload: UpdateActive):
    query = CarInfoBaseModel.update().where(CarInfoBaseModel.c.pk == pk).values(active=payload.active)
    await database.execute(query)
    return {"status": "Successfully Updated!"}