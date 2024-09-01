from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated
)

from . import serializers
from . import models

class IsMember(BasePermission):
    def has_object_permission(self, request, view):
        print("in persmission class")
        try:
            conversation = models.Conversations.objects.get(id=view.kwargs['pk'])
        except models.Conversations.DoesNotExist:
            return False
        return request.user in conversation.members.all()

class ConversationViewSet(ModelViewSet):

    serializer_class = serializers.ConversationSerializer
    def get_queryset(self):
        return self.request.user.conversations.all()
    
    def get_permissions(self):
        if self.action in ['list', 'create']:
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated(), IsMember()]
        
class ListMessageView(ListAPIView):
    serializer_class = serializers.MessageSerializer
    permission_classes = [IsAuthenticated & IsMember]
    
    def get_queryset(self):
        conversation_id = self.kwargs['pk']
        return self.request.user.conversations.get(id=conversation_id).messages.all()