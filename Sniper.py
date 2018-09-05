# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

bot = commands.Bot(command_prefix='/')

 
@bot.event
async def on_message(message):
    if message.content.startswith('/status'):
            embed = discord.Embed(title="Apple Temp", description="Everything is healthy", colour=0x1a94f0)
            embed.set_footer(text="Miner Bot™ @ coded by Captain#2713")
            await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('/help'):
        embed=discord.Embed(title="***Miner Bot Help***", description="Bot Cost: 5$", color=0x1a94f0)
        embed.set_author(name='Commands', icon_url="")
        embed.add_field(name="***Coming soon***", value="/status to check if Miner is online", inline=True)
        embed.set_footer(text='Miner Bot Status: 🔵 Online')
        await bot.send_message(message.channel, embed=embed)
        
        
        
    if message.content.startswith('/payment'):
        embed=discord.Embed(title="***Miner Bot Payment**", description="Miner Bot cost 5$ and there is no refund⛏", color=0x1a94f0)
        embed.set_author(name='Why choose Miner Bot? Because its fun and can make your server active! It can roast you and block words', icon_url="")
        embed.add_field(name=":thumbsdown: The following is 100% prohibited:", value="Why? Because it protects it from getting it leaked", inline=True)
        embed.set_footer(text='Thread posted by Captain#2713')
        await bot.send_message(message.channel, embed=embed)           

      
    if message.content.startswith('/verify'):
        embed=discord.Embed(title="Discord Verification", description="Your Discord account will now be under staff approval", color=0x1a94f0)
        embed.set_author(name='Apple Temp', icon_url="https://orig00.deviantart.net/369f/f/2008/282/3/9/8_bit_apple_day_by_monketron.jpg")
        embed.add_field(name="Please be patience because staff have to review", value="This could take up to 1 day to be verified", inline=True)
        embed.set_footer(text='Verified on 00/00/0000')
        await bot.send_message(message.channel, embed=embed)      
        
        
    if message.content.startswith('/rules'):
        embed=discord.Embed(title=":unamused: Do not @ping or direct message [DM] the Staff with unsolicited messages.", description="They are people too! Please treat them as such!  Besides, repeated distraction will only delay the next update.", color=0x1a94f0)
        embed.set_author(name='***Server Rules***', icon_url="")
        embed.add_field(name=":thumbsdown: The following is 100% prohibited:", value="Please respect the rules", inline=True)
        embed.set_footer(text='Thread posted by Captain#2713')
        await bot.send_message(message.channel, embed=embed)         

    if message.content.startswith('/names'):
        await bot.send_message(message.channel, "Minecraft Username: **Really** Availability 10/12/2018 @ 8:53:55 AM")

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
