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
        
        
    if message.content.startswith('/miner'):
        embed=discord.Embed(title="https://discord.gg/kJGFfKA", description="⛏", color=0x1a94f0)
        embed.set_author(name='Miner Bot Discord: 👷', icon_url="")
        embed.add_field(name="https://discord.io/Miner", value="Want to buy the bot? Join our discord and pm Captain#2713", inline=True)
        embed.set_footer(text='Miner Bot Status: 🔵 Online')
        await bot.send_message(message.channel, embed=embed)  
        
    if message.content.startswith('/payment'):
        embed=discord.Embed(title="***Miner Bot Payment**", description="Miner Bot cost 5$ and there is no refund⛏", color=0x1a94f0)
        embed.set_author(name='Why choose Miner Bot? Because its fun and can make your server active! It can roast you and block words', icon_url="")
        embed.add_field(name="How to purchase? Pm Captain#2713 once you purchased you must give me Administrator so I can add it.", value="Why? Because it protects it from getting it leaked", inline=True)
        embed.set_footer(text='Thread posted by Captain#2713')
        await bot.send_message(message.channel, embed=embed)           

      
    if message.content.startswith('<3'):
        await bot.delete_message           
        await bot.send_message(message.channel, ":heart: ")      

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
