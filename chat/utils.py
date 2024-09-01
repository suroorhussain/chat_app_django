from channels.db import database_sync_to_async

from chat.models import Conversations

from account.models import User

@database_sync_to_async
def get_conversation_id(user, groupid=None, username=None, **kwargs):
    if groupid:
        conversation = Conversations.objects.get(id=groupid, members__in=[user], type = Conversations.GROUP)
    else:
        recipient = User.objects.get(username=username)
        conversation = Conversations.objects.get_or_create(type=Conversations.DM, members__in=[user, recipient])
    return conversation.id