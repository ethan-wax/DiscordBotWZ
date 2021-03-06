import discord
import os
import requests

client = discord.Client()

@client.event
async def on_ready():
  print('The warzone bot is now online as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

    if message.content.startswith('!wz'):
      print('The warzone bot is still being created.')