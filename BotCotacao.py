import discord

intents = discord.Intents.all()
Client = discord.Client(command_prefix='!', intents=intents)

@Client.event
async def on_ready():
    print('Logamos como {0.user}'.format(Client))

@Client.event
async def on_message(message):
  if message.author == Client.user:
    return
  
  if message.content.startswith("Oi"):
    await message.channel.send('Oi tudo bem? Eu sou o EconBot vou auxiliar você em busca de informações')

Client.run('MTA4MjQzMTA3MTg4MDIzMzAyMg.GGr25V.3z6mc0offaIWWHGnk_HqG8RyHqE9vbAxeQtkmg')