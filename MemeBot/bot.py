from re import sub
import discord
#from praw.reddit import Submission
disc_token='' #enter ur discord bot token
reddit_sec='' #enter ur secret reddit key
reddit_app_id='' #enter ur reddit app id
import praw
import random
import asyncpraw
from discord.colour import Color

from discord.ext import commands

client=commands.Bot(command_prefix='!',description=None)

REDDIT_ENABLED_SUBREDDITS=['r/entrepreneur','r/investing','r/BusinessHub']


reddit=praw.Reddit(client_id='',        #enter ur reddit app id
                    client_secret='',  #enter ur secret reddit key
                    user_agent="trial"
)

#subreddit= reddit.subreddit("desimemes")

@client.event
async def on_ready():
    print("ready")

@client.command()
async def trial(ctx):
    subreddit= reddit.subreddit("IndianDankMemes")
    top=subreddit.hot(limit=50)
    all_subs=[]

    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    #url=random_sub.url
    #em=discord.Embed(title=name)
    #em.set_image(url=url)
    #await ctx.channel.send("Here's a link to the subreddit: \n{}".format(url))
    embed = discord.Embed(title=name, url=random_sub.url,
                           color=discord.Color.random(),
                           )
    embed.set_image(url=random_sub.url)
    await ctx.send(embed=embed)


client.run(disc_token)

