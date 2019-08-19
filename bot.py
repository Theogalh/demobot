import discord
import os

TOKEN = os.getenv('TOKEN', None)
CHANNELS = list(map(int, os.getenv('CHANNELS', "").split(',')))

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    print(CHANNELS)
    if message.author == client.user:
        return
    if message.author.id == int(os.getenv('AUTHOR', 0)):
        message.author.send('TEST OK')
    if message.channel.id not in CHANNELS:
        return
    if message.content.startswith('[LFG]'):
        return
    msg = 'Hello {0.author.mention} \n' \
          'Pour poster un message dans ce channel, ton message doit commencer par [LFG]\n' \
          'Seuls les annonces sont acceptées, merci de ne pas répondre dans ce channel, ' \
          'mais répondre dans un autre channel ou en MP(modifié)\n'.format(message)
    await message.author.send(msg)
    await message.delete()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
