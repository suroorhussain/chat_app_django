from rest_framework import serializers

from .models import (
    Conversations,
    Messages
)

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = ['name', 'type', 'members', 'id']