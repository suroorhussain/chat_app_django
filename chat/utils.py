from django.db.models import Q

from channels.db import database_sync_to_async

from chat.models import Conversations

from account.models import User

@database_sync_to_async
def is_valid_conversation_id(user, conversation_id):
        conversation = Conversations.objects.filter(id=conversation_id, members__in=[user])
        return conversation.exists()

@database_sync_to_async
def save_message(conversation_id, user, message):
    conversation = Conversations.objects.get(id=conversation_id)
    message = conversation.messages.create(sender=user, message=message)
    conversation.save() # This changes the updated_at field of the conversation.
    return message