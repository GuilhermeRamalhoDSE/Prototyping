from typing import List, Optional
from ninja import Router
from django.shortcuts import get_object_or_404
from prototyping.models.client_models import Client
from prototyping.schemas.client_schema import ClientIn, ClientOut
from prototyping.auth import JWTAuth

client_router = Router(tags=["Clients"])

@client_router.post("/", response={201: ClientOut}, auth=JWTAuth())
def create_client(request, payload: ClientIn):
    Client = Client.objects.create(**payload.dict(), auth=JWTAuth())
    return Client

@client_router.get("/", response=List[ClientOut], auth=JWTAuth())
def read_client(request, Client_id: Optional[int] = None, name: Optional[str] = None):
    if Client_id:
        return [get_object_or_404(Client, id=Client_id)]
    if name:
        return list(Client.objects.filter(name__icontains=name))
    return list(Client.objects.all())

@client_router.put("/{client_id}", response=ClientOut, auth=JWTAuth())
def update_client(request, client_id: int, payload: ClientIn):
    client = get_object_or_404(Client, id=client_id)
    for attr, value in payload.dict().items():
        setattr(client, attr, value)
    client.save()
    return Client

@client_router.delete("/{client_id}", response={204: None}, auth=JWTAuth())
def delete_client(request, client_id: int):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return {"success": True}
