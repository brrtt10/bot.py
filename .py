import discord
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command
async def hello(ctx):
    await ctx.send(f'Olá! eu sou o bot {bot.user}!')

@bot.command
async def bye(ctx):
    await ctx.send(f'Até a próxima {member.name} \U0001f642')

bot.run("MTQ2Njg4NTU3NjQ0MjUxMTQ5Mw.GEViBi.Cvyudhw2Qf66RQJx6Vs3obTmozOO6z-BcHEn_o")
