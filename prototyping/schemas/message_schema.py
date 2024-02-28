from datetime import datetime
from ninja import Schema

class MessageIn(Schema):
    client_id: int
    project_id: int
    user_id: int
    message: str

class MessageOut(Schema):
    id: int
    client_id: int
    project_id: int
    user_id: int
    date: datetime
    message: str
