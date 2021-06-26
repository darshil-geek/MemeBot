import discord
import praw
from discord.colour import Color

from discord.ext import commands

client=commands.Bot(command_prefix='cd ',description=None)

@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="Current Version", description="The bot version is 1.0",Color=0x00ff00)
    myEmbed.add_field(name="Version Code: ",value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released: ", value="25th June 2021",inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Darshil Shah")

    await context.message.channel.send(embed=myEmbed)

@client.command(name="ping")
async def ping(context):
    await context.message.channel.send("cd pong")




@client.event
async def on_ready():
    general_channel=client.get_channel(850599495023591454)
    await general_channel.send("The bot is online")




async def on_message(self,message):
    
    if message.content== "RAMDI.ping":
        await message.channel.send("RAMDI.pong")
        
client.run('ODU3OTUyMjM1OTEyNDI5NTY5.YNXESQ.zsCcEJYzRyepzfY23tvNyd3ReZs')

