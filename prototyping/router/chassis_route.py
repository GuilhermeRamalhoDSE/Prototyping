from ninja import Router
from typing import Optional
from ninja.errors import HttpError
from prototyping.models.chassis_models import Chassis
from prototyping.schemas.chassis_schema import ChassisSchema, ChassisCreateSchema, ChassisUpdateSchema
from django.shortcuts import get_object_or_404
from prototyping.auth import JWTAuth
from prototyping.utils import get_user_info_from_token, check_user_permission

chassis_router = Router(tags=['Chassis'])

@chassis_router.post("/", response={201: ChassisSchema}, auth=JWTAuth())
def create_chassis(request, payload: ChassisCreateSchema):
    user_info = get_user_info_from_token(request)
    
    is_superuser = check_user_permission(request)
    
    if is_superuser and payload.license_id is not None:
        license_id = payload.license_id
    else:
        license_id = user_info.get('license_id')
    
    if not license_id:
        raise HttpError(400, "license_id is required.")
    
    chassis_data = payload.dict(exclude_unset=True)
    chassis_data['license_id'] = license_id
    chassis = Chassis.objects.create(**chassis_data)

    return 201, chassis


@chassis_router.get("/", response=list[ChassisSchema], auth=JWTAuth())
def read_chassis(request, chassis_id: Optional[int] = None):
    if not check_user_permission(request):
        raise HttpError(403, "You do not have permission to view these chassis.")

    user_info = get_user_info_from_token(request)
    license_id = user_info.get('license_id')
    
    if chassis_id:
        chassis = Chassis.objects.filter(id=chassis_id)
        if license_id:
            chassis = chassis.filter(license_id=license_id)
    else:
        chassis = Chassis.objects.filter(license_id=license_id) if license_id else Chassis.objects.all()
    
    return chassis


@chassis_router.put("/{chassis_id}", response={200: ChassisSchema}, auth=JWTAuth())
def update_chassis(request, chassis_id: int, payload: ChassisUpdateSchema):
    if not check_user_permission(request):
        raise HttpError(403, "You do not have permission to update this chassis.")

    chassis = get_object_or_404(Chassis, id=chassis_id)
    user_info = get_user_info_from_token(request)

    if not user_info.get('is_superuser') and str(chassis.license_id) != str(user_info.get('license_id')):
        raise HttpError(403, "You do not have permission to update this chassis.")

    for attr, value in payload.dict(exclude_none=True).items():
        setattr(chassis, attr, value)
    chassis.save()
    return chassis



@chassis_router.delete("/{chassis_id}", response={204: None}, auth=JWTAuth())
def delete_chassis(request, chassis_id: int):
    if not check_user_permission(request):
        raise HttpError(403, "You do not have permission to delete this chassis.")
    
    chassis = get_object_or_404(Chassis, id=chassis_id)
    user_info = get_user_info_from_token(request)

    if not user_info.get('is_superuser') and str(chassis.license_id) != str(user_info.get('license_id')):
        raise HttpError(403, "You do not have permission to delete this chassis.")
    
    chassis.delete()
    return 204, None


