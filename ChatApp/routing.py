from . import consumers
from django.urls import path

url_routing = [
    path("ws/sc/<str:group>/",consumers.ChatAppConsumer.as_asgi())
]