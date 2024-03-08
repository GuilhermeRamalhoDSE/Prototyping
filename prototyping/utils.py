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

    is_superuser = user_info.get('is_superuser', False) in [True, 'True', 'true', 1, '1']

    if is_superuser:
        return True

    if user_id is not None:
        user = get_object_or_404(User, id=user_id)

        if user.license_id != user_info.get('license_id'):
            return False  

    if user_info.get('license_id') is not None:
        return True 

    return False
