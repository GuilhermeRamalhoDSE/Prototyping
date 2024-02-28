from ninja import Schema
from typing import List

class ProjectIn(Schema):
    client_id: int
    name: str
    users_ids: List[int] = []

class ProjectOut(Schema):
    id: int
    client_id: int
    name: str
    creation_date: str
    last_release_date: str
    users_ids: List[int]
