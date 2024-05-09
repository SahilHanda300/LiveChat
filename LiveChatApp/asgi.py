"""
ASGI config for LiveChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import LiveChat.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LiveChatApp.settings')

application = ProtocolTypeRouter(
    {
    'http':get_asgi_application(),
    'websocket':URLRouter(
         LiveChat.routing.url_routing
     )
    } 
)
