from ninja import Schema
from typing import Optional

class ComponentIn(Schema):
    version_id: int
    name: str
    position_x: float
    limit_position_x: Optional[float] = None
    position_y: float
    limit_position_y: Optional[float] = None
    position_z: float
    limit_position_z: Optional[float] = None
    rotation_x: float
    limit_rotation_x: Optional[float] = None
    rotation_y: float
    limit_rotation_y: Optional[float] = None
    rotation_z: float
    limit_rotation_z: Optional[float] = None
    rotation_w: float
    limit_rotation_w: Optional[float] = None
    area_radius: float
    haptic_stiffness: float
    haptic_temperature: float
    haptic_texture: int

class ComponentOut(Schema):
    id: int
    version_id: int
    name: str
    position_x: float
    position_y: float
    position_z: float
    rotation_x: float
    rotation_y: float
    rotation_z: float
    rotation_w: float
    area_radius: float
    haptic_stiffness: float
    haptic_temperature: float
    haptic_texture: int
