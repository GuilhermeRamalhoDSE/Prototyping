from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional
from django.db.models.fields.files import FieldFile


class ChassisBaseSchema(BaseModel):
    name: str
    file: str  

class ChassisCreateSchema(ChassisBaseSchema):
    pass

class ChassisSchema(BaseModel):
    id: int
    name: str
    file: str  
    creation_date: datetime = Field(None, alias='data_creazione')
    last_modified: datetime = Field(None, alias='data_ultima_modifica')

    @validator('file', pre=True, always=True)
    def convert_file_to_url(cls, v):
        if isinstance(v, FieldFile):
            return v.url  
        return v 
    class Config:
        orm_mode = True
        from_attributes = True