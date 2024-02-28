from ninja import Router
from prototyping.models.chassis_models import Chassis
from prototyping.schemas.chassis_schema import ChassisSchema, ChassisCreateSchema
from django.shortcuts import get_object_or_404

chassis_router = Router(tags=['Chassis'])

@chassis_router.post("/", response={201: ChassisSchema})
def create_chassis(request, payload: ChassisCreateSchema):
    chassis = Chassis.objects.create(**payload.dict())
    return 201, chassis

@chassis_router.get("/", response=list[ChassisSchema])
def read_chassis(request):
    chassis = Chassis.objects.all()
    return chassis

@chassis_router.put("/{chassis_id}", response={200: ChassisSchema})
def update_chassis(request, chassis_id: int, payload: ChassisCreateSchema):
    chassis = get_object_or_404(Chassis, id=chassis_id)
    for attr, value in payload.dict().items():
        setattr(chassis, attr, value)
    chassis.save()
    return chassis

@chassis_router.delete("/{chassis_id}", response={200: None})
def delete_chassis(request, chassis_id: int):
    chassis = get_object_or_404(Chassis, id=chassis_id)
    chassis.delete()
    return 204, None
