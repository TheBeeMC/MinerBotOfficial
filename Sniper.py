# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

command_prefix='$'
bot = commands.Bot(command_prefix)
description = 'Miner Bot™ @ coded by Captain#2713'
 
@bot.event
async def on_message(message):
    if message.content.startswith('$status'):
            embed = discord.Embed(title="Miner Bot Status: 🔵 Online", description="Everything is healthy", colour=0x1a94f0)
            embed.set_footer(text="Miner Bot™ @ coded by Captain#2713")
            await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('+help'):
        embed=discord.Embed(title="Miner Bot Help", description="+invite: Prints an invite link for the bot.", color=0x1a94f0)
        embed.set_author(name='Commands', icon_url="")
        embed.add_field(name="+help: Brings up list of commands", value="+info: Prints info about the bot.", inline=True)
        embed.set_footer(text='Miner Bot™ @ coded by Captain#2713')
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('+Loltest'):
        await bot.send_message(message.channel, "")
        print('Bot has been added to new server')

    if message.content.startswith('+info'):
        await bot.send_message(message.channel, "Miner Bot™ @ coded by Captain#2713")

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name="Miner"))

@bot.event
async def on_ready():
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
        
bot.run(os.getenv('TOKEN'))
