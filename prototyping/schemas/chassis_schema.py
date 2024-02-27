from datetime import datetime
from pydantic import BaseModel, Field


class ChassisBaseSchema(BaseModel):
    name: str
    file: str  

class ChassisCreateSchema(ChassisBaseSchema):
    pass

class ChassisSchema(ChassisBaseSchema):
    id: int
    creation_date: datetime = Field(None, alias='data_creazione')
    last_modified: datetime = Field(None, alias='data_ultima_modifica')

    class Config:
        from_attributes = True
