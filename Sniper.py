import discord
from discord.ext import commands
import random
import asyncio
import time
import os



Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["FUCK", "CUNT", "BITCH", "DICK", "KYS", "FAGGOT", "FUCKING", "NIGGER", "NIGGA", "WHORE", "ASS", "KILL YOUR SELF", "IDIOT", "DUMBASS", "LOSER", "NIGER", "***KYS***", "***FAGGOT***", "***K Y S***", "***LOSER***"]
bypass_list = []



@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** We don't allow swearing 😡 Thank you")
                except discord.errors.NotFound:
                    return
                
                
                
        if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))
      
                        
                                 
@client.event
async def on_ready():
      await client.change_presence(game=discord.Game(name="Purchase Miner for 5$ ⛏"))
        
        
        
      
        
client.run(os.getenv('TOKEN'))
