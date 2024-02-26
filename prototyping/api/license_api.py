from ninja import NinjaAPI, Query
from typing import List
from django.shortcuts import get_object_or_404
from prototyping.models.license_models import LicenseManagementDse
from prototyping.schemas.license_schema import LicenseSchema, LicenseCreateSchema, LicenseUpdateSchema

api = NinjaAPI()

@api.post("/licenses/", response=LicenseSchema, tags=['Licenses'])
def create_license(request, payload: LicenseCreateSchema):
    license_obj = LicenseManagementDse.objects.create(**payload.dict())
    return LicenseSchema.from_orm(license_obj)

@api.get("/licenses/", response=List[LicenseSchema], tags=['Licenses'])
def read_licenses(request, customer_id: int = Query(None), name: str = Query(None)):
    filters = {}
    if customer_id is not None:
        filters['customer_id'] = customer_id
    if name:
        filters['name__icontains'] = name

    licenses = LicenseManagementDse.objects.filter(**filters)
    return [LicenseSchema.from_orm(license) for license in licenses]

@api.put("/licenses/{customer_id}/", response=LicenseSchema, tags=['Licenses'])
def update_license(request, customer_id: int, payload: LicenseUpdateSchema):
    license_obj = get_object_or_404(LicenseManagementDse, customer_id=customer_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(license_obj, attr, value)
    license_obj.save()
    return LicenseSchema.from_orm(license_obj)

@api.delete("/licenses/{customer_id}/", tags=['Licenses'])
def delete_license(request, customer_id: int):
    license_obj = get_object_or_404(LicenseManagementDse, customer_id=customer_id)
    license_obj.delete()
    return {"success": True}

