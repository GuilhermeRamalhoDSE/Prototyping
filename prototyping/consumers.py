import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from prototyping.models.message_models import Message
from prototyping.models.client_models import Client
from prototyping.models.project_models import Project
from prototyping.models.user_models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_id

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = text_data_json['user_id']
        project_id = text_data_json['project_id']
        client_id = text_data_json['client_id']
        user_full_name = text_data_json.get('user_full_name')  

        await self.save_message(user_id, project_id, client_id, message, user_full_name)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user_id': user_id,
                'user_full_name': user_full_name,
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']
        user_full_name = event['user_full_name']

        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'user_full_name': user_full_name,
            'message': message
        }))
    
    @database_sync_to_async
    def save_message(self, user_id, project_id, client_id, message_text, user_full_name):
        user = User.objects.get(id=user_id)
        project = Project.objects.get(id=project_id)
        client = Client.objects.get(id=client_id)
        created_message = Message.objects.create(user=user, project=project, client=client, message=message_text)
