import discord
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('OutBot Online.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000) }ms.')

@client.command(pass_context=True)
async def announce(ctx,*,message,):
    embed = discord.Embed(title="Announcement",description=message,color=0x9208ea)
    embed.set_footer(text="Announcement made by OutdatedBot")
    await ctx.send(ctx.message.channel,embed=embed)


client.run("")
