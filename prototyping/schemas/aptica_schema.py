from ninja import Schema
from typing import Optional

class ApticaCreate(Schema):
    license_id: int
    hand: str
    mac_address: str

class ApticaUpdate(Schema):
    license_id: Optional[int] = None
    hand: Optional[str] = None
    mac_address: Optional[str] = None

class ApticaOut(Schema):
    id: int
    license_id: int
    hand: str
    mac_address: str
