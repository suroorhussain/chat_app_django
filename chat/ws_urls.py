from django.urls import re_path

from . import consumers

urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chat/dm/(?P<username>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chat/group/(?P<groupid>[0-9a-f-]+)/$', consumers.ChatConsumer.as_asgi()),
]