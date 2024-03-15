from ninja.security import HttpBearer
from ninja.errors import HttpError
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings


User = get_user_model()


class JWTAuth(HttpBearer):
    def authenticate(self, request, token=None):
        if token is None:
            token = request.headers.get('Authorization')
            if token and token.startswith("Bearer "):
                token = token[7:]  
        
        if token is None:
            token = request.GET.get('token')
        
        if not token:
            raise HttpError(401, "Authentication token not provided")
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_email = payload.get("email")
            user = User.objects.get(email=user_email)
            
            if payload.get("is_superuser", False) != user.is_superuser:
                raise HttpError(403, "Access denied")
            
            return user
        except jwt.ExpiredSignatureError:
            raise HttpError(401, "Token has expired")
        except jwt.DecodeError:
            raise HttpError(401, "Error decoding token")
        except User.DoesNotExist:
            raise HttpError(401, "User does not exist")
