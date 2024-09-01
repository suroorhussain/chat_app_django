from rest_framework import serializers

from .models import (
    Conversations,
    Messages
)

from account.models import User

class MemberSerisalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']

class MessageSerializer(serializers.ModelSerializer):
    sender = MemberSerisalizer()
    class Meta:
        model = Messages
        fields = ['sender', 'message', 'id', 'created_at']

class ConversationSerializer(serializers.ModelSerializer):
    members = MemberSerisalizer(many=True)
    class Meta:
        model = Conversations
        fields = [
            'name',
            'type',
            'members',
            'id',
            'unread_messages',
        ]