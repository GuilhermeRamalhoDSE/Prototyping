from ninja import Schema

class ElementIn(Schema):
    chassis_id: int
    name: str
    

class ElementOut(Schema):
    id: int
    chassis_id: int
    name: str
    component_count: int
    
    @staticmethod
    def resolve_chassis_id(obj):
        return obj.chassis.id

    @staticmethod
    def resolve_component_count(obj):
        return obj.component_count