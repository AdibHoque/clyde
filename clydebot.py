import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix=commands.when_mentioned_or('c!'))

@bot.event
async def on_ready():
	print('working')
	
def is_owner(ctx):
    return ctx.message.author.id == "488353416599306270"

@bot.command(pass_context = True)
@commands.check(is_owner)     
async def dmall(ctx,*, msg:str=None):
    if msg is None:
      await bot.say('Not sent')
      return
    else: 
      for user in ctx.message.server.members:
        try:
          await bot.send_message(user, msg)
          await asyncio.sleep(1)
          
@bot.command(pass_context = True)
async def help_1(ctx):
	await bot.say('no u')
	
bot.run(os.getenv('Token'))
