from pydantic import BaseModel
from typing import List, Optional

class SuccessCreate(BaseModel):
    status: str = "Successfully Created!"

class SuccessUpdated(BaseModel):
    status: str = "Successfully Updated!"

class SuccessDeleted(BaseModel):
    status: str = "Successfully Deleted!"