from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from prototyping.models.user_models import User
from prototyping.schemas.user_schema import UserSchema, UserCreateSchema, UserUpdateSchema
from prototyping.auth import JWTAuth
import jwt
from django.conf import settings
from prototyping.utils import check_user_permission, get_user_info_from_token
from django.http import HttpResponseForbidden

user_router = Router(tags=['Users'])

@user_router.post("/", response={201: UserSchema}, auth=JWTAuth())
def create_user(request, user_in: UserCreateSchema):
    user = User.objects.create(**user_in.dict())
    return user

@user_router.get("/", response=List[UserSchema], auth=JWTAuth())
def read_users(request):
    if not check_user_permission(request):
        return HttpResponseForbidden("You do not have permission to view these users.")
    
    user_info = get_user_info_from_token(request)
    license_id = user_info.get('license_id')
    
    users = User.objects.filter(license_id=license_id) if license_id else User.objects.all()
    return users

@user_router.put("/{user_id}", response=UserSchema, auth=JWTAuth())
def update_user(request, user_id: int, data: UserUpdateSchema):
    user = get_object_or_404(User, id=user_id)
    for attribute, value in data.dict(exclude_none=True).items():
        setattr(user, attribute, value)
    user.save()
    return user

@user_router.delete("/{user_id}", response={204: None}, auth=JWTAuth())
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return None
