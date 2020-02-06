import sys
import discord
import random
import asyncio
import time
import datetime
import urllib.request
import json
import re
import os
import traceback
import math
client = discord.Client()
from discord.ext import tasks
from datetime import datetime, timedelta, timezone


TOKEN = os.environ['DISCORD_BOT_TOKEN']

JST = timezone(timedelta(hours=+9), 'JST')

test_flag = False
test_ch = None
fb_flag = False
m_num = 0
stop_num = 0
revive_num = 0
start_time = None
monster_name = None
all_damage = 0
atk_num = -1
all_exp = 0


@tasks.loop(seconds=10)
async def loop():
    global stop_num
    if test_flag==True:
        tao=client.get_user(526620171658330112)
        if tao:
            def test_check (d_msg):
                if d_msg.author != tao:
                    return 0
                if d_msg.channel!=test_ch:
                    return 0
                return 1

            try:
                t_res=await client.wait_for('message', timeout=20, check = test_check)
            except asyncio.TimeoutError:
                stop_num+=1
                await test_ch.send(f'::i m')

            else:
                pass

@client.event
async def on_ready():
    global test_ch
    start_ch = client.get_channel(615550825732767775)
    await start_ch.send(datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S"))
    print(datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S"))
    loop.start()

@client.event
async def on_message(message):
    me = client.user
    amano = client.get_user(446610711230152706)
    tao = client.get_user(526620171658330112)

    global m_num
    global stop_num
    global revive_num
    global atk_num
    global monster_name
    global all_damage
    global fb_flag
    global test_flag
    global test_ch
    global start_time
    global all_exp

    sent = "None"
    if not atk_num== 0:
        sent = f"\n**現在ノ討伐数**：`{m_num}`\n**停止検知回数**：`{stop_num}`\n**死亡復活回数：**`{revive_num}`\n**総ダメージ数：**`{all_damage}`\n**単発平均火力：**`{(round((all_damage)/(atk_num)))}`\n**総獲得経験値：**`{all_exp}`"


    if message.content=='a)stop' and test_flag==True and message.author==me:
        test_flag=False
        test_ch=None
        await message.channel.send(f'**__Auto Battle System Stop__**\n**戦闘開始時刻**：{start_time}\n**総合敵討伐数**：{m_num}\n**停止検知回数**：{stop_num}\n**死亡復活回数**：{revive_num}')
        
    if message.content.startswith("a)start") and message.author==me:
        test_flag = True
        test_ch = message.channel
        start_time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
        await message.channel.send(f'**Auto Battle System Start**\n**開始時刻：**{datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")}')
        if test_ch:
            await test_ch.send(f'::attack ')

    if message.channel==test_ch and test_flag==True and message.author == tao:
        if f"{me.name}の攻撃" in message.content:
            if not 'かわされてしまった' in message.content:
                atk_num+=1
                all_damage+=int((message.content.split(f'{monster_name}に')[1]).split('のダメージ')[0])

        if f"{me.name}はやられてしまった" in message.content:
            revive_num+=1
            await asyncio.sleep(0.2)
            await test_ch.send('::item e　復活')

        elif f"{me.name}の攻撃" in message.content and f"{amano.name}のHP" in message.content and not f"{me.name}はやられてしまった" in message.content:           
            await asyncio.sleep(0.2)
            if fb_flag == True:
                await test_ch.send(f"::item f {sent}")
            else:
                await test_ch.send(f"::attack {sent}")


    if message.channel==test_ch and test_flag==True and message.author == me:

        if message.content.startswith('::item f') and fb_flag==True:
            def remsg_check(msg):
                if msg.author!=tao:
                    return 0
                elif msg.channel!=test_ch:
                    return 0
                elif not 'のHP' in msg.content:
                    return 0
                return 1
            try:
                res_msg=await client.wait_for('message',timeout=10,check=remsg_check)
            except asyncio.TimeoutError:
                stop_num+=1
                await test_ch.send(f'::item f {sent}')
            else:
                pass
 
        if message.content.startswith('::attack'):
            def remsg_check(msg):
                if msg.author!=tao:
                    return 0
                elif msg.channel!=test_ch:
                    return 0
                elif not f'{me.name}の攻撃' in msg.content:
                    return 0
                return 1
            try:
                res_msg=await client.wait_for('message',timeout=10,check=remsg_check)
            except asyncio.TimeoutError:
                stop_num+=1
                await test_ch.send(f'::attack {sent}')
            else:
                pass
 


    if message.channel == test_ch and message.embeds and test_flag==True:

        if message.embeds[0].description and f'{me.mention}はもうやられている' in message.embeds[0].description:
            await asyncio.sleep(0.2)
            await test_ch.send('::item e')

        elif message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:
            monster_name=((message.embeds[0].title).split('】\n')[1]).split('が待ち構えている')[0]
            await asyncio.sleep(0.25)
            m_num+=1
            if "超激レア" in message.embeds[0].title:
                if not "狂気ネコしろまる" in message.embeds[0].title:
                    await test_ch.send(f"::item f {sent}")
                    fb_flag = True
                else:
                    await test_ch.send(f"::attack {sent}")

            else:
                await test_ch.send(f"::attack {sent}")


            """
            pgui.hotkey('ctrl','v')
            pgui.typewrite('attack')
            pgui.press('enter', presses=1, interval=0.5)
            pgui.keyDown('enter')
            pgui.keyUp('enter')
            """

        if message.embeds[0].description and '回復' in message.embeds[0].description or 'UNBAN' in message.embeds[0].description:
            await asyncio.sleep(0.2)
            await test_ch.send(f'::attack {sent}')


        if message.embeds[0].title and '戦闘結果' in message.embeds[0].title:
            fb_flag = False
            all_exp+=int(((message.embeds[0].description).split(f'{me.mention}は')[1]).split('経験値')[0])

    if message.channel==test_ch and test_flag==True:
        if not message.author in [tao,me]:
            log_ch = client.get_channel(674753156109828109)
            await log_ch.send(embed = discord.Embed(title = 'test_ch発言ログ', description = f'**発言者**\n{message.author}\n**時刻**\n{datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")}\n内容\n{message.content}'))
      

@client.event
async def on_message_edit(before,after):
    if after.channel==test_ch:
        if 'BAN' in after.content:
            await asyncio.sleep(0.2)
            await test_ch.send('::i m')
    if after.embeds and after.embeds[0].description and after.channel == test_ch and "仲間に" in after.embeds[0].description:
        if  not 'ミニ' in after.embeds[0].description and "クルーエル" in after.embeds[0].description or "超激レア" in after.embeds[0].description:
            await after.add_reaction("👍")
        else:
            await after.add_reaction("👎")


client.run(TOKEN,bot=False)
