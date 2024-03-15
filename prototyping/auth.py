from ninja.security import HttpBearer
from ninja.errors import HttpError
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings
import logging

# Obtém o modelo de usuário padrão do Django
User = get_user_model()

# Configura o logger para este módulo
logger = logging.getLogger(__name__)

class JWTAuth(HttpBearer):
    def authenticate(self, request, token=None):
        logger.info("Iniciando autenticação JWT...")

        # Se um token não foi fornecido diretamente, tenta obter da query string
        if token is None:
            token = request.GET.get('token')
            if token:
                logger.info(f"Token obtido da query string: {token}")
            else:
                logger.error("Token não fornecido.")
                raise HttpError(401, "Authentication token not provided")

        try:
            # Decodifica o token usando a chave secreta e o algoritmo HS256
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_email = payload.get("email")

            # Tenta obter o usuário pelo e-mail fornecido no payload do token
            user = User.objects.get(email=user_email)

            # Verifica se a flag de superusuário no token corresponde à do usuário
            if payload.get("is_superuser", False) != user.is_superuser:
                logger.error("Acesso negado.")
                raise HttpError(403, "Access denied")

            # Se tudo estiver correto, retorna o usuário autenticado
            return user

        except jwt.ExpiredSignatureError:
            logger.error("Token expirado.")
            raise HttpError(401, "Token has expired")
        except jwt.DecodeError:
            logger.error("Erro ao decodificar o token.")
            raise HttpError(401, "Error decoding token")
        except User.DoesNotExist:
            logger.error("Usuário não existe.")
            raise HttpError(401, "User does not exist")
