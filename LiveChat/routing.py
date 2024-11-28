from . import consumers
from django.urls import re_path  # Use re_path instead of path

# WebSocket routing
websocket_urlpatterns = [
    re_path(r'ws/sc/(?P<group>\w+)/$', consumers.ChatAppConsumer.as_asgi()),  # Using regular expression to capture the 'group' parameter
]