from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional
from django.db.models.fields.files import FieldFile


class ChassisBaseSchema(BaseModel):
    name: str
    file: Optional[str] = None  
    license_id: int

class ChassisCreateSchema(ChassisBaseSchema):
    pass  

class ChassisUpdateSchema(BaseModel):
    name: Optional[str] = None
    file: Optional[str] = None  

class ChassisSchema(BaseModel):
    id: int
    name: str
    file: Optional[str] = None  
    creation_date: Optional[datetime] = None
    last_modified: Optional[datetime] = None

    @validator('file', pre=True, always=True)
    def convert_file_to_url(cls, v):
        if isinstance(v, FieldFile) and v.name:  
            return v.url
        return None  
    class Config:
        from_attributes = True