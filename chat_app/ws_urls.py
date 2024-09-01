from django.urls import re_path

from channels.routing import URLRouter

urlpatterns = [
    re_path('ws/chat/', URLRouter('chat.ws_urls')),
] 