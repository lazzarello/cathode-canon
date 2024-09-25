import discord
import os
from dotenv import load_dotenv

load_dotenv()

# channel_id = os.environ['CHANNEL_ID']
token = os.environ['DISCORD_TOKEN']
channel_id = 0
username = os.environ['DISCORD_USERNAME']
schedule = os.environ['DISCORD_CHANNEL']
limit = None 
filename = "messages.txt"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        for channel in self.get_all_channels():
            if channel.name == schedule:
                channel_id = channel.id
                break
        channel = self.get_channel(channel_id)
        # https://discordpy.readthedocs.io/en/stable/api.html#discord.TextChannel.history
        # channel history is only about 500K and saves in a few seconds, nbd!
        with open(filename, 'w') as file:
            messages = [message async for message in channel.history(limit=limit, oldest_first=True)]
            for message in messages:
                if message.author.name == username:
                    file.write(f'{message.created_at} : {message.content}\n')
                    # print(f'{message.created_at} : {message.content}\n')

intents = discord.Intents.default()
intents.messages = True
discord.Permissions.read_message_history = True
client = MyClient(intents=intents)
client.run(token)