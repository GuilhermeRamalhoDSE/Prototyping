from django.contrib.auth import authenticate
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from ninja import Router, Query
from ninja.errors import HttpError
from prototyping.schemas.login_schema import AuthSchema, LoginResponseSchema

login_router = Router(tags=['Login'])

@login_router.api_operation(["GET", "POST"], response=LoginResponseSchema)
def login(request, auth_data: AuthSchema = None, email: str = Query(None), password: str = Query(None)):
    if request.method == "GET":
        if not email or not password:
            raise HttpError(400, "Email and password are required for login.")
        user_credentials = {'email': email, 'password': password}
    else:
        if not auth_data:
            raise HttpError(400, "Request body for login is missing.")
        user_credentials = {'email': auth_data.email, 'password': auth_data.password}

    user = authenticate(**user_credentials)
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
        raise HttpError(401, "Invalid credentials")
