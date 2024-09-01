from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .import views

router = DefaultRouter()

router.register(r'conversations', views.ConversationViewSet, basename='conversations')

'''
re_path and the pk naming for the conversation_id is used so that views.IsMember 
can be reused for messages endpoint as well. This should be rewritten .
'''
urlpatterns = [
    re_path(r'conversations/(?P<pk>[^/.]+)/messages/', views.ListMessageView.as_view(), name='conversation_messages'),
]
urlpatterns += router.urls