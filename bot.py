import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '{Prefix}')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

client.run('{Token}')