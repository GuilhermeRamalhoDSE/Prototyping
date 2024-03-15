from ninja import Router, UploadedFile, File
from django.shortcuts import get_object_or_404
from typing import List, Optional
from ninja.errors import HttpError
from prototyping.schemas.component_schema import ComponentCreateSchema, ComponentUpdateSchema, ComponentSchema
from prototyping.models.component_model import Component
from prototyping.models.chassis_models import Chassis
from prototyping.models.element_models import Element
from prototyping.auth import JWTAuth
from django.http import Http404
from prototyping.utils import get_user_info_from_token, check_user_permission
from django.http import FileResponse
import os
from django.core.files.storage import default_storage

component_router = Router(tags=["Components"])

@component_router.post("/", response={201: ComponentSchema}, auth=JWTAuth())
def create_component(request, component_in: ComponentCreateSchema, file: UploadedFile = File(...)):
    user_info = get_user_info_from_token(request)
    is_superuser = check_user_permission(request)

    if is_superuser:
        element_id = component_in.element_id
    else:
        element_id = user_info.get('element_id')

    if not element_id:
        raise Http404("Element ID is required.")

    element = get_object_or_404(Element, id=element_id)
    
    if not is_superuser and str(element.chassis.license_id) != str(user_info.get('license_id')):
        raise Http404("You do not have permission to add components to this element.")

    component_data = component_in.dict(exclude_unset=True, exclude={'element_id'})
    component = Component.objects.create(
        **component_data,
        element=element,
        file=file
    )

    component_schema = ComponentSchema.from_orm(component)

    return 201, component_schema


@component_router.get("/", response=List[ComponentSchema], auth=JWTAuth()) 
def read_components(request, element_id: Optional[int] = None):
    if not check_user_permission(request):
        raise HttpError(403, "You do not have permission to view these components.")
    
    user_info = get_user_info_from_token(request)
    license_id = user_info.get('license_id')

    if not element_id:
        raise HttpError(400, "Element ID is required.")
    if license_id is not None:
        element = get_object_or_404(Element.objects.select_related('chassis'), id=element_id, chassis__license_id=license_id)
    else:
        element = get_object_or_404(Element, id=element_id)
    
    components = Component.objects.filter(element=element)
    
    return components

@component_router.get("/{component_id}", response=ComponentSchema, auth=JWTAuth())
def read_component_by_id(request, component_id: int):
    if not check_user_permission(request):
        raise HttpError(403, "You do not have permission to view this component.")
    
    user_info = get_user_info_from_token(request)
    license_id = user_info.get('license_id')
    
    component = get_object_or_404(Component, id=component_id)

    return component

@component_router.get("/download/{component_id}", auth=JWTAuth())
def download_component_file(request, component_id: int):
    user_info = get_user_info_from_token(request)
    component = get_object_or_404(Component, id=component_id)
    
    is_superuser = user_info.get('is_superuser', False)
    
    if is_superuser or str(component.element.chassis.license_id) == str(user_info.get('license_id')):
        if component.file and hasattr(component.file, 'path'):
            file_path = component.file.path
            if os.path.exists(file_path):
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
            else:
                raise Http404("File does not exist.")
        else:
            raise Http404("No file associated with this component.")
    else:
        raise HttpError(403, "You do not have permission to download this file.")


@component_router.put("/{component_id}", response=ComponentSchema, auth=JWTAuth()) 
def update_component(request, component_id: int, data: ComponentUpdateSchema, file: UploadedFile = File(None)):
    user_info = get_user_info_from_token(request)
    component = get_object_or_404(Component, id=component_id)
    element = get_object_or_404(Element, id=component.element_id)
    chassis = get_object_or_404(Chassis, id=element.chassis_id)

    if not user_info.get('is_superuser') and str(chassis.license_id) != str(user_info.get('license_id')):
        raise Http404("You do not have permission to update this component.")

    for attribute, value in data.dict(exclude_none=True).items():
        setattr(component, attribute, value)

    if file and component.file:
        if default_storage.exists(component.file.name):
            default_storage.delete(component.file.name)
    
    if file:
        component.file = file

    component.save()
    return component



@component_router.delete("/{component_id}", response={204: None}, auth=JWTAuth())
def delete_component(request, component_id: int):
    user_info = get_user_info_from_token(request)
    component = get_object_or_404(Component, id=component_id)
    element = get_object_or_404(Element, id=component.element_id)
    chassis = get_object_or_404(Chassis, id=element.chassis_id)

    if not user_info.get('is_superuser', False) and str(chassis.license_id) != str(user_info.get('license_id')):
        raise Http404("You do not have permission to delete this component.")

    if component.file:
        file_path = component.file.path
        if os.path.exists(file_path):
            os.remove(file_path)
    
    component.delete()
    return 204, None
