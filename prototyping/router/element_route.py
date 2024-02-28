from django.shortcuts import get_object_or_404
from ninja import Router
from typing import List, Optional
from prototyping.models.element_models import Element
from prototyping.schemas.element_schema import ElementIn, ElementOut

element_router = Router(tags=["Elements"])

@element_router.post("/", response={201: ElementOut})
def create_element(request, payload: ElementIn):
    element = Element.objects.create(**payload.dict())
    return element

@element_router.get("/", response=List[ElementOut])
def read_elements(request, name: Optional[str] = None, id: Optional[int] = None):
    query = Element.objects.all()
    if name:
        query = query.filter(name__icontains=name)
    if id:
        query = query.filter(id=id)
    return query

@element_router.put("/{element_id}", response=ElementOut)
def update_element(request, element_id: int, payload: ElementIn):
    element = get_object_or_404(Element, id=element_id)
    for attr, value in payload.dict().items():
        setattr(element, attr, value)
    element.save()
    return element

@element_router.delete("/{element_id}")
def delete_element(request, element_id: int):
    element = get_object_or_404(Element, id=element_id)
    element.delete()
    return {"message": "Element deleted successfully"}
