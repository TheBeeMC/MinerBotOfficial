import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["FUCK", "BITCH", "SHIT"]
bypass_list = []




@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "{0.author.mention} chat has been removed for breaking the `Terms And Service`".format(message))
                    embed=discord.Embed(title="Status: 🔵 On", description="Chat has been removed for `Swearing`!", color=0x1a94f0)
                    embed.set_author(name='No Swearing Allowed', icon_url="")
                    embed.set_footer(text='Generated From: 21/9/2018')
                    await client.send_message(message.channel, embed=embed)     
                except discord.errors.NotFound:
                    return

 
      
@client.event
async def on_ready():
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + client.user.name + ', ' + client.user.id)
    await client.change_presence(game=discord.Game(name="#1 No Swearing Bot"))
        
client.run(os.getenv('TOKEN'))
