import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from prototyping.models.message_models import Message
from prototyping.models.client_models import Client
from prototyping.models.project_models import Project
from prototyping.models.notification_models import Notification
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
        action = text_data_json.get('action')

        if action == 'open_conversation':
            project_id = text_data_json['project_id']
            user_id = text_data_json['user_id']
            await self.mark_messages_as_read(project_id, user_id)
        else:
            message = text_data_json['message']
            user_id = text_data_json['user_id']
            project_id = text_data_json['project_id']
            client_id = text_data_json['client_id']
            user_full_name = text_data_json.get('user_full_name')

            if not user_full_name:
                user_full_name = await self.get_user_full_name(user_id)

            await self.save_message(user_id, project_id, client_id, message, user_full_name)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'user_id': user_id,
                    'user_full_name': user_full_name,
                    'message': message,
                    'project_id': project_id,
                }
            )

    @database_sync_to_async
    def mark_messages_as_read(self, project_id, user_id):
        Message.objects.filter(project_id=project_id, user_id=user_id, is_read=False).update(is_read=True)

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'user_id': event['user_id'],
            'user_full_name': event['user_full_name'],
            'message': event['message'],
            'project_id': event['project_id'],
        }))
    
    @database_sync_to_async
    def save_message(self, user_id, project_id, client_id, message_text, user_full_name):
        user = User.objects.get(id=user_id)
        user_full_name = user_full_name or f"{user.first_name} {user.last_name}"
        project = Project.objects.get(id=project_id)
        client = Client.objects.get(id=client_id)
        created_message = Message.objects.create(user=user, project=project, client=client, message=message_text)
        
        eligible_users = project.users.exclude(id=user_id)
        staff_users = User.objects.filter(is_staff=True)
        all_users_to_notify = set(eligible_users) | set(staff_users)
        
        notifications = [Notification(message=created_message, user=other_user) for other_user in all_users_to_notify]
        Notification.objects.bulk_create(notifications)

        for notification in notifications:
            self.channel_layer.group_send(
                f'user_{notification.user.id}',
                {
                    'type': 'receive_notification',
                    'message': f'Nova mensagem em {project.name}: "{message_text}"',
                    'from': user_full_name,
                    'project_id': project_id
                }
            )
    
    @database_sync_to_async
    def get_user_full_name(self, user_id):
        user = User.objects.get(id=user_id)
        return f"{user.first_name} {user.last_name}"

    async def receive_notification(self, event):
        await self.send(text_data=json.dumps(event))
