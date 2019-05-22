import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'))

@bot.event
async def on_ready():
	print('working')
	
def is_owner(ctx):
    return ctx.message.author.id == "488353416599306270"

@bot.command(pass_context = True)
@commands.check(is_owner)     
async def bal(ctx):
    embed=discord.Embed(title="ADIB HOQUE's Balance:",description='You currently have 10,084,059 Credits',color=0x00AE86)
    embed.set_thumbnail(url= 'https://cdn.discordapp.com/attachments/554964608130088980/580696234680123403/PokecordMoney.png')
    await bot.say(embed=embed)
	
bot.run(os.getenv('Token'))
