from ninja import Router
from django.shortcuts import get_object_or_404
from prototyping.models.project_models import Project
from prototyping.models.message_models import Message
from prototyping.schemas.message_schema import MessageIn, MessageOut, UserOut
from prototyping.auth import QueryTokenAuth, HeaderTokenAuth
from prototyping.utils import get_user_info_from_token
from typing import List, Any
from ninja.errors import HttpError

message_router = Router(tags=["Messages"])

@message_router.post("/", response={201: MessageOut})
def create_message(request, message_in: MessageIn) -> Any:
    user_info = get_user_info_from_token(request)
    user_id = user_info.get('user_id')
    is_superuser = user_info.get('is_superuser', False)
    is_staff = user_info.get('is_staff', False)

    project = Project.objects.filter(id=message_in.project_id, client_id=message_in.client_id).first()
    if not project:
        raise HttpError(404, "Projeto não encontrado ou cliente inválido")

    if not (is_superuser or is_staff or project.users.filter(id=user_id).exists()):
        raise HttpError(403, "Usuário não autorizado")

    message = Message.objects.create(
        client_id=message_in.client_id,
        project_id=message_in.project_id,
        user_id=user_id,
        message=message_in.message
    )

    return 201, {
        "id": message.id,
        "client_id": message.client_id,
        "project_id": message.project_id,
        "user": {"id": user_id, "full_name": user_info.get('full_name')},
        "date": message.date,
        "message": message.message
    }

    
@message_router.get("/{project_id}", response=list[MessageOut])
def read_messages(request, project_id: int):
    user_info = get_user_info_from_token(request)
    user_id = user_info.get('user_id')
    is_superuser = user_info.get('is_superuser', False)
    is_staff = user_info.get('is_staff', False)

    project = Project.objects.filter(id=project_id).first()
    if not project:
        raise HttpError(404, "Projeto não encontrado")

    if not (is_superuser or is_staff or project.users.filter(id=user_id).exists()):
        raise HttpError(403, "Usuário não autorizado")

    messages_query = Message.objects.filter(project_id=project_id).select_related('user')
    result = []

    for message in messages_query:
        user_data = {
            "id": message.user.id,
            "full_name": f"{message.user.first_name} {message.user.last_name}"
        }
        message_data = {
            "id": message.id,
            "client_id": message.client.id,
            "project_id": message.project.id,
            "user": user_data,
            "date": message.date,
            "message": message.message
        }
        result.append(message_data)
    
    return result

@message_router.put("/{message_id}", response={200: MessageOut}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def update_message(request, message_id: int, payload: MessageIn):
    message = get_object_or_404(Message, id=message_id)
    for attr, value in payload.dict().items():
        setattr(message, attr, value)
    message.save()
    return 200, MessageOut.from_orm(message)

@message_router.delete("/{message_id}", response={204: None}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def delete_message(request, message_id: int):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return 204, None
