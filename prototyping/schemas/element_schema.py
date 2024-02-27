from ninja import Schema

class ElementIn(Schema):
    chassis_id: int
    name: str
    component_count: int

class ElementOut(Schema):
    id: int
    chassis_id: int
    name: str
    component_count: int
