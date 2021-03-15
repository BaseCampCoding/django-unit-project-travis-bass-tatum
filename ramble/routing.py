from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/(chat/public1\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/(chat/public2\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/(chat/public3\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/(chat/public4\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/(chat/public5\w+)/$', consumers.ChatConsumer.as_asgi()),
]