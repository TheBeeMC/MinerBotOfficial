import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["FUCK", "BITCH", "SHIT", "FAG", "FAGGOT", "FUCKER", "ASS", "ASSHOLE", "NIGGA", "NIGER", "NIGA", "CUNT", "L", "LOSER", "BAD"]
bypass_list = []



@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Bot**: Hey no swearing out here ok?")
                    await client.send_message(message.channel, "**You**: https://media1.tenor.com/images/b531fcefb582e156b994a6765ee47dc7/tenor.gif?itemid=5658414")
                except discord.errors.NotFound:
                    return

 
      
@client.event
async def on_ready():
    print('No Swearing Bot #1')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + client.user.name + ', ' + client.user.id)
    await client.change_presence(game=discord.Game(name="#1 No Swearing Bot"))
        
client.run(os.getenv('TOKEN'))
