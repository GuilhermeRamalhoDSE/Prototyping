from ninja import Router, Query
from typing import List, Optional
from django.shortcuts import get_object_or_404
from prototyping.models.user_models import User
from prototyping.schemas.user_schema import UserSchema, UserCreateSchema
from prototyping.auth import JWTAuth

user_router = Router(tags=['Users'])

@user_router.post("/", response={201: UserSchema}, auth=JWTAuth())
def create_user(request, user_in: UserCreateSchema):
    user = User.objects.create(**user_in.dict())
    return user

@user_router.get("/", response=List[UserSchema], auth=JWTAuth())
def read_users(request, user_id: Optional[int] = Query(None)):
    if user_id:
        user = get_object_or_404(User, id=user_id)
        return [user]  
    users = User.objects.all()
    return users

@user_router.put("/{user_id}", response=UserSchema, auth=JWTAuth())
def update_user(request, user_id: int, data: UserCreateSchema):
    user = get_object_or_404(User, id=user_id)
    for attribute, value in data.dict().items():
        setattr(user, attribute, value)
    user.save()
    return user

@user_router.delete("/{user_id}", response={204: None}, auth=JWTAuth())
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return None
