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
        embed=discord.Embed(title="***Payment Infos***", description="Bot Cost: 5$", color=0x1a94f0)
        embed.set_author(name='Commands', icon_url="")
        embed.add_field(name="Info: You will pay 5$ PayPal to @Captain once payment goes in with Friends & Family ONLY then you will invite me to your server and give me Administrator so I can add the bot itself. This is the only way for you to get the discord bot after purchase. Remember this is the only way to protect it from getting it leaked.s", value="+info: Prints info about the bot.", inline=True)
        embed.set_footer(text='Why chose Miner Bot? Because it is fun and I will be adding better things to it such as giveaways and polls and ping ms and more? Even get everyone active!!!')
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('FUCK'):
        await bot.send_message(message.channel, "Don't swear")
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
