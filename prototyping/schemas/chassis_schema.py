from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional
from django.db.models.fields.files import FieldFile


class ChassisBaseSchema(BaseModel):
    name: str
    file: str  
    license_id: int

class ChassisCreateSchema(ChassisBaseSchema):
    license_id: int

class ChassisUpdateSchema(BaseModel):
    name: Optional[str] = None
    file: Optional[str] = None

class ChassisSchema(BaseModel):
    id: int
    name: str
    file: str  
    creation_date: Optional[datetime] = None
    last_modified: Optional[datetime] = None

    @validator('file', pre=True, always=True)
    def convert_file_to_url(cls, v):
        if isinstance(v, FieldFile):
            return v.url  
        return v 
    class Config:
        from_attributes = True