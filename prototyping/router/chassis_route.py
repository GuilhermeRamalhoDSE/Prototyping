from typing import Optional
from ninja import Router, File
from ninja.files import UploadedFile
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from prototyping.models.chassis_models import Chassis
from prototyping.models.license_models import License
from prototyping.schemas.chassis_schema import ChassisSchema, ChassisUpdateSchema, ChassisCreateSchema
from django.http import HttpRequest
from prototyping.auth import JWTAuth
from prototyping.utils import get_user_info_from_token, check_user_permission
from django.http import FileResponse, Http404
import os
from django.core.files.storage import default_storage

chassis_router = Router(tags=['Chassis'])



@chassis_router.post("/", response={201: ChassisSchema}, auth=JWTAuth())
def create_chassis(request: HttpRequest, chassis_in: ChassisCreateSchema, file: UploadedFile = File(...)):
    user_info = get_user_info_from_token(request)
    is_superuser = check_user_permission(request)
    
    if is_superuser and chassis_in.license_id is not None:
        final_license_id = chassis_in.license_id
    else:
        final_license_id = user_info.get('license_id')
    
    if not final_license_id:
        raise HttpError(400, "license_id is required.")

    license = get_object_or_404(License, id=final_license_id)

    chassis = Chassis.objects.create(
        name=chassis_in.name, 
        license=license, 
        file=file  
    )
    
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

@chassis_router.get("/download/{chassis_id}")
def download_chassis_file(request, chassis_id: int, token: Optional[str] = None):
    user_info = None
    if token:
        try:
            jwt_auth = JWTAuth()
            user_info = jwt_auth.authenticate(request, token)
        except:

            pass
    
    chassis = get_object_or_404(Chassis, id=chassis_id)
    
    if user_info:
        is_superuser = user_info.get('is_superuser', False)
        if not (is_superuser or str(chassis.license_id) == str(user_info.get('license_id', ''))):
            raise Http404("You do not have permission to download this file.")

    if chassis.file and hasattr(chassis.file, 'path'):
        file_path = chassis.file.path
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
        else:
            raise Http404("File does not exist.")
    else:
        raise Http404("No file associated with this chassis.")



@chassis_router.put("/{chassis_id}", response={200: ChassisSchema}, auth=JWTAuth())
def update_chassis(request, chassis_id: int, payload: ChassisUpdateSchema, file: Optional[UploadedFile] = File(None)):

    if not check_user_permission(request):
        raise HttpError(403, "You do not have permission to update this chassis.")

    chassis = get_object_or_404(Chassis, id=chassis_id)
    user_info = get_user_info_from_token(request)

    if not user_info.get('is_superuser') and str(chassis.license_id) != str(user_info.get('license_id')):
        raise HttpError(403, "You do not have permission to update this chassis.")

    if file and chassis.file:
        if default_storage.exists(chassis.file.name):
            default_storage.delete(chassis.file.name)

    for attr, value in payload.dict(exclude_none=True).items():
        setattr(chassis, attr, value)

    if file: 
        chassis.file = file

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

    if chassis.file:
        file_path = chassis.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
    
    chassis.delete()
    return 204, None
