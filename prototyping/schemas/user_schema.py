from ninja import Schema
from typing import Optional

class UserSchema(Schema):
    first_name: str
    last_name: str
    email: str
    role: str
    

class UserCreateSchema(Schema):
    first_name: str
    last_name: str
    email: str
    is_staff: Optional[bool] = False
    role: str
    password: str
    license_id: int  
