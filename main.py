import discord
from discord.ext import commands
import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
from colorama import Fore
import os 


prefix = ("-")


RICHY = discord.Client()
RICHY = commands.Bot(description='IX EMBED', command_prefix=prefix,)





RICHY.remove_command('help')



@RICHY.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='INSANE X EMBED')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/840193188983341097/GLITCHO_GIF_20210507_171727.gif')
    embed.set_footer(text='IX OP')
    embed.add_field(name='___**INSANE X EMBED BOT**___', value='```COMMAND OF THIS IX EMBED | PREFIX = -```')
    embed.add_field(name='**-embed**', value='```JUST TYPE -embed (what ever the text is)```')
    await ctx.send(embed=embed) 

@RICHY.command()
async def embed(ctx, *, description):
    embed = discord.Embed(title='INSANE X EMBED', description=description)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/840193188983341097/GLITCHO_GIF_20210507_171727.gif')
    embed.set_footer(text='IX OP')
    await ctx.send(embed=embed)
    
print("IX EMBED IS READY!!! lmao")

RICHY.run(token, bot=True)
