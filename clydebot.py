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
async def bal(ctx):
    embed=discord.Embed(title="ADIB HOQUE's Balance:",description='You currently have 1,00,00,0000 credits',color=0x00AE86)
    embed.set_thumbnail(url= 'https://cdn.discordapp.com/attachments/554964608130088980/580696234680123403/PokecordMoney.png')
    await bot.say(embed=embed)
	
bot.run(os.getenv('Token'))
