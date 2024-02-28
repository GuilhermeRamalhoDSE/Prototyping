from ninja import Router, Query
from typing import List
from django.shortcuts import get_object_or_404
from prototyping.models.license_models import License
from prototyping.schemas.license_schema import LicenseSchema, LicenseCreateSchema, LicenseUpdateSchema


license_router = Router(tags=['Licenses'])

@license_router.post("/licenses/", response={201: LicenseSchema})
def create_license(request, payload: LicenseCreateSchema):
    license_obj = License.objects.create(**payload.dict())
    return LicenseSchema.from_orm(license_obj)

@license_router.get("/licenses/", response=List[LicenseSchema])
def read_licenses(request, license_id: int = Query(None), name: str = Query(None)):
    filters = {}
    if license_id is not None:
        filters['id'] = license_id
    if name:
        filters['name__icontains'] = name

    licenses = License.objects.filter(**filters)
    return [LicenseSchema.from_orm(license) for license in licenses]

@license_router.put("/licenses/{license_id}/", response=LicenseSchema)
def update_license(request, license_id: int, payload: LicenseUpdateSchema):
    license_obj = get_object_or_404(License, id=license_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(license_obj, attr, value)
    license_obj.save()
    return LicenseSchema.from_orm(license_obj)

@license_router.delete("/licenses/{license_id}/")
def delete_license(request, license_id: int):
    license_obj = get_object_or_404(License, id=license_id)
    license_obj.delete()
    return {"success": True}
