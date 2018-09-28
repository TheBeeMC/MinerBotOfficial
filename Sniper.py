# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

command_prefix='+'
bot = commands.Bot(command_prefix)
description = 'sniper.py, coded by unpredictable'
 
@bot.event
async def on_message(message):
    if message.content.startswith('+snipeadd'):
            embed = discord.Embed(title="Let's walk you through the process of queueing a snipe.", description="DM the bot with 'beginqueue' to queue your snipe.", colour=0x1a94f0)
            embed.set_author(name="Thanks for choosing sniper.py!", icon_url="")
            embed.add_field(name="Enjoy your new name!", value="-trinity and iliyan")
            embed.set_footer(text="sniper.py™ © coded by unpredictable")
            await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('+name'):
        embed=discord.Embed(title="**Generated At: 29/9/2018**", description="The name `Hacks` has dropped but have recieved information that the name is going to get changed back.", colour=0x1a94f0)
        embed.set_author(name='Name Drop Alert', icon_url="")
        await bot.send_message(message.channel, embed=embed)




@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    await bot.change_presence(game=discord.Game(name="https://namemc.com/minecraft-names?length_op=&length=3&lang=en&searches=100"))
    
bot.run(os.getenv('TOKEN'))
