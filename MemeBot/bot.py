from re import sub
import discord
#from praw.reddit import Submission
disc_token='' #enter ur discord bot token

import random
import asyncpraw
from discord.colour import Color

from discord.ext import commands

client=commands.Bot(command_prefix='.',description=None)

REDDIT_ENABLED_SUBREDDITS=['r/entrepreneur','r/investing','r/BusinessHub']


reddit=praw.Reddit(client_id='', #enter ur reddit app id
                    client_secret='',#enter ur secret reddit key
                    user_agent="trial"
)

subreddit= reddit.subreddit("desimemes")

@client.event
async def on_ready():
    print("ready")

@client.command()
async def sr(ctx):
    meme_choices=["Semenretention"]
    x=random.choice(meme_choices)
    subreddit= await reddit.subreddit(x)
    #top=subreddit.hot(limit=50)
    all_subs=[]

    
    async for submission in subreddit.hot(limit=50):
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    text=''.join(random_sub.selftext)
    
    embed = discord.Embed(title=name, url=random_sub.url,
                            description=text,
                           color=discord.Color.random(),
                           )
    await ctx.send(embed=embed)


@client.command()
async def bnews(ctx):
    meme_choices=["investing"]
    x=random.choice(meme_choices)
    subreddit= reddit.subreddit(x)
    top=subreddit.hot(limit=50)
    all_subs=[]

    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    text=''.join(random_sub.selftext)
    
    embed = discord.Embed(title=name, url=random_sub.url,
                            description=text,
                           color=discord.Color.random(),
                           )
    await ctx.send(embed=embed)

@client.command()
async def progmemes(ctx):
    meme_choices=["ProgrammerHumor","programmingmemes"]
    x=random.choice(meme_choices)
    subreddit= reddit.subreddit(x)
    top=subreddit.hot(limit=50)
    all_subs=[]

    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    embed = discord.Embed(title=name, url=random_sub.url,
                           color=discord.Color.random(),
                           )
    embed.set_image(url=random_sub.url)
    await ctx.send(embed=embed)


client.run(disc_token)

