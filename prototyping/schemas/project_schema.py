from ninja import Schema
from typing import List, Optional
from datetime import date

class ProjectIn(Schema):
    client_id: int
    name: str
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
    name: str
    start_date: date
    end_date: Optional[date] = None
    users: List[UserOut] 
