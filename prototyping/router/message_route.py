from ninja import Router
from django.shortcuts import get_object_or_404
from prototyping.models.message_models import Message
from prototyping.schemas.message_schema import MessageIn, MessageOut
from prototyping.auth import QueryTokenAuth, HeaderTokenAuth

message_router = Router(tags=["Messages"])

@message_router.post("/", response={201: MessageOut}, auth=[QueryTokenAuth(), HeaderTokenAuth()])
def create_message(request, message_in: MessageIn):
    message = Message.objects.create(**message_in.dict())
    return 201, message

@message_router.get("/", response=list[MessageOut], auth=[QueryTokenAuth(), HeaderTokenAuth()])
def read_messages(request, q: str = None):
    if q:
        messages = Message.objects.filter(message__icontains=q).select_related('client', 'project', 'user')
    else:
        messages = Message.objects.all().select_related('client', 'project', 'user')
    return [MessageOut(**message.__dict__) for message in messages]

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
