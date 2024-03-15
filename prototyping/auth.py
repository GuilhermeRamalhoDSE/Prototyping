from ninja.security import HttpBearer, APIKeyQuery
from ninja.errors import HttpError
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class JWTHeaderAuth(HttpBearer):
    def authenticate(self, request, token):
        return self.verify_jwt_token(token)

    def verify_jwt_token(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return User.objects.get(email=payload.get("email"))
        except Exception as e:
            raise HttpError(401, "Invalid token or user does not exist")

class JWTQueryAuth(APIKeyQuery):
    param_name = "token"  
    def authenticate(self, request, key):
        return self.verify_jwt_token(key)

    def verify_jwt_token(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return User.objects.get(email=payload.get("email"))
        except Exception as e:
            raise HttpError(401, "Invalid token or user does not exist")

