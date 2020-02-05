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

m_num = 0
client = discord.Client()


TOKEN = os.environ['DISCORD_BOT_TOKEN']

from discord.ext import tasks

from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

test_flag = False
test_ch = None
fb_flag = False
stop_num = 0


@tasks.loop(seconds=30)
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
                t_res=await client.wait_for('message', timeout=60, check = test_check)
            except asyncio.TimeoutError:
                stop_num+=1
                await test_ch.send(f'::attack \n**討伐数**：{m_num}\n**停止検知回数**：{stop_num}')

            else:
                pass

@client.event
async def on_ready():
    global test_ch
    start_ch = client.get_channel(615550825732767775)
    await start_ch.send(datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S"))
    print(datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S"))
    
    """
    pgui.click(50,50)
    pgui.typewrite('start')
    """
    loop.start()

@client.event
async def on_message(message):
    me = client.user
    amano = client.get_user(446610711230152706)
    tao = client.get_user(526620171658330112)


    global m_num
    global fb_flag
    global test_flag
    global test_ch

    if message.content.startswith("a)start"):
        test_flag = True
        test_ch = message.channel
        await message.channel.send("Auto Battle System Start")
        if test_ch:
            await test_ch.send(f'::attack {datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")}')

    if message.channel==test_ch and test_flag==True and message.author == tao:
        if f"{me.name}はやられてしまった" in message.content:
            await asyncio.sleep(0.2)
            await test_ch.send('::item e　復活')

        elif f"{me.name}の攻撃" in message.content and f"{amano.name}のHP" in message.content and not f"{me.name}はやられてしまった" in message.content:
            await asyncio.sleep(0.2)
            if fb_flag == True:
                await test_ch.send(f"::item f \n**討伐数**：{m_num}\n**停止検知回数**：{stop_num}")
            else:
                await test_ch.send(f"::attack \n**討伐数**：{m_num}\n**停止検知回数**：{stop_num}")


    if message.channel == test_ch and message.embeds and test_flag==True:

        if message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:
            await asyncio.sleep(0.4)
            m_num+=1
            if "超激レア" in message.embeds[0].title:
                if not "狂気ネコしろまる" in message.embeds[0].title:
                    await test_ch.send(f"::item f \n**討伐数**：{m_num}\n**停止検知回数**：{stop_num}")
                    fb_flag = True
                else:
                    await test_ch.send(f"::attack \n**討伐数**：{m_num}\n**停止検知回数**：{stop_num}")

            else:
                await test_ch.send(f"::attack \n**討伐数**：{m_num}\n**停止検知回数**：{stop_num}")

            """
            pgui.hotkey('ctrl','v')
            pgui.typewrite('attack')
            pgui.press('enter', presses=1, interval=0.5)
            pgui.keyDown('enter')
            pgui.keyUp('enter')
            """

        if message.embeds[0].description and '回復' in message.embeds[0].description:
            await asyncio.sleep(0.2)
            await test_ch.send(f'::attack 復活')


        if message.embeds[0].title and '戦闘結果' in message.embeds[0].title:
            fb_flag = False

 
@client.event
async def on_message_edit(before,after):
    if after.embeds and after.channel==test_ch:
        if 'Ban' in after.embeds[0].description or 'ban' in after.embeds[0].description :
            await asyncio.sleep(0.2)
            await test_ch.send('::i m')
    if after.embeds and after.channel == test_ch and "仲間に" in after.embeds[0].description:
        if  not 'ミニ' in after.embeds[0].description and "クルーエル" in after.embeds[0].description or "超激レア" in after.embeds[0].description:
            await after.add_reaction("👍")
        else:
            await after.add_reaction("👎")


client.run(TOKEN,bot=False)
