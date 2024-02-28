from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List, Optional
from prototyping.schemas.component_schema import ComponentIn, ComponentOut  
from prototyping.models.component_model import Component  

component_router = Router()

@component_router.post("/", response={201: ComponentOut}, tags=["Components"])
def create_component(request, component_in: ComponentIn):
    component = Component.objects.create(**component_in.dict())
    return component

@component_router.get("/", response=List[ComponentOut], tags=["Components"])
def read_component(request, component_id: Optional[int] = None, name: Optional[str] = None):
    if component_id:
        component = get_object_or_404(Component, id=component_id)
        return [component]  
    elif name:
        components = Component.objects.filter(name__icontains=name)
        return components
    else:
        components = Component.objects.all()
        return components

@component_router.put("/{component_id}", response=ComponentOut, tags=["Components"])
def update_component(request, component_id: int, data: ComponentIn):
    component = get_object_or_404(Component, id=component_id)
    for attribute, value in data.dict().items():
        setattr(component, attribute, value)
    component.save()
    return component

@component_router.delete("/{component_id}", response={204: None}, tags=["Components"])
def delete_component(request, component_id: int):
    component = get_object_or_404(Component, id=component_id)
    component.delete()
    return None
