from channels.consumer import AsyncConsumer

class ChatAppConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        self.group = self.scope['url_route']['kwargs']['group']
        await self.channel_layer.group_add(self.group,self.channel_name)
        await self.send({
            'type':'websocket.accept'
        })
    async def websocket_receive(self,event):
         print(event)
         await self.channel_layer.group_send(self.group,{
             'type':'chat.messages',
             'message':event['text']
         })
    async def chat_messages(self,event):
        await self.send({
            'type':'websocket.send',
            'text':event['message'],
        })
        
    async def websocket_disconnect(self,event):
        await self.send({
            'type':'websocket.disconnect'
        })