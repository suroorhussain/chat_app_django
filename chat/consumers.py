import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync

from . import utils

from pprint import pprint

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        pprint(self.scope['url_route']['kwargs'])
        user = self.scope["user"]
        if user.is_anonymous:
            await self.close()
        else:
            self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
            print(self.conversation_id)
            if await utils.is_valid_conversation_id(user, self.conversation_id):
                await self.channel_layer.group_add(self.conversation_id, self.channel_name)
                await self.accept()
            else:
                await self.close()

    async def disconnect(self, close_code):
        if getattr(self, 'conversation_id', None):
            await self.channel_layer.group_discard(self.conversation_id, self.channel_name)
        else:
            pass

    async def receive_json(self, content):
        message = content['message']
        sender = self.scope['user']

        await utils.save_message(self.conversation_id, sender, message)

        await self.channel_layer.group_send(
            self.conversation_id, {"type": "chat.message", "message": message, "sender": sender.username}
        )

    async def chat_message(self, event):
        print(event)
        message = event['message']
        sender = event['sender']

        await self.send_json({"message": message, "sender": sender})