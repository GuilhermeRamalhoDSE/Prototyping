import jwt
from django.conf import settings
from django.shortcuts import get_object_or_404
from prototyping.models.user_models import User

def get_user_info_from_token(request):
    token = request.headers.get('Authorization').split(' ')[1]
    decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    return decoded_token

def check_user_permission(request, user_id=None):
    user_info = get_user_info_from_token(request)

    # Verificando se é superusuário de forma robusta (considerando a possibilidade de valores "truthy")
    is_superuser = user_info.get('is_superuser', False) in [True, 'True', 'true', 1, '1']

    # Superusuários têm permissão irrestrita
    if is_superuser:
        return True

    # Se um user_id específico é fornecido, verificar se o usuário requisitante tem permissão para acessá-lo
    if user_id is not None:
        user = get_object_or_404(User, id=user_id)
        # Verificar se o usuário tem o mesmo license_id
        if user.license_id != user_info.get('license_id'):
            return False  # Sem permissão se os license_id não coincidem

    # Para usuários normais (não superusuários), garantir que tenham um license_id
    if user_info.get('license_id') is not None:
        return True  # Usuários com license_id têm permissão básica

    # Se nenhuma das condições acima for satisfeita, negar permissão
    return False
