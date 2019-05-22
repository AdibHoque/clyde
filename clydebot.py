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
    embed=discord.Embed(title="ADIB HOQUE's Balance:",description='You currently have 1,00,00,0000 credits',color=)
	
bot.run(os.getenv('Token'))
