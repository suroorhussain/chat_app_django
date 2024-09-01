from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated
)

from .serializers import ConversationSerializer

class IsMember(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()

class ConversationViewSet(ModelViewSet):

    def get_queryset(self):
        return self.request.user.conversations.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ConversationSerializer
        return ConversationSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'create']:
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated(), IsMember()]