from datetime import datetime
from ninja import Schema

class ReleaseIn(Schema):
    client_id: int
    project_id: int
    name: str
    

class ReleaseOut(Schema):
    id: int
    client_id: int
    project_id: int
    name: str
    file_url: str  
    creation_date: datetime
