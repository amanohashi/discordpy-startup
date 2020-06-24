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

@client.event
async def on_ready():
    print("ready")


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
