from ninja import Schema
from typing import List, Optional
from datetime import date

class ProjectIn(Schema):
    client_name: Optional[str] = None
    name: Optional[str] = None
    start_date: Optional[date] = None  
    end_date: Optional[date] = None
    users_ids: List[int] = []

class UserOut(Schema):
    id: int
    full_name: str

class UserIdSchema(Schema):
    user_id: int


class ProjectOut(Schema):
    id: int
    client_id: int
    client_name: str
    name: str
    start_date: date
    end_date: Optional[date] = None
    users: List[UserOut] 
