from ninja import Router
from typing import List, Optional
from django.shortcuts import get_object_or_404
from prototyping.models.aptica_models import Aptica
from prototyping.models.license_models import License
from prototyping.schemas.aptica_schema import ApticaCreate, ApticaUpdate, ApticaOut
from ninja.errors import HttpError

aptica_router = Router()

@aptica_router.post("/", response={201: ApticaOut}, tags=["Aptica"])
def create_aptica(request, payload: ApticaCreate):
    license = get_object_or_404(License, id=payload.license_id)
    if request.user.is_superuser or request.user.license_id == license.id:
        aptica = Aptica.objects.create(**payload.dict(), license=license)
        return 201, aptica
    else:
        raise HttpError(403, "You do not have permission to perform this action.")

@aptica_router.get("/", response=List[ApticaOut], tags=["Aptica"])
def read_apticas(request, aptica_id: Optional[int] = None):
    if aptica_id:
        aptica = get_object_or_404(Aptica, id=aptica_id, license=request.user.license)
        return [aptica]
    else:
        if request.user.is_superuser:
            apticas = Aptica.objects.all()
        else:
            apticas = Aptica.objects.filter(license=request.user.license)
        return apticas


@aptica_router.put("/{aptica_id}", response=ApticaOut, tags=["Aptica"])
def update_aptica(request, aptica_id: int, payload: ApticaUpdate):
    aptica = get_object_or_404(Aptica, id=aptica_id, license=request.user.license)
    for attr, value in payload.dict().items():
        setattr(aptica, attr, value)
    aptica.save()
    return aptica

@aptica_router.delete("/{aptica_id}", response={204: None}, tags=["Aptica"])
def delete_aptica(request, aptica_id: int):
    aptica = get_object_or_404(Aptica, id=aptica_id, license=request.user.license)
    aptica.delete()
    return 204, None
