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
    if message.content.startswith('/sfnanMAEms'):
            await bot.delete_message(message)
            embed = discord.Embed(title="#name-dropping-alert", description="The name `Bandit` is dropping and has received no queries on our Check Availability!", colour=0x1a94f0)
            embed.set_footer(text="Generated From: This is a automatic message")
            await bot.send_message(message.channel, embed=embed)
      
      
    if message.content.startswith('t2xm3oxX'):
            await bot.delete_message(message)
            embed = discord.Embed(title="#verify-yourself", description="Please be patience and wait until you are verified", colour=0x1a94f0)
            embed.add_field(name="`DatatError: Cannot add data property`", value="`user to be 'verified'``", inline=True)
            embed.set_footer(text="Generated From: #verify-wait")
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

      
    if message.content.startswith('.userhasbeenverifiedX2x'):
        await bot.delete_message(message)     
        embed=discord.Embed(title="Discord Verification", description="A discord account has succesfully been linked `By a Staff Member`!", color=0x1a94f0)
        embed.set_author(name='MCGiftSniper', icon_url="")
        embed.set_footer(text='Generated From: #verify-wait')
        await bot.send_message(message.channel, embed=embed)      
        
        
    if message.content.startswith('/rules'):
        embed=discord.Embed(title=":unamused: Do not @ping or direct message [DM] the Staff with unsolicited messages.", description="They are people too! Please treat them as such!  Besides, repeated distraction will only delay the next update.", color=0x1a94f0)
        embed.set_author(name='***Server Rules***', icon_url="")
        embed.add_field(name=":thumbsdown: The following is 100% prohibited:", value="Please respect the rules", inline=True)
        embed.set_footer(text='Thread posted by Captain#2713')
        await bot.send_message(message.channel, embed=embed)         

    if message.content.startswith('/names'):
        await bot.send_message(message.channel, "The name `Bethany` is dropping and has received no queries on our availability checker!")
    
      
    if message.content.startswith('[CA] '):
        await bot.send_message(message.channel, "Yay, It is available. Go and queue it before someone else does! `Please notice this is not yet done and it is in currenty progress`")

    if message.content.startswith('https://'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, ".gift warn {0.author.mention} `for posting links in chat`".format(message))
        embed=discord.Embed(title="Warning System", description="User has been warned for `posting links in chat`!", color=0x1a94f0)
        embed.set_author(name='MCGiftSniper', icon_url="")
        embed.set_footer(text='Generated From: This is a automatic message')
        await bot.send_message(message.channel, embed=embed)
        
    if message.content.startswith('http://'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, ".gift warn {0.author.mention} `for posting links in chat`".format(message))
        embed=discord.Embed(title="Warning System", description="User has been warned for `posting links in chat`!", color=0x1a94f0)
        embed.set_author(name='MCGiftSniper', icon_url="")
        embed.set_footer(text='Generated From: This is a automatic message')
        await bot.send_message(message.channel, embed=embed)    
        
    if message.content.startswith('https:/'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, ".gift warn {0.author.mention} `for posting links in chat`".format(message))
        embed=discord.Embed(title="Warning System", description="User has been warned for `posting links in chat`!", color=0x1a94f0)
        embed.set_author(name='MCGiftSniper', icon_url="")
        embed.set_footer(text='Generated From: This is a automatic message')
        await bot.send_message(message.channel, embed=embed)          
      
@bot.event
async def on_ready():
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Somewhere in the database"))
        
bot.run(os.getenv('TOKEN'))
