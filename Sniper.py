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
        
        
        
    if message.content.startswith('.apple mypunishments'):
        embed=discord.Embed(title="Punishments", description="[PUNISHMENTS] You do not have any current punishments", color=0x1a94f0)
        embed.set_author(name='Apple', icon_url="https://image.sportsmansguide.com/dimage/reticle_107_ts.gif")
        embed.set_footer(text='Generated at: Now / Today')
        await bot.send_message(message.channel, embed=embed)           

      
    if message.content.startswith('.apple verify o75oD8ujrH7VVxLj'):
        embed=discord.Embed(title="Discord Verification", description="Your Discord account has successfully been linked to `You are now under staff pending please wait until a staff checks`!", color=0x1a94f0)
        embed.set_author(name='Apple', icon_url="https://image.sportsmansguide.com/dimage/reticle_107_ts.gif")
        embed.set_footer(text='Generated at: Now / Today')
        await bot.send_message(message.channel, embed=embed)      
        
        
    if message.content.startswith('/rules'):
        embed=discord.Embed(title=":unamused: Do not @ping or direct message [DM] the Staff with unsolicited messages.", description="They are people too! Please treat them as such!  Besides, repeated distraction will only delay the next update.", color=0x1a94f0)
        embed.set_author(name='***Server Rules***', icon_url="")
        embed.add_field(name=":thumbsdown: The following is 100% prohibited:", value="Please respect the rules", inline=True)
        embed.set_footer(text='Thread posted by Captain#2713')
        await bot.send_message(message.channel, embed=embed)         

    if message.content.startswith('/names'):
        await bot.send_message(message.channel, "The name `really` is dropping and has received no queries on our availability checker!")
      
      
    if message.content.startswith('.error'):
        await bot.send_message(message.channel, "`TypeError: Cannot read property 'length' of undefined`")



@bot.event
async def on_ready():
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
        
bot.run(os.getenv('TOKEN'))
