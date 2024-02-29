from django.contrib.auth import authenticate
from django.conf import settings
import jwt
from datetime import datetime, timedelta
from ninja import Router
from ninja.errors import HttpError
from prototyping.schemas.login_schema import AuthSchema

login_router = Router()

@login_router.post("/")
def login(request, auth_data: AuthSchema):
    user = authenticate(email=auth_data.email, password=auth_data.password)
    if user:
        expiration_time = datetime.utcnow() + timedelta(days=1)
        token = jwt.encode({
            'email': user.email,
            'exp': expiration_time
        }, settings.SECRET_KEY, algorithm='HS256')
        return {"token": token}
    else:
        raise HttpError(401, {"error": "Invalid credentials"})
