from ninja import Schema
from typing import Optional

class ElementIn(Schema):
    chassis_id: Optional[int] = None
    name: Optional[str] = None
    

class ElementOut(Schema):
    id: int
    chassis_id: int
    name: str
    component_count: int
    chassis_name: str
    
    @staticmethod
    def resolve_chassis_id(obj):
        return obj.chassis.id

    @staticmethod
    def resolve_component_count(obj):
        return obj.component_count
    
    @staticmethod
    def resolve_chassis_name(obj): 
        return obj.chassis.name