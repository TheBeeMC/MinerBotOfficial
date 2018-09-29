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

    if message.content.startswith('soon lol ok'):
        await bot.delete_message(message)
        embed=discord.Embed(title="**11/1/2018 @ 1:04:04 PM**", description="The name `pigeon` has dropped but that name has already been taken by someone else already!", colour=0x1a94f0)
        embed.set_author(name='Name Drop Alert 🚨', icon_url="")
        embed.set_footer(text="https://chearful.ninja/#")
        await bot.send_message(message.channel, embed=embed)
        
        
        




@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    await bot.change_presence(game=discord.Game(name="https://namemc.com/minecraft-names?length_op=&length=3&lang=en&searches=100"))
    
bot.run(os.getenv('TOKEN'))
