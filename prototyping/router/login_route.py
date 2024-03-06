from django.contrib.auth import authenticate
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from ninja import Router
from ninja.errors import HttpError
from prototyping.schemas.login_schema import AuthSchema, LoginResponseSchema

login_router = Router()

@login_router.post("/", response=LoginResponseSchema)
def login(request, auth_data: AuthSchema):
    user = authenticate(email=auth_data.email, password=auth_data.password)
    if user:
        expiration_time = datetime.utcnow() + timedelta(days=1)
        
        # Define license_id dependendo se o usuário é superusuário ou não
        if not user.is_superuser and hasattr(user, 'license') and user.license is not None:
            license_id = user.license.id
        else:
            license_id = None  # Superusuários ou usuários sem license associado
        
        token = jwt.encode({
            'email': user.email,
            'exp': expiration_time,
            'license_id': license_id
        }, settings.SECRET_KEY, algorithm='HS256')
        
        return {
            "token": token,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            "license_id": license_id,
        }
    else:
        raise HttpError(401, {"error": "Invalid credentials"})
