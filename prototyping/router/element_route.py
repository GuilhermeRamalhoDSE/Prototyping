from django.shortcuts import get_object_or_404
from ninja import Router
from typing import List, Optional
from prototyping.models.element_models import Element
from prototyping.schemas.element_schema import ElementIn, ElementOut
from prototyping.models.chassis_models import Chassis
from prototyping.auth import JWTAuth
from prototyping.utils import get_user_info_from_token, check_user_permission
from ninja.errors import HttpError

element_router = Router(tags=["Elements"])

@element_router.post("/", response={201: ElementOut}, auth=JWTAuth())
def create_element(request, payload: ElementIn):
    
    chassis = get_object_or_404(Chassis, id=payload.chassis_id)
    
    element = Element.objects.create(**payload.dict())
    return 201, element

@element_router.get("/", response=List[ElementOut], auth=JWTAuth())
def read_elements(request, chassis_id: Optional[int] = None):

    if not check_user_permission(request):
        raise HttpError(403, "You do not have permission to view these elements.")

    user_info = get_user_info_from_token(request)
    license_id = user_info.get('license_id')

    if chassis_id:

        if license_id is not None:
            chassis = get_object_or_404(Chassis, id=chassis_id, license_id=license_id)
        else:
            chassis = get_object_or_404(Chassis, id=chassis_id)

        elements = Element.objects.filter(chassis=chassis)
    else:
        raise HttpError(400, "Chassis ID is required.")

    return elements


@element_router.put("/{element_id}", response=ElementOut, auth=JWTAuth())
def update_element(request, element_id: int, payload: ElementIn):
    element = get_object_or_404(Element, id=element_id)
    for attr, value in payload.dict().items():
        setattr(element, attr, value)
    element.save()
    return element

@element_router.delete("/{element_id}", response={204: None}, auth=JWTAuth())
def delete_element(request, element_id: int):
    element = get_object_or_404(Element, id=element_id)
    element.delete()
    return {"message": "Element deleted successfully"}
