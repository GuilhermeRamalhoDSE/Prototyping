from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List,  Optional
from prototyping.schemas.release_schema import ReleaseIn, ReleaseOut 
from prototyping.models.release_models import Release

release_router = Router(tags=["Releases"])

@release_router.post("/", response={201: ReleaseOut})
def create_release(request, release_in: ReleaseIn):
    file_obj = request.FILES.get('file')
    release = Release.objects.create(**release_in.dict(), file=file_obj)
    return release

@release_router.get("/", response=List[ReleaseOut])
def read_releases(request, client_id: Optional[int] = None, project_id: Optional[int] = None):
    filters = {}
    if client_id:
        filters['client_id'] = client_id
    if project_id:
        filters['project_id'] = project_id
    
    releases = Release.objects.filter(**filters)
    return releases

@release_router.put("/{release_id}", response=ReleaseOut)
def update_release(request, release_id: int, data: ReleaseIn):
    release = get_object_or_404(Release, id=release_id)
    for attribute, value in data.dict().items():
        if attribute != 'file':
            setattr(release, attribute, value)
    if 'file' in request.FILES:
        release.file = request.FILES.get('file')
    release.save()
    return release

@release_router.delete("/{release_id}", response={204: None})
def delete_release(request, release_id: int):
    release = get_object_or_404(Release, id=release_id)
    release.delete()
    return None
