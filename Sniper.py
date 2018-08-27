import discord
from discord.ext import commands
import random
import asyncio
import time
import os


Client = discord.Client()

client = commands.Bot(command_prefix = "?")

chat_filter = ["FUCK", "CUNT", "BITCH", "DICK", "KYS", "FAGGOT", "FUCKING", "NIGGER", "NIGGA", "WHORE", "ASS", "KILL YOUR SELF"]
bypass_list = []

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** Don't swear 😡 Thank you")
                except discord.errors.NotFound:
                    return

@client.event
async def on_ready():
      await client.change_presence(game=discord.Game(name="& Cave mining ⛏"))
        
        
        
@client.event
async def on_message(message):
    if message.content.lower().startswith("ping"):
        await client.send_message(message.channel, "PONG 🏓")
        
        
    if message.content.lower().startswith("giveaway"):
        emb - (discord.Embed(description="React with 🎉 to enter!", colour=0x3DF270))
        emb - (discord.Embed(description="Time remaining: Random time", colour=0x3DF270))
        emb - (discord.Embed(description="Ends at • Random Time PM/ AM", colour=0x3DF270))                                  
        emb.set_author(name="Premium Rank Giveaway")
        await client.add_reaction(botmsg, "🎉")                                  
        await client.send_messafe(message.channel, embed=em)                              

    if message.content.lower().startswith("test"):
        botmsg = await client.send_message(message.channel, "👍 oder 👎")

        await client.add_reaction(botmsg, "👍")
        await client.add_reaction(botmsg, "👎")

        global testmsgid
        testmsgid = botmsg.id

        global testmsguser
        testmsguser = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    chat = reaction.message.channel

    if reaction.emoji == "👍" and msg.id == testmsgid and user == testmsguser:
        await client.send_message(chat, "Daumen Hoch")

    if reaction.emoji == "👎" and msg.id == testmsgid and user == testmsguser:
        await client.send_message(chat, "Daumen Runter")




client.run(os.getenv('TOKEN'))
