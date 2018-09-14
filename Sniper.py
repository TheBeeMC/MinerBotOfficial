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
            await bot.delete_message(message)
            embed = discord.Embed(title="#name-dropping-alert", description="The name `Jeans` is dropping and has received no queries on our Check Availability!", colour=0x1a94f0)
            embed.set_footer(text="Generated From: This is a automatic message")
            await bot.send_message(message.channel, embed=embed)
      
      
    if message.content.startswith('t2xm3oxX'):
            await bot.delete_message(message)
            embed = discord.Embed(title="#verify-yourself", description="To verify yourself please check settings and find a code like `.verify (CODE)` Please notice this isn't yet done as the website isn't 100% Up!", colour=0x1a94f0)
            embed.set_footer(text="Generated From: This is a automatic message")
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

      
    if message.content.startswith('.verify'):
        embed=discord.Embed(title="Discord Verification", description="Your discord account has not been succesfully linked `Please use .verify (CODE)`!", color=0x1a94f0)
        embed.set_author(name='Dragonfruit', icon_url="https://orig00.deviantart.net/89b1/f/2018/119/7/6/dragon_fruit_pixel_art_by_hikary_starrysky-dca5kt8.png")
        embed.set_footer(text='Generated From: Dragonfruit Bot')
        await bot.send_message(message.channel, embed=embed)      
        
        
    if message.content.startswith('/rules'):
        embed=discord.Embed(title=":unamused: Do not @ping or direct message [DM] the Staff with unsolicited messages.", description="They are people too! Please treat them as such!  Besides, repeated distraction will only delay the next update.", color=0x1a94f0)
        embed.set_author(name='***Server Rules***', icon_url="")
        embed.add_field(name=":thumbsdown: The following is 100% prohibited:", value="Please respect the rules", inline=True)
        embed.set_footer(text='Thread posted by Captain#2713')
        await bot.send_message(message.channel, embed=embed)         

    if message.content.startswith('/names'):
        await bot.send_message(message.channel, "The name `really` is dropping and has received no queries on our availability checker!")
       
      
      
    if message.content.startswith('[CA] '):
        await bot.send_message(message.channel, "Yay, It is available. Go and queue it before someone else does! `Please notice this is not yet done and it is in currenty progress`")



@bot.event
async def on_ready():
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
    await bot.change_presence(game=discord.Game(name="Somewhere in the database"))
        
bot.run(os.getenv('TOKEN'))
