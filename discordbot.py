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

ready = False
test_flag = False
test_ch = None
fb_flag = False
FB_flag = False
m_num = 0
stop_num = 0
revive_num = 0
start_time = None
monster_name = None
all_damage = 0
atk_num = -1
all_exp = 0
lv = 0
em_desc = None
em_title = None
stop_skd = None
start_skd = None
check_flag = False

R = 0
SR = 0
SSR = 0
SSR_flag = False
kisei_flag = False
do_time = 0

#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－#

@client.event
async def on_ready():
    pass

#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－#

@tasks.loop(seconds=60)
async def loop():
    global test_flag
    global test_ch
    global SSR_flag
    global check_flag
    global stop_num
    global stop_skd
    global start_skd
    tao = client.get_user(526620171658330112)
    
    now = datetime.now(JST).strftime('%H:%M')
    if stop_skd or start_skd:
        print(f"{now} ≠ {stop_skd}")
        print(f"{now} ≠ {start_skd}")
    if now == '00:00':
        channel = client.get_channel(676499145208627201)
        await channel.send('::login') 
    if stop_skd and now == stop_skd:
        print(f"{now} = {stop_skd}")
        test_flag = False
        await asyncio.sleep(5)
        await test_ch.send("::re")
        await test_ch.send(f">>> **Auto Battle System Stop**\n`Time = {stop_skd}`")
        schedule_time = None
    
    if stop_skd and now == start_skd:
        print(f"{now} = {start_skd}")
        test_flag = True
        await test_ch.send("::attack")
        await test_ch.send(f">>> **Auto Battle System Start**\n`Time = {start_skd}`")
        start_skd = None
    

    if test_flag==True and SSR_flag == False:
        if tao :
            def test_check (tao_msg):
                if tao_msg.author != tao:
                    return 0
                if tao_msg.channel!=test_ch:
                    return 0
                return 1

            try:
                t_res=await client.wait_for(
                    'message',
                    timeout=10,
                    check = test_check
                )

            except asyncio.TimeoutError:
                if fb_flag == True or FB_flag == True:
                    await test_ch.send("::item f")
                else:
                    await test_ch.send("::attack 停止")
                stop_num+=1

            else:
                return


#－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－#
        
@client.event
async def on_message(message):
    global ready
    if not ready == True:
        ready = True
        log_ch = client.get_channel(676505024435585055)
        print (f'起動ログ\n{datetime.now(JST)}')
        embed = discord.embed(
            title = "起動ログ",
            description = datetime.now(JST).strflime("%Y/%M/%D %H:%M:%S"))
        embed.timestamp = datetime.now(JST)
        await log_ch.send(embed = embed)
        loop.start()
        return
    
    if not message.guild:
        return
    me = client.user
    amano = discord.utils.get(message.guild.members,id=446610711230152706)
    if not amano:
        return
    tao = discord.utils.get(message.guild.members,id=526620171658330112)


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
    global R
    global SR
    global SSR
    global SSR_flag
    global lv
    global check_flag
    global FB_flag
    global kisei_flag
    global do_time
    global em_desc
    global em_title
    global stop_skd
    global start_skd

    sent = "None"

    if message.embeds and message.embeds[0].description:
        em_desc = message.embeds[0].description

    if message.embeds and message.embeds[0].title:
        em_title = message.embeds[0].title

    if message.content.startswith('a)?user='):
        id = int(message.content.split('=')[1])
        user = client.get_user(id)
        m_ch = message.channel
        await m_ch.send(f">>> Checking ID『{id}』")
        if user:
            await message.channel.send(f'>>> **Found The User**\n『{user}』')
        else:
            await m_ch.send(">>> **Couldn't Found The User**")

    if not atk_num == 0:
        sent1 = f"**現在ノ討伐数：**`{m_num}`"

        if not R == 0:
            sent2 = f"**Ｒ　　出現数：**`{R}({(round((R/m_num)*10000))/100}％)`"
        else:
            sent2 = f"**Ｒ　　出現数：**`{R}(0%)`"

        if not SR == 0:
            sent3 = f"**ＳＲ　出現数：**`{SR}({(round((SR/m_num)*10000))/100}％)`"
        else:
            sent3 = f"**ＳＲ　出現数：**`{SR}(0%)`"

        if not SSR == 0:
            sent4 = f"**ＳＳＲ出現数：**`{SSR}({(round((SSR/m_num)*10000))/100}％)`"
        else:
            sent4 = f"**ＳＳＲ出現数：**`{SSR}(0%)`"

        sent5 = f"**総ダメージ数：**`{all_damage}({(round((all_damage)/(atk_num)))}/atk)`"
        sent6 = f"**総獲得経験値：**`{all_exp}`"
        sent7 = f'**総合ＬｖＵＰ：**`{lv}`'

        sent = f'\n{sent1}\n{sent2}\n{sent3}\n{sent4}\n{sent5}\n{sent6}\n{sent7}'


    if message.author == me:
        if message.content.startswith('a)on'):
            if 'fb' in message.content:
                FB_flag = True
                await message.channel.send(f'>>> **Set FB_flag**\n`{FB_flag}`')
            if 'kisei' in message.content:
                kisei_flag = True
                await message.channel.send(f'>>> **Set Kisei**\n`{kisei_flag}`')

        if message.content.startswith('a)off'):
            if 'fb' in message.content:
                FB_flag = False
                await message.channel.send(f'>>> **Set FB_flag**\n`{FB_flag}`')
            if 'kisei' in message.content:
                kisei_flag = False
                await message.channel.send(f'>>> **Set Kisei**\n`{kisei_flag}`')

        if message.content.startswith('a)set_speed '):
            do_time = float(message.content.split(' ')[1])
            text = f'>>> **Set Speed**\n`Speed = {do_time}s`'
            await message.channel.send(text)

        if message.content.startswith('a)set_skd '):
            schedule_time = message.content.split(" ")[1]
            if message.content.startswith("a)set_skd ~"):
                stop_skd = schedule_time.split('~')[0]
            elif "~" in message.content:
                stop_skd = schedule_time.split('~')[1]
                start_skd = schedule_time.split('~')[0]
                test_ch = message.channel
            else:
                start_skd =  message.content.split(" ")[1]
            text = (f">>> **Set Schedule**\n`Time = {start_skd} ~ {stop_skd}`")
            await message.channel.send(text)
            
        if message.content == 'a)represt':
            m_num = 0
            stop_num = 0
            revive_num = 0
            all_damage = 0
            atk_num = -1
            all_exp = 0
            lv = 0
            R = 0
            SR = 0
            SSR = 0
            await message.channel.send(f'**Reset Prest**')

    if message.content.startswith('a)prest') and not message.author.bot:
        await message.channel.send(f'{sent}')

    if message.content == 'a)login' and not message.author.bot:
        await message.channel.send('::login')

    if message.content=='a)stop':
        if not message.author==me and not message.author.guild_permissions.administrator:
            await message.author.send('スマンがこのコマンドは俺と鯖缶以外使えねえ…')
            return
        if test_flag==False:
            await message.channel.send(">>> **Macro System hasn't started**")
            return
        test_flag=False
        test_ch=None
        asent =  f"\n**現在ノ討伐数**\n`{m_num}`"
        asent += f"\n**停止検知回数**\n`{stop_num}`"
        asent += f"\n**死亡復活回数**\n`{revive_num}`"
        asent += f"\n**Ｒ　　出現数**\n`{R}`"
        asent += f"\n**ＳＲ　出現数**\n`{SR}`"
        asent += f"\n**ＳＳＲ出現数**\n`{SSR}`"
        asent += f"\n**総ダメージ数**\n`{all_damage}`"
        asent += f"\n**単発平均火力**\n`{(round((all_damage)/(atk_num)))}`"
        asent += f"\n**総獲得経験値**\n`{all_exp}`"
        await message.channel.send(
            f'>>> ```__Auto Battle System Stop__' +
            f'\n戦闘開始時刻：{start_time}' +
            f'\n総合敵討伐数：{m_num}' +
            f'\n停止検知回数：{stop_num}' +
            f'\n死亡復活回数：{revive_num}```'
        )
        ch = client.get_channel(676498979017588737)
        time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
        embed = discord.Embed(
            title = f'**Auto Battle System Stop**',
            description = (
               f"**開始時刻\n{start_time}"+
               f"\n**停止時刻**\n{time}"+
               f"\n**戦闘場所**"+
               f"\n{message.guild.name}({message.guild.id})"+
               f"\n{message.channel.name}({message.channel.id})\n{asent}"),
            color = discord.Color.green()
        )
        await ch.send(embed =embed)

    if message.content.startswith("a)start") and message.author==me:
        test_ch = message.channel
        if test_ch:
            test_flag = True
            start_time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
            ch = client.get_channel(676498979017588737)
            time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
            embed = discord.Embed(
                title = f'**Auto Battle System Start**',
                description = (
                    f'**開始時刻**\n{time}'+
                    f'\n**戦闘場所**\n{message.guild.name}({message.guild.id})'+
                    f'\n{message.channel.name}({message.channel.id})'
                ),
                color = discord.Color.blue()
            )
            await ch.send(embed =embed)

            if test_ch:
                if FB_flag == True:
                    await test_ch.send('::item f')
                else:
                    await test_ch.send(f'::attack ')
            do_time = 0.2

    if message.content == '::item f' and message.author == client.user:
        await message.edit(content = '>>> **スペルカード発動！**')

    if test_flag==False:
        return
    if not message.channel==test_ch:
        return
    #ー以下マクロチャンネル以外反応無くなるーーーーーーーーーーーーーーーーーーーーーーーー#
    if message.author != tao :
        return
    if message.embeds:
        if em_desc:
            if f'{me.mention}はもうやられている' in em_desc:
                await asyncio.sleep(0.2)
                await test_ch.send('::item e')

            if '回復' in em_desc or 'UNBAN' in em_desc:
                await asyncio.sleep(0.2)
                await test_ch.send(f'::attack')

        if em_title:
            if 'が待ち構えている' in em_title:
                monster_name=((em_title).split('】\n')[1]).split('が待ち構えている')[0]
                await asyncio.sleep(do_time)
                m_num+=1

                if kisei_flag == True:
                    await asyncio.sleep(do_time)
                    await test_ch.send('::attack')
                    return
                if "超激レア" in em_title:
                    SSR += 1
                    SSR_flag = True
                    await test_ch.send('>>> **超激レア出現\n一分間のカウントダウンを開始します**\nCOUNTDOWN\n__60__')
                    await asyncio.sleep(10)
                    await test_ch.send('>>> COUNTDOWN\n__50__')
                    await asyncio.sleep(10)
                    await test_ch.send('>>> COUNTDOWN\n__40__')
                    await asyncio.sleep(10)
                    await test_ch.send('>>> COUNTDOWN\n__30__')
                    await asyncio.sleep(10)
                    await test_ch.send('>>> COUNTDOWN\n__20__')
                    await asyncio.sleep(10)
                    await test_ch.send('>>> COUNTDOWN\n__10__')
                    await asyncio.sleep(10)
                    await test_ch.send('>>> COUNTDOWN\n__0__')
                    SSR_flag = False
                    if not "フロスト" in em_title:
                        await test_ch.send(f"::item f")
                        fb_flag = True
                    else:
                        await test_ch.send(f"::attack")
                    return

                if "激レア" in em_title or "シリーズ" in em_title:
                    SR += 1

                if "レア" in em_title or "超強敵" in em_title:
                    R += 1

                if fb_flag == True or FB_flag == True:
                    await test_ch.send(f'::item f')
                else:
                    await test_ch.send(f"::attack")

        if '戦闘結果' in em_title:
            fb_flag = False
            SSR_flag = False
            all_exp+=int(((em_desc).split(f'{me.mention}は')[1]).split('経験値')[0])
            lv_before = int((
                (em_desc)\
                .split('Lv.')[1])\
                .split(' -> ')[0])
            lv_after = int((
                (em_desc)\
                .split('Lv.')[2])\
                .split('`')[0])
            lv += lv_after - lv_before

    if kisei_flag == True:
        return
    #ー以下寄生仲は反応無くなるーーーーーーーーーーーーーーーーーーーーーーーーーー#
    elif f'符の参' in message.content and 'HP' in message.content:
        if not fb_flag == True and not FB_flag == True:
            return
        atk_num += 1
        await asyncio.sleep(do_time)
        await test_ch.send(f"::item f")

    elif f"{me.name}の攻撃" in message.content and f"{me.name}のHP" in message.content:
        if f"{me.name}はやられてしまった" in message.content:
            revive_num+=1
            await asyncio.sleep(do_time)
            await test_ch.send('::item e　復活')
            return
        if not 'かわされてしまった' in message.content:
            atk_num+=1
            if not monster_name == None:
                all_damage+=int((message.content.split(f'{monster_name}に')[1]).split('のダメージ')[0])
        await asyncio.sleep(do_time)
        await test_ch.send(f"::attack")



    if not message.author in [tao,me]:
        log_ch = client.get_channel(676498863628222496)
        embed = discord.Embed(
            title = 'test_ch発言ログ',
            description = (
                f'**発言者**\n{message.author}'+
                f'\n**時刻**\n{datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")}'+
                f'\n**内容**\n{message.content}'
                )
            )
        await log_ch.send(embed = embed)


@client.event
async def on_message_edit(before,after):
    if after.channel==test_ch and after.embeds and after.embeds[0].description:
        if 'BAN' in after.embeds[0].description:
            await asyncio.sleep(0.2)
            await test_ch.send('::i m')
        if 'マクロ' in after.embeds[0].description:
            await asyncio.sleep(0.2)
            await test_ch.send('0')
    if after.embeds and after.embeds[0].description and after.channel == test_ch and "仲間に" in after.embeds[0].description:
        await asyncio.sleep(3)
        if  not 'ミニ' in after.embeds[0].description and "クルーエル" in after.embeds[0].description or "超激レア" in after.embeds[0].description:
            await after.add_reaction("👍")
        else:
            await after.add_reaction("👎")


client.run(TOKEN,bot=False)
