from ninja import Schema
from typing import Optional

class UserSchema(Schema):
    id: int  
    first_name: str
    last_name: str
    email: str
    role: str
    is_staff: Optional[bool] = False  
    
class UserCreateSchema(Schema):
    first_name: str
    last_name: str
    email: str
    is_staff: Optional[bool] = False
    role: str
    password: str
    license_id: int  


class UserUpdateSchema(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    is_staff: Optional[bool] = None
    role: Optional[str] = None
    password: Optional[str] = None
    license_id: Optional[int] = None
