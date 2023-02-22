import os

import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = 'MTA3Nzg1OTg0MTY2MzU3NDA5Ng.GKFrXU.enKsS0YtI5WRLU0MqEiar_zGVOUKuaALv8kV_U'
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hello candle':
        await message.channel.send('hello')
client.run(TOKEN)