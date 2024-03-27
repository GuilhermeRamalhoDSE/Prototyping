import os
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import prototyping.routing 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            prototyping.routing.websocket_urlpatterns
        )
    ),
})
