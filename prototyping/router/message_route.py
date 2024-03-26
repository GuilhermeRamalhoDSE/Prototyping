from ninja import Router
from django.shortcuts import get_object_or_404
from prototyping.models.project_models import Project
from prototyping.models.message_models import Message
from prototyping.models.notification_models import Notification
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
        raise HttpError(404, "Project not found or invalid client")

    if not (is_superuser or is_staff or project.users.filter(id=user_id).exists()):
        raise HttpError(403, "Unauthorized user")

    message = Message.objects.create(
        client_id=message_in.client_id,
        project_id=message_in.project_id,
        user_id=user_id,
        message=message_in.message,
    )

    return 201, {
        "id": message.id,
        "client_id": message.client_id,
        "project_id": message.project_id,
        "user": {"id": user_id, "full_name": user_info.get('full_name')},
        "date": message.date,
        "message": message.message
    }
   
@message_router.get("/{project_id}", response=List[MessageOut], auth=[QueryTokenAuth(), HeaderTokenAuth()])
def read_messages(request, project_id: int):
    user_info = get_user_info_from_token(request)
    user_id = user_info.get('user_id')
    is_superuser = user_info.get('is_superuser', False)
    is_staff = user_info.get('is_staff', False)

    project = Project.objects.filter(id=project_id).first()
    if not project:
        raise HttpError(404, "Project not found")

    if not (is_superuser or is_staff or project.users.filter(id=user_id).exists()):
        raise HttpError(403, "Unauthorized user")

    messages_query = Message.objects.filter(project_id=project_id).select_related('user')
    result = []

    for message in messages_query:
        message_data = MessageOut(
            id=message.id,
            client_id=message.client.id,
            project_id=message.project.id,
            user=UserOut(id=message.user.id, full_name=f"{message.user.first_name} {message.user.last_name}"),
            date=message.date,
            message=message.message
        )
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

@message_router.get("/notifications", response=List[MessageOut], auth=[QueryTokenAuth(), HeaderTokenAuth()])
def get_unread_notifications(request) -> Any:
    user_info = get_user_info_from_token(request)
    user_id = user_info.get('user_id')

    unread_notifications = Notification.objects.filter(user_id=user_id, is_read=False).select_related('message')
    
    return [MessageOut.from_orm(notification.message) for notification in unread_notifications]

@message_router.get("/{project_id}/unread-count", response={200: int}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def get_project_unread_messages_count(request, project_id: int) -> Any:
    user_info = get_user_info_from_token(request)
    user_id = user_info.get('user_id')

    unread_count = Notification.objects.filter(
        message__project_id=project_id,
        user_id=user_id,
        is_read=False
    ).count()

    return 200, unread_count


@message_router.patch("/{message_id}/read", response={200: None}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def mark_message_as_read(request, message_id: int):
    user_info = get_user_info_from_token(request)
    user_id = user_info.get('user_id')

    Notification.objects.filter(message_id=message_id, user_id=user_id).update(is_read=True)

    return 200, None
