from ninja import Router
from typing import List, Optional
from django.shortcuts import get_object_or_404
from prototyping.schemas.component_release_schema import ComponentReleaseCreateSchema, ComponentReleaseSchema
from prototyping.models.component_release_models import ComponentRelease
from prototyping.auth import JWTAuth

component_release_router = Router(tags=["Component Release"])

@component_release_router.post("/", response={201: ComponentReleaseSchema}, auth=JWTAuth())
def create_component_release(request, payload: ComponentReleaseCreateSchema):
    component_release = ComponentRelease.objects.create(**payload.dict())
    return component_release

@component_release_router.get("/", response=List[ComponentReleaseSchema], auth=JWTAuth())
def read_component_releases(request, component_release_id: Optional[int] = None):
    if component_release_id:
        release = get_object_or_404(ComponentRelease, id=component_release_id)
        return [release]
    releases = ComponentRelease.objects.all()
    return releases

@component_release_router.put("/{component_release_id}", response=ComponentReleaseSchema, auth=JWTAuth())
def update_component_release(request, component_release_id: int, payload: ComponentReleaseCreateSchema):
    release = get_object_or_404(ComponentRelease, id=component_release_id)
    for attr, value in payload.dict().items():
        setattr(release, attr, value)
    release.save()
    return release

@component_release_router.delete("/{component_release_id}", response={204: None}, auth=JWTAuth())
def delete_component_release(request, component_release_id: int):
    release = get_object_or_404(ComponentRelease, id=component_release_id)
    release.delete()
    return None