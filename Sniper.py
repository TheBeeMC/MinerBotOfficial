import discord
from discord.ext import commands
import random
import asyncio
import time
import os


client = discord.Client()

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('Fuck'):
        await client.delete_message(msg)

@client.event
async def on_ready():
      await client.change_presence(activity=discord.Game(name="& Cave mining ⛏"))



client.run(os.getenv('TOKEN'))
