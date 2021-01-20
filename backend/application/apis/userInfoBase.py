from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from ..database import database
from ..models.models import UserInfoBaseModel
from ..schemas.userInfoBase_schema import CreateUser, UserSchema, UpdateUser, UsernameSchema
from ..schemas.common import SuccessCreate, SuccessUpdated, SuccessDeleted
from typing import List
from ..log.log import logger
from ..core.confirm_idnumber import checkID
import hashlib

router = APIRouter()
MD5 = hashlib.md5()

@router.post("/user", response_model=SuccessCreate, status_code=status.HTTP_201_CREATED)
@logger.catch
async def create_user(create: CreateUser):
    db_user = await database.execute(UserInfoBaseModel.select().where(UserInfoBaseModel.c.idnumber == create.idnumber))
    if db_user:
        return JSONResponse(status_code=500, content={"detail": "此用戶已存在!"})
    elif checkID(create.idnumber) == False:
        return JSONResponse(status_code=500, content={"detail": "身分證字號有誤!"})
    else:
        data = create.idnumber + create.username
        MD5.update(data.encode("utf-8"))
        user_id = MD5.hexdigest()
        
        query = UserInfoBaseModel.insert().values(
            idnumber=create.idnumber,
            username=create.username,
            sex=create.sex,
            addr=create.addr,
            email=create.email,
            phone=create.phone,
            user_id=user_id
        )
        await database.execute(query)
        return {"status": "Successfully Created!"}
    
@router.get("/user", response_model=List[UserSchema], status_code=status.HTTP_200_OK)
@logger.catch
async def read_users():
    query = UserInfoBaseModel.select().order_by(UserInfoBaseModel.c.pk)
    return await database.fetch_all(query)

@router.put("/user/{pk}", response_model=SuccessUpdated, status_code=status.HTTP_200_OK)
@logger.catch
async def update_user(pk: int, payload: UpdateUser):
    query = UserInfoBaseModel.update().where(UserInfoBaseModel.c.pk == pk).values(addr=payload.addr, email=payload.email, phone=payload.phone)
    await database.execute(query)
    return {"status": "Successfully Updated!"}

@router.delete("/user/{pk}", response_model=SuccessDeleted, status_code=status.HTTP_200_OK)
@logger.catch
async def delete_user(pk: int):
    query = UserInfoBaseModel.delete().where(UserInfoBaseModel.c.pk == pk)
    await database.execute(query)
    return {"status": "Successfully Deleted!"}

@router.get("/username", response_model=List[UsernameSchema], status_code=status.HTTP_200_OK)
@logger.catch
async def read_username():
    query = UserInfoBaseModel.select().with_only_columns([UserInfoBaseModel.c.username])
    return await database.fetch_all(query)