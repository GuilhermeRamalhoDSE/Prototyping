from ninja import Router, Query
from typing import List, Optional
from django.shortcuts import get_object_or_404
from prototyping.models.user_models import User
from prototyping.schemas.user_schema import UserSchema, UserCreateSchema

user_router = Router()

@user_router.post("/users/", response={201: UserSchema}, tags=['Users'])
def create_user(request, user_in: UserCreateSchema):
    user = User.objects.create(**user_in.dict())
    return user

@user_router.get("/users/", response=List[UserSchema], tags=['Users'])
def read_users(request, user_id: Optional[int] = Query(None)):
    if user_id:
        user = get_object_or_404(User, id=user_id)
        return [user]  
    users = User.objects.all()
    return users

@user_router.put("/users/{user_id}/", response=UserSchema, tags=['Users'])
def update_user(request, user_id: int, data: UserCreateSchema):
    user = get_object_or_404(User, id=user_id)
    for attribute, value in data.dict().items():
        setattr(user, attribute, value)
    user.save()
    return user

@user_router.delete("/users/{user_id}/", response={204: None}, tags=['Users'])
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return None
