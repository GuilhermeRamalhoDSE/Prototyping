from django.contrib.auth import authenticate
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from ninja import Router, Query
from ninja.errors import HttpError
from prototyping.schemas.login_schema import AuthSchema, LoginResponseSchema

login_router = Router(tags=['Login'])

@login_router.post("/", response=LoginResponseSchema)
def login_post(request, auth_data: AuthSchema):
    return authenticate_user(auth_data.email, auth_data.password)

@login_router.get("/", response=LoginResponseSchema)
def login_get(request, email: str = Query(...), password: str = Query(...)):
    return authenticate_user(email, password)

def authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user:
        expiration_time = datetime.utcnow() + timedelta(days=1)
        token = jwt.encode({
            'email': user.email,
            'exp': expiration_time,
            'is_superuser': user.is_superuser,
            'license_id': getattr(user, 'license_id', None) if not user.is_superuser else None,
        }, settings.SECRET_KEY, algorithm='HS256')

        return {
            "token": token,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            "license_id": getattr(user, 'license_id', None) if not user.is_superuser else None,
        }
    else:
        raise HttpError(401, {"error": "Invalid credentials"})
