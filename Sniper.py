# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

command_prefix='/'
bot = commands.Bot(command_prefix)
description = 'Miner Bot™ @ coded by Captain#2713'
 
@bot.event
async def on_message(message):
    if message.content.startswith('/status'):
            embed = discord.Embed(title="Miner Bot Status: 🔵 Online", description="Everything is healthy", colour=0x1a94f0)
            embed.set_footer(text="Miner Bot™ @ coded by Captain#2713")
            await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('/help'):
        embed=discord.Embed(title="***Miner Bot Help***", description="Bot Cost: 5$", color=0x1a94f0)
        embed.set_author(name='Commands', icon_url="")
        embed.add_field(name="***Coming soon***", value="/status to check if Miner is online", inline=True)
        embed.set_footer(text='Miner Bot Status: 🔵 Online')
        await bot.send_message(message.channel, embed=embed)
        
        
    if message.content.startswith('lolgame'):
        embed=discord.Embed(title="***Miner Bot is now back online***", description="🔵", color=0x1a94f0)
        embed.set_author(name='Service: Healthy 🔵', icon_url="")
        embed.add_field(name="Thank you for your patience", value="Bot is now back online!", inline=True)
        embed.set_footer(text='Posted by Captain#2713')
        await bot.send_message(message.channel, embed=embed)        

      
    if message.content.startswith('fuck'):
        await bot.send_message(message.channel, "Try not swearing next time ok? 😡")      

    if message.content.startswith('/info'):
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
