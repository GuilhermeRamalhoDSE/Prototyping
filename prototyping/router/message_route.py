from ninja import Router
from django.shortcuts import get_object_or_404
from prototyping.models.message_models import Message
from prototyping.schemas.message_schema import MessageIn, MessageOut, UserOut
from prototyping.auth import QueryTokenAuth, HeaderTokenAuth

message_router = Router(tags=["Messages"])

@message_router.post("/", response={201: MessageOut}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def create_message(request, message_in: MessageIn):
    message = Message.objects.create(**message_in.dict())
    return 201, message

@message_router.get("/", response=list[MessageOut], auth=[QueryTokenAuth(), HeaderTokenAuth()])
def read_messages(request):
    messages = Message.objects.all()
    result = []
    for message in messages:
        user_data = UserOut(id=message.user.id, full_name=f"{message.user.first_name} {message.user.last_name}")
        message_data = MessageOut(
            id=message.id,
            content=message.content,
            created_at=message.created_at,
            user=user_data
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
