import discord
import requests

#Variaveis principais e API da cotação
link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
intents = discord.Intents.all()
Client = discord.Client(command_prefix='!', intents=intents)

#Variaveis para moeda
moeda = requests.get(link)
moeda = moeda.json() 
moeda_dolar = moeda['USDBRL']['bid']
moeda_euro = moeda['EURBRL']['bid']
moeda_BTC = moeda['BTCBRL']['bid']


#Confirmação de Log do BOT
@Client.event
async def on_ready():
    print('Logamos como {0.user}'.format(Client))

#Respostas do BOT + Criação de mensagens
@Client.event
async def on_message(message):
  if message.author == Client.user:
    return
  
  if message.content.startswith("Oi"):
    await message.channel.send('Oi tudo bem? Eu sou o EconBot vou auxiliar você em busca de informações')

  if message.content.startswith("Dolar"):
     await message.channel.send(moeda_dolar)
  
  if message.content.startswith("Euro"):
     await message.channel.send(moeda_euro)
  
  if message.content.startswith("bitcoin"):
     await message.channel.send(moeda_BTC)

Client.run('Seu Discord Token')