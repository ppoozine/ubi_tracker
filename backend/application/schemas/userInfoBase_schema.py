from pydantic import BaseModel
from typing import List, Optional, Dict


class CreateUser(BaseModel):
    idnumber: str
    username: str
    sex: str
    addr: str
    email: str
    phone: str

class UserSchema(BaseModel):
    pk: int
    idnumber: str
    username: str
    sex: str
    addr: str
    email: str
    phone: str
    user_id: str

class UpdateUser(BaseModel):
    addr: str
    email: str
    phone: str

class UsernameSchema(BaseModel):
    username: str
