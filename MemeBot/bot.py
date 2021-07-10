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

@client.event
async def on_ready():
    print("ready")



async  def text_only(subr_choices,ctx):
    x=random.choice(subr_choices)
    subreddit= await reddit.subreddit(x)
    all_subs=[]

    
    async for submission in subreddit.hot(limit=50):
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    text=''.join(random_sub.selftext)
    text=text[:4096]
    embed = discord.Embed(title=name, url=random_sub.url,
                            description=text,
                           color=discord.Color.random(),
                           )
    await ctx.send(embed=embed)


async def img_txt(subr_choices,ctx):
    x=random.choice(subr_choices)
    subreddit= await reddit.subreddit(x)
    all_subs=[]

    
    async for submission in subreddit.hot(limit=50):
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    embed = discord.Embed(title=name, url=random_sub.url,
                            #description=text,
                           color=discord.Color.random(),
                           )
    embed.set_image(url=random_sub.url)
    await ctx.send(embed=embed)


@client.command()
async def r(ctx, type=''):
    if(type=="sr"):
        subr_choices=["Semenretention"]  #insert subreddits of your choice here
        await text_only(subr_choices,ctx)

    elif(type=="bnews"):
        subr_choices=["investing","personalfinance"]  #insert subreddits of your choice here
        await text_only(subr_choices,ctx)

    elif(type=="progmemes"):
        subr_choices=["ProgrammerHumor","programmingmemes"]  #insert subreddits of your choice here
        await img_txt(subr_choices,ctx)

client.run(disc_token)

