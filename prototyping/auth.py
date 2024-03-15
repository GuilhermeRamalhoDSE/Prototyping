from ninja.security import HttpBearer
from ninja.errors import HttpError
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

class JWTAuth(HttpBearer):
    def authenticate(self, request, token=None):
        def test_authenticate(token):
            try:
                # Simule a lógica de decodificação e autenticação aqui
                 logger.info("Token:", token)
                # Insira aqui a lógica de decodificação do token
            except Exception as e:
                 logger.info("Erro durante a autenticação:", e)

        logger.info("Iniciando autenticação JWT...")
        if token is None:
            token = request.GET.get('token')
            logger.info(f"Token obtido da query string: {token}")
        if not token:
            logger.error("Token não fornecido.")
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
