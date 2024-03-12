from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional
from django.db.models.fields.files import FieldFile

class ComponentBaseSchema(BaseModel):
    version_id: int
    name: str
    limit_position_x: float
    limit_position_y: float
    limit_position_z: float
    limit_rotation_x: float
    limit_rotation_y: float
    limit_rotation_z: float
    limit_rotation_w: float
    area_radius: float
    haptic_stiffness: Optional[float] = None
    haptic_temperature: Optional[float] = None
    haptic_texture: Optional[int] = None


class ComponentCreateSchema(ComponentBaseSchema):
    element_id: int

class ComponentUpdateSchema(BaseModel):
    version_id: Optional[int] = None
    name: Optional[str] = None
    limit_position_x: Optional[float] = None
    limit_position_y: Optional[float] = None
    limit_position_z: Optional[float] = None
    limit_rotation_x: Optional[float] = None
    limit_rotation_y: Optional[float] = None
    limit_rotation_z: Optional[float] = None
    limit_rotation_w: Optional[float] = None
    area_radius: Optional[float] = None
    haptic_stiffness: Optional[float] = None
    haptic_temperature: Optional[float] = None
    haptic_texture: Optional[int] = None
    file_path: Optional[str] = Field(None, alias='file')

class ComponentSchema(BaseModel):
    id: int
    version_id: int
    element_id: int  
    name: str
    limit_position_x: Optional[float] = None
    limit_position_y: Optional[float] = None
    limit_position_z: Optional[float] = None
    limit_rotation_x: Optional[float] = None
    limit_rotation_y: Optional[float] = None
    limit_rotation_z: Optional[float] = None
    limit_rotation_w: Optional[float] = None
    area_radius: float
    haptic_stiffness: Optional[float]
    haptic_temperature: Optional[float]
    haptic_texture: Optional[int]
    file_path: Optional[str] = Field(None, alias='file')
    creation_date: Optional[datetime] = None
    last_modified_date: Optional[datetime] = None

    @validator('file_path', pre=True, always=True)
    def convert_file_to_url(cls, v):
        if isinstance(v, FieldFile) and v.name:
            return v.url
        return v

    class Config:
        from_attributes = True
