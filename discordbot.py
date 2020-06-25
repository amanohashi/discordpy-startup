ID_CHANNEL_README = 724173902338588774 # 該当のチャンネルのID
ID_ROLE_WELCOME = 724175515929411606 # 付けたい役職のID

import discord
import asyncio
import math
import random
import os
import re
import ast
import traceback
from datetime import datetime, timedelta, timezone
from discord.ext import tasks

JST = timezone(timedelta(hours=+9), 'JST')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
Guild = None

@client.event
async def on_ready():
    print("ready")
    global Guild
    Guild = client.get_guild(452832341912584243)


@client.event
async def on_message(msg):
    if msg.content == "+)ping":
        await msg.channel.send("Pong!!")


@client.event
async def on_member_join(member):
    CHANNEL_ID = 724179600392978442 #チャンネルID(int)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f'> + `{member}`参加')
    ch = client.get_channel(723119145079537705)
    await member.send(f"{member.mention}さん。**何鯖**へようこそ！\n{ch.mention}にて自己紹介をお願いします(o*。\_。)oペコッ")


@client.event
async def on_member_remove(member):
    CHANNEL_ID = 724179600392978442
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(f'> - `{member}`退出')


LOG_CH_ID = 725690840399347714    

@client.event
async def on_message_edit(defore, after):
    embed = discord.Embed(
        title="MessageEdited",
        description=f"**{defore.author}**"
    )
    embed.add_field(
        name="BeforeMessage",
        value=before.content
    )
    embed.add_field(
        name="AfterMessage",
        value=after.content
    )
    embed.timestump=datetime.now(JST)
    await client.get_channel(LOG_CH_ID).send(embed=embed)

    
    
@client.event
async def on_message_delete(message):
    embed = discord.Embed(
        title="MessageDelete",
        description=f"**{message.author}**"
    )
    embed.add_field(
        name="DeleteMessage",
        value=messag.content
    )
    embed.timestump=datetime.now(JST)
    await client.get_channel(LOG_CH_ID).send(embed=embed)

    
    
@client.event
async def on_raw_reaction_add(payload):

    # channel_id から Channel オブジェクトを取得
    channel = client.get_channel(payload.channel_id)

    # 該当のチャンネル以外はスルー
    if channel.id != ID_CHANNEL_README:
        return

    # guild_id から Guild オブジェクトを取得
    guild = client.get_guild(payload.guild_id)

    # user_id から Member オブジェクトを取得
    member = guild.get_member(payload.user_id)

    # 用意した役職IDから Role オブジェクトを取得
    role = guild.get_role(ID_ROLE_WELCOME)

    # リアクションを付けたメンバーに役職を付与
    await member.add_roles(role)

    # 分かりやすいように歓迎のメッセージを送る
    m = await channel.send(f'{role.mention}を{member.mention}に付与！')
    await asyncio.sleep(5)
    await m.delete()

client.run(token)
