from ninja import Schema
from typing import Optional

class AuthSchema(Schema):
    email: str
    password: str

class LoginResponseSchema(Schema):
    token: str
    is_superuser: bool
    is_staff: bool
    license_id: Optional[int] = None 
