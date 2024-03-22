from datetime import datetime
from ninja import Schema
from typing import Optional

class MessageIn(Schema):
    client_id: int
    project_id: int
    user_id: int
    message: str

class UserOut(Schema):
    id: int
    full_name: Optional[str]

class MessageOut(Schema):
    id: int
    client_id: int
    project_id: int
    user: UserOut
    date: datetime
    message: str
    formatted_date: str = None

    def __init__(self, **data):
        super().__init__(**data)
        self.formatted_date = self.date.strftime('%Y-%m-%d %H:%M:%S') if self.date else None
 