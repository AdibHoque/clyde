import discord
from discord.ext import commands
import asyncio
import os
from discord import Game, Embed, Color, Status, ChannelType

bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'))
bot.remove_command("help")

async def status_task():
	while True:
		await bot.change_presence(game=discord.Game(name='Pokémon on 598780 servers.'))
		await asyncio.sleep(696)
						
@bot.event
async def on_ready():
	print('working')
	bot.loop.create_task(status_task())
	
def is_owner(ctx):
    return ctx.message.author.id == "488353416599306270"

@bot.command(pass_context=True)
@commands.check(is_owner)
async def bal(ctx):
	print('Showing fake balance')
	await bot.purge_from(ctx.message.channel, limit = 1)
	embed=discord.Embed(title="!AD!B!'s Balance:",description='You currently have 10,084,069 credits.',color=0x00AE86)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/554964608130088980/580696234680123403/PokecordMoney.png')
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
@commands.check(is_owner)
async def redeem(ctx):
	print('Showing fake redeem')
	await bot.purge_from(ctx.message.channel, limit = 1)
	embed=discord.Embed(title="Your Redeems: 696💸",description="Redeems are a special type of currency that can be used to get either a pokémon of your choice, or 15000 credits.",color=0x00AE86)
	embed.add_field(name = '.redeem <pokémon>',value ='Use a redeem to obtain a pokémon of your choice.',inline = False)
	embed.add_field(name = '.redeem credits',value ='Use a redeem to obtain 15 000 credits.',inline = False)
	embed.set_footer(text='How do I get redeems? Type ".help redeem" to find out!')
	await bot.say(embed=embed)

bot.run(os.getenv('Token'))
