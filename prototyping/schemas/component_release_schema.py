from ninja import Schema

class ComponentReleaseCreateSchema(Schema):
    chassis_id: int
    element_id: int
    component_id: int
    file: str

class ComponentReleaseSchema(ComponentReleaseCreateSchema):
    id: int
