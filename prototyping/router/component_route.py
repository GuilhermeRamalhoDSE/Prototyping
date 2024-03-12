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

component_router = Router(tags=["Components"])

@component_router.post("/", response={201: ComponentSchema}, auth=JWTAuth()) 
def create_component(request, element_id: int, component_in: ComponentCreateSchema, file: UploadedFile = File(...)):
    user_info = get_user_info_from_token(request)
    element = get_object_or_404(Element, id=element_id)
    chassis = get_object_or_404(Chassis, id=element.chassis_id)

    if str(chassis.license_id) != str(user_info.get('license_id')):
        raise Http404("You do not have permission to add components to this element.")
    
    component = Component.objects.create(
        **component_in.dict(exclude_unset=True),
        element=element,
        file=file
    )
    return component

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

@component_router.put("/{component_id}", response=ComponentSchema, auth=JWTAuth()) 
def update_component(request, component_id: int, data: ComponentUpdateSchema, file: UploadedFile = File(None)):
    user_info = get_user_info_from_token(request)
    component = get_object_or_404(Component, id=component_id)
    element = get_object_or_404(Element, id=component.element_id)
    chassis = get_object_or_404(Chassis, id=element.chassis_id)

    if str(chassis.license_id) != str(user_info.get('license_id')):
        raise Http404("You do not have permission to update this component.")

    for attribute, value in data.dict(exclude_none=True).items():
        setattr(component, attribute, value)
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

    if str(chassis.license_id) != str(user_info.get('license_id')):
        raise Http404("You do not have permission to delete this component.")

    component.delete()
    return None
