from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from ..database import database
from ..models.models import car_segment_table, UserInfoBaseModel, CarInfoBaseModel
from ..schemas.carSegment_schema import CarTripSchema, CoordinateSchema
from typing import List
from ..log.log import logger
from datetime import datetime, timedelta
from sqlalchemy import and_

router = APIRouter()

@router.get("/carTrip/{start_date}/{end_date}/{username}", response_model=List[CarTripSchema], status_code=status.HTTP_200_OK)
async def read_car_trip(start_date: str, end_date: str, username: str):
    # SELECT tracker_id FROM user_info_base INNER JOIN user_info_base.user_id = car_info_base.user_id WHERE user_info_base.username=username;
    tracker_id = await database.execute(UserInfoBaseModel.select().with_only_columns([CarInfoBaseModel.c.tracker_id]).select_from(UserInfoBaseModel.join(CarInfoBaseModel, UserInfoBaseModel.c.user_id == CarInfoBaseModel.c.user_id)).where(UserInfoBaseModel.c.username == username))
    
    trips = []
    count = datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")
    for i in range(count.days+1):
        table = car_segment_table("car_segment_" + (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(i)).strftime("%Y-%m-%d"))
        query = table.select().with_only_columns([table.c.tracker_id, table.c.trip_id, table.c.trip_date]).where(table.c.tracker_id == tracker_id).distinct().order_by(table.c.trip_id)
        trip = await database.fetch_all(query)
        trips = trips + trip
    print(trips)
    return trips


@router.get("/carTracking/{tracker_id}/{trip_date}/{trip_id}", response_model=List[CoordinateSchema], status_code=status.HTTP_200_OK)
async def read_car_tracking(tracker_id: str, trip_date: str, trip_id: int):
    # coordinates = []
    table = car_segment_table("car_segment_" + trip_date)
    query = table.select().with_only_columns([table.c.latitude, table.c.longitude]).where(and_(table.c.tracker_id == tracker_id, table.c.trip_id == trip_id)).order_by(table.c.seq_no)
    return await database.fetch_all(query)