from ninja import Schema
from typing import List, Optional
from datetime import date

class ProjectIn(Schema):
    client_id: int
    name: str
    start_date: Optional[date] = None  
    end_date: Optional[date] = None
    users_ids: List[int] = []

class ProjectOut(Schema):
    id: int
    client_id: int
    name: str
    start_date: date  
    end_date: date  
    users_ids: List[int]
