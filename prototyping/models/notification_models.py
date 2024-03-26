from django.db import models
from prototyping.models.message_models import Message
from django.conf import settings

class Notification(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='notifications')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('message', 'user')
