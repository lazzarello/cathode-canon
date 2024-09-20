import discord
import os
from dotenv import load_dotenv

load_dotenv()

# channel_id = os.environ['CHANNEL_ID']
token = os.environ['DISCORD_TOKEN']
channel_id = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        for channel in self.get_all_channels():
            if channel.name == 'schedule-pacific':
                channel_id = channel.id
                break
        channel = self.get_channel(channel_id)
        messages = [message async for message in channel.history(limit=100)]
        for message in messages:
           print(f'{message.author}: {message.content}')

intents = discord.Intents.default()
intents.messages = True
discord.Permissions.read_message_history = True
client = MyClient(intents=intents)
client.run(token)