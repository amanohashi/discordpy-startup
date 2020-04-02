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

edit_flag = True

t_num = 0

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
SKD = None

T_flag = True

t_data_dic = {}

R = 0
SR = 0
SSR = 0
SSR_flag = False
kisei_flag = False
do_time = 0

#＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊#

@client.event
async def on_ready():
    pass

#＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊#

@tasks.loop(seconds=31)
async def loop():
    if ready == True:
        global test_flag
        global test_ch
        global SSR_flag
        global check_flag
        global stop_num
        global stop_skd
        global start_skd
        global skd
        tao = client.get_user(526620171658330112)
        now = datetime.now(JST).strftime('%H:%M')
        now_2 = datetime.now(JST).strftime('%m/%d %H:%M')   
        t_ch = client.get_channel(691690169342099556)
        def MSG (msg):
            if msg.author != tao:
                return 0
            return 1

        try:
            await client.wait_for(
                'message',
                timeout=10,
                check = MSG
        )

        except asyncio.TimeoutError:
            if T_flag == False:
                return
            await t_ch.send(f"::t {now}")
           
    
        if stop_skd or start_skd:
            print(f"{now_2} ≠ {stop_skd}")
            print(f"{now_2} ≠ {start_skd}")
    
        if now == '00:00':
            channel = client.get_channel(691699090932891708)
            test_flga = False
            await asyncio.sleep(1)
            await channel.send('::login') 
            await channel.send('t!daily') 
            await asyncio.sleep(1)
            test_flga = True

        if stop_skd and now_2 == stop_skd:
            print(f"{now_2} = {stop_skd}")
            test_flag = False
            await asyncio.sleep(5)
            await test_ch.send("::re")
            await test_ch.send(f">>> **Auto Battle System Stop**\n`Time = {stop_skd}`")
            stop_skd = None
    
        if start_skd and now_2 == start_skd:
            print(f"{now_2} = {start_skd}")
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

#＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊#

@client.event
async def on_message(message):
  
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
    global SKD
    global ready
    global T_flag
    global t_data_dic


    if message.embeds and message.embeds[0].description:
        em_desc = message.embeds[0].description

    if message.embeds and message.embeds[0].title:
        em_title = message.embeds[0].title

    if ready != True:
        ready = True
        loop.start()
        skd_ch = client.get_channel(691699090932891708)
        SKD = (await skd_ch.history( limit = 5 ).flatten())
        if SKD :
            skd = SKD[0]
            SKD = skd
        if skd:
            if not skd.embeds:
                print('embed_None')
                return
            if not skd.embeds[0].description:
                print('desc_None')
                return
            SKD_desc = skd.embeds[0].description
            if SKD_desc.split(' ')[0] == 'True':
                test_flag = True
                testch_id = int(SKD_desc.split(' ')[1])
                test_ch = client.get_channel(testch_id)
                await test_ch.send('::attack 起動')
                if start_skd == None and stop_skd == None:
                    for Field in SKD.embeds[0].fields:
                        if Field.name=="Start_skd":
                            start_skd = Field.value
                        if Field.name=="Stop_skd":
                            stop_skd = Field.value
        log_ch = client.get_channel(691699090932891708)
        print (f'起動ログ\n{datetime.now(JST)}')
        embed = discord.Embed(
            title = "起動ログ",
            description = datetime.now(JST).strftime(f"%Y-%m-%d %H:%M:%S ABS_flag = {test_flag}"))
        embed.timestamp = datetime.now(JST)
        await log_ch.send(embed = embed)
        
        t_datach= client.get_channel(666173722163412995) 
        DATA = await t_datach.history( limit = None ).flatten()
        for data in DATA:
            if not data.embeds:
                continue
            t_data_dic[data.embeds[0].title] = data.embeds[0].description
        return
    
    if not message.guild:
        return
    me = client.user
    amano = discord.utils.get(message.guild.members,id=690901325298401291)
    mio = client.get_user(644153226597498890)
    if not amano:
        return
    tao = client.get_user(526620171658330112)

    skd_ch = client.get_channel(684483032618500108)
 
    sent = "None"

    if message.content.startswith('a)?user='):
        id = int(message.content.split('=')[1])
        user = client.get_user(id)
        m_ch = message.channel
        await m_ch.send(f">>> Checking ID『{id}』")
        if user:
            await message.channel.send(f'>>> **Found The User**\n『{user}』')
        else:
            await m_ch.send(">>> **Couldn't Found The User**")


    t_ch = client.get_channel(691690169342099556) 
    if message.channel == t_ch and message.author == tao:
        msg = message
        if msg.embeds:
            if msg.embeds[0].author.name == f"Training | {client.user}さんの問題":
                await asyncio.sleep(0.5)
                t_q = msg.embeds[0].description
                if t_q in t_data_dic:
                    await t_ch.send(t_data_dic[t_q])
                else:
                    await t_ch.send('しらね')

    if message.author == mio and message.channel == t_ch:
        if message.embeds and message.embeds[0].description:
            if "答え" in message.embeds[0].description:
                A = message.embeds[0].description.split("`")[1]
                await t_ch.send(A)

            
#【　個人用　コマンド　】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.author == me:

        if message.content.startswith('a)off me'):
            await message.channel.send('>>> **Kill Me**')
            await client.logout()
            await sys.exit()

        if message.content.startswith('a)eval '):
            msg = message.content.split('a)eval ')[1]
            exec(msg)
    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith('a)on'):
            if 'fb' in message.content:
                FB_flag = True
                await message.channel.send(f'>>> **Set FB**\n`{FB_flag}`')
            if 'kisei' in message.content:
                kisei_flag = True
                await message.channel.send(f'>>> **Set Kisei**\n`{kisei_flag}`')
            if 'tr' in message.content:
                T_flag = True
                await message.channel.send(f'>>> **Set TR**\n`{T_flag}`')
                await t_ch.send('::t start')


    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith('a)off'):
            if 'fb' in message.content:
                FB_flag = False
                await message.channel.send(f'>>> **Set FB_flag**\n`{FB_flag}`')
            if 'kisei' in message.content:
                kisei_flag = False
                await message.channel.send(f'>>> **Set Kisei**\n`{kisei_flag}`')
            if 'tr' in message.content:
                T_flag = False
                await message.channel.send(f'>>> **Set TR**\n`{T_flag}`')


        if message.content.startswith('a)set_speed '):
            do_time = float(message.content.split(' ')[1])
            text = f'>>> **Set Speed**\n`Speed = {do_time}s`'
            await message.channel.send(text)

    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith('a)set_skd '):
            schedule_time = message.content.split("a)set_skd ")[1]
            if message.content.startswith("a)set_skd ~"):
                start_skd = None
                stop_skd = schedule_time.split('~')[1]
            elif "~" in message.content:
                stop_skd = schedule_time.split('~')[1]
                start_skd = schedule_time.split('~')[0]
                test_ch = message.channel
            else:
                start_skd =  message.content.split(" ")[1]
                stop_skd = None
            text = (f">>> **Set Schedule**\n`Time = {start_skd} ~ {stop_skd}`")
            await message.channel.send(text)

            if not SKD:
                return
            if not SKD.embeds and not SKD.embeds[0].description:
                return
            SKD_desc = SKD.embeds[0].description
            embed = discord.Embed(
                title = SKD.embeds[0].title,
                description = f'{SKD_desc.split(" ")[0]} {message.channel.id}')
            embed.add_field(
                name = 'Start_Skd',
                value = start_skd)
            embed.add_field(
                name = 'Stop_Skd',
                value = stop_skd)
            await SKD.edit(embed=embed)     

    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

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

#【　停　止　中　】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    if message.content.startswith('a)prest') and not message.author.bot:
        await message.channel.send(f'{sent}')

#【　login　コマンド　】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    if message.content == 'a)login' and not message.author.bot:
        await message.channel.send('::login')

#【　ABS　ストップ　】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    if message.content=='a)stop':
        if not message.author==me and not message.author.guild_permissions.administrator:
            await message.author.send('スマンがこのコマンドは俺と鯖缶以外使えねえ…')
            return
        if test_flag==False:
            await message.channel.send(">>> **Macro System hasn't started**")
            return
        test_flag=False
        test_ch=None
        await message.channel.send(
            f'>>> **Auto Battle System Stop**' +
            f'`\n戦闘開始時刻：{start_time}' +
            f'\n総合敵討伐数：{m_num}'
        )
        ch = client.get_channel(691699090932891708)
        time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
        embed = discord.Embed(
            title = f'**Auto Battle System Stop**',
            description = (
               f"**戦闘開始時刻\n{start_time}"+
               f"\n**戦闘停止時刻**\n{time}"+
               f"\n**戦闘指定場所**"+
               f"\n{message.guild.name}({message.guild.id})"+
               f"\n{message.channel.name}({message.channel.id})\n{asent}"),
            color = discord.Color.green()
        )
        await ch.send(embed =embed)
        if SKD:
            embed = discord.Embed(
                title = 'ABS Skd',
                description = f'False {test_ch.id}'
            )
            for F in SKD.embeds[0].fields:
                if F:
                    embed.add_field(
                        name = f'{F.name}',
                        value = f'{F.value}')
            await SKD.edit(embed=embed)




#【ABSスタート】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    if message.content.startswith("a)start") and message.author==me:
        test_ch = message.channel
        if test_ch:
            test_flag = True
            await test_ch.send(f'>>> Set_Ch\nch = `{test_ch.name}`\ntest_flag = `{test_flag}`')
            start_time = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")
            ch = client.get_channel(691699090932891708)
            time = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")
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

            embed = discord.Embed(
                title = 'ABS Skd',
                description = f'True {test_ch.id}'
            )
            if SKD:
                for F in SKD.embeds[0].fields:
                    if F:
                        embed.add_field(
                        name = f'{F.name}',
                        value = f'{F.value}')
                await SKD.edit(embed=embed)
            if test_ch:
                if FB_flag == True:
                    await test_ch.send('::item f')
                else:
                    await test_ch.send(f'::attack ')
            do_time = 0.2

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    if message.content == '::i f' and message.author == client.user:
        await asyncio.sleep(1)
        await message.edit(content = '>>> **スペルカード発動！**')

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    if test_flag==False:
        return
    if message.channel!=test_ch:
        return
    #ー以下マクロチャンネル以外反応無くなるーーーーーーーーーーーーーーーーーーーーーーーー#
    tao = client.get_user(526620171658330112)
    if message.author != tao :
        return
    if message.embeds:
        if em_desc:
            if f'{me.mention}はもうやられている' in em_desc:
                await asyncio.sleep(0.2)
                await test_ch.send('::re ｽﾝｯ( ˙꒳​˙  )')

            if '回復' in em_desc or 'UNBAN' in em_desc:
                await asyncio.sleep(0.2)
                await test_ch.send(f'::attack')

        if message.embeds[0].title:
            em_title = message.embeds[0].title
            if '待ち構' in em_title:
                monster_name=((em_title).split('】\n')[1]).split('が待ち構えている')[0]
                await asyncio.sleep(do_time)
                m_num+=1

                if "フロスト" in em_title:
                    await test_ch.send(f"::item f")
                    fb_flag = True
                    return
                if fb_flag == True or FB_flag == True:
                    await test_ch.send(f'::item f')
                else:
                    await test_ch.send(f"::attack (^ω^≡^ω^)")

        if '戦闘結果' in em_title:
            fb_flag = False
            SSR_flag = False

    if kisei_flag == True:
        return
    #ー以下寄生中は反応無くなるーーーーーーーーーーーーーーーーーーーーーーーーーー#
    if f'ダメージ' in message.content:
        await asyncio.sleep(do_time)
        if not 'HP' in message.content:
            return
        if fb_flag == True or FB_flag == True:      
            await test_ch.send(f"::item f")
        if f'{client.user.name}は' in message.content:
            if f'{me.name}はやられてしまった' in message.content:
                await test_ch.send('::re ( ˘ω˘ ) ｽﾔｧ…')
            elif f'{me.name}の攻撃' in message.content:
                await test_ch.send('::attack ｽﾝｯ( ˙꒳​˙  )')


    elif not message.author in [tao,me]:
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
            await test_ch.send('yes')
        else:
            await test_ch.send('no')
                
    global edit_flag
    global t_num

    if after.channel.id == 691690169342099556 and after.embeds:
        if "正解" in after.embeds[0].description and edit_flag != False and T_flag == True:
            edit_flag = False
            t_num += 1
            await asyncio.sleep(2)
            await after.channel.send(f"::t {t_num}")
            await asyncio.sleep(0.2)
            edit_flag = True
client.run(TOKEN,bot=False)
