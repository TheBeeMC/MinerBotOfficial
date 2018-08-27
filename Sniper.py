import discord
from discord.ext import commands
import random
import asyncio
import time
import os


class MyClient(commands.Bot):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return


        if message.content.startswith('https://'):
            await message.delete();

        if message.content.startswith('https//'):
            await message.delete();

        if message.content.startswith('cunt'):
            await message.delete();

        if message.content.startswith('CUNT'):
            await message.delete();

        if message.content.startswith('FUCK'):
            await message.delete();

        if message.content.startswith('Fuck'):
            await message.delete();

        if message.content.startswith('fuck'):
            await message.delete();

        if message.content.startswith('asshole'):
            await message.delete();

        if message.content.startswith('ASSHOLE'):
            await message.delete();

        if message.content.startswith('Loser'):
            await message.delete();

        if message.content.startswith('LOSER'):
            await message.delete();

        if message.content.startswith('kys'):
            await message.delete();

        if message.content.startswith('KYS'):
            await message.delete();

        if message.content.startswith('WHORE'):
            await message.delete();

        if message.content.startswith('whore'):
            await message.delete();

        if message.content.startswith('BITCH'):
            await message.delete();

        if message.content.startswith('bitch'):
            await message.delete();

        if message.content.startswith('NIGGER'):
            await message.delete();

        if message.content.startswith('nigger'):
            await message.delete();

        if message.content.startswith('fag'):
            await message.delete();

        if message.content.startswith('faggot'):
            await message.delete();

        if message.content.startswith('FAG'):
            await message.delete();

        if message.content.startswith('FAGGOT'):
            await message.delete();

        if message.content.startswith('Faggot'):
            await message.delete();


        if message.content.startswith('status'):
            await message.channel.send('Miner status: 🔴 Offline')


        if message.content.startswith('partner'):
            await message.channel.send('If you would like to partner please contact a Council staff or a Staff Member')
            await message.channel.send('We only accept partners around 40-50 channels minimum!')
            await message.channel.send('Remember that Miner Bot is a free discord bot!')
            await message.channel.send('If you spam the owner to partner you will be banned from the discord')
            await message.channel.send('Any suicidal / sexual discords or fake giveaways money will not be accepteble')
            await message.channel.send('And we will not partner with those kinds of servers')

        if message.content.startswith('ping'):
            await message.channel.send('Pong 🏓')

        if message.content.startswith('$test'):
            await message.channel.send('⛏  ***INVITE REWARDS***  ⛏')
            await message.channel.send('Invite 20 people to get Donators™')
            await message.channel.send('Donators has access to special commands, private servers, Private giveaways')
            await message.channel.send('Invite 50 people to get Ruby')
            await message.channel.send('Ruby has access to everything Donators has and access to Clash of Rescue capes and custom skins and gems')
            await message.channel.send('To get Premium it will cost 5$ PayPal')
            await message.channel.send('Has access to All Donator and Ruby perks! + Custom Private servers Clash of Rescue and partner cape, and more!')

        if message.content.startswith('$grind'):
            await message.channel.send('Guess any number. If you are correct you get gems [Remember it can be any numbers from 1 to 100000000] ***Miner bot made by @Captain#2713***')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 1000)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('Correct you have got 10 gems! To claim take a [screenshot and send it to a staff member so they can add it into #grind-gems-list] ***Miner bot made by @Captain#2713***')
            else:
                await message.channel.send('Sorry you have not got any gems! Better luck next time ***Miner bot made by @Captain#2713***')

bot = MyClient(command_prefix="$")

@bot.event
async def on_ready():
      await bot.change_presence(activity=discord.Game(name="& Cave mining ⛏"))



client.run(os.getenv('TOKEN'))
