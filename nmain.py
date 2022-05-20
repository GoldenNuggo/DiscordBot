import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix = '!')

@bot.event
async def ready():
  print('Bot is ready.')

@bot.event
async def on_member_join(member):
  print(f'{member} has joined the server!')

@bot.event
async def on_member_remove(member):
  print(f'{member} has left the server')




# Activates the bot
bot.run('OTc0MjY4NzE2MjE5MDAyOTYw.GRcoRV.trIcl7gAXMkdjnUS-h5ikrKRkHcy-UyXlFfOr4')