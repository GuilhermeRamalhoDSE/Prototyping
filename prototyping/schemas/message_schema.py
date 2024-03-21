from datetime import datetime
from ninja import Schema

class MessageIn(Schema):
    client_id: int
    project_id: int
    user_id: int
    message: str

class UserOut(Schema):
    id: int
    full_name: str  

class MessageOut(Schema):
    id: int
    client_id: int
    project_id: int
    user: UserOut
    date: datetime
    message: str
    formatted_date: str = None 

    def __post_init__(self):
        super().__post_init__() 
        self.formatted_date = self.date.strftime('%Y-%m-%d %H:%M:%S') if self.date else None
 