from channels.generic.websocket import AsyncWebsocketConsumer
import json


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "test"

        # Add this channel to the group asynchronously
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group when WebSocket disconnects
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Parse incoming message
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    async def chat_message(self, event):
        # Receive the message from the group and send it to WebSocket
        message = event["message"]

        await self.send(text_data=json.dumps({
            "type": "chat",
            "message": message
        }))
