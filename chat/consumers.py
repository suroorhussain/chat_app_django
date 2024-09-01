import json

from channels.generic.websocket import AsyncWebsocketConsumer

from asgiref.sync import async_to_sync

from . import utils

from pprint import pprint

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        pprint(self.scope['url_route']['kwargs'])
        user = self.scope["user"]
        if user.is_anonymous:
            await self.close()
        self.conversation_id = str(await utils.get_conversation_id(user, **self.scope['url_route']['kwargs']))

        await self.channel_layer.group_add(self.conversation_id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.conversation_id, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.conversation_id, {"type": "chat.message", "message": message}
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({'message': message}))