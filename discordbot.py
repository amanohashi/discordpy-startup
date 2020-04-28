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

user_dic = {}

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
stop_skd = None
start_skd = None
check_flag = False
SKD = None
die_word = '::item e ♻️'
bukikon = 0
best_dmg = 0

T_flag = False

t_data_dic = {}

yadonushi_flag = False
kiseisya = None

R = 0
SR = 0
SSR = 0
SSR_flag = False
kisei_flag = False
do_time = 0.2

#＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊#

@client.event
async def on_ready():
    ch = client.get_channel(676505024435585055)
    await ch.send('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

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
            channel = client.get_channel(676499145208627201)
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
                def test_check(tao_msg):
                    if tao_msg.author != tao:
                        return 0
                    if tao_msg.channel!=test_ch:
                        return 0
                    return 1

                try:
                    t_res=await client.wait_for(
                        'message',
                        timeout=60,
                        check = test_check
                )

                except asyncio.TimeoutError:
                    if fb_flag == True or FB_flag == True:
                        await test_ch.send("::item f")
                    else:
                        await test_ch.send(f"::attack `{stop_num}`")
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
    global stop_skd
    global start_skd
    global SKD
    global ready
    global T_flag
    global t_data_dic
    global die_word
    global bukikon
    global best_dmg
    global user_dic
    global yadonushi_flag
    global kiseisya

    em_desc = None
    em_title = None
    msg_ctt = None
    m_ch = None
    m_ctt = None

    if message.embeds and message.embeds[0].description:
        em_desc = message.embeds[0].description
    if message.embeds and message.embeds[0].title:
        em_title = message.embeds[0].title
    if message.content:
        msg_ctt = message.content
        m_ctt = msg_ctt
    if message.channel:
        m_ch = message.channel
        
    if message.content.startswith("reward "):
        if message.author.id != 701735198513168454:
            return
        if message.channel.id != 701721786592657461:
            return
        ch_id = 701721786592657461
        ch = client.get_channel(ch_id)
        pattern = r"reward \[(\d{1,})] \[(\d{1,})]"
        result = re.search(pattern,message.content)
        await ch.send(f"t!credit {result.group(1)} {result.group(2)}")
        def check(msg):
            if msg.author.id != 172002275412279296:
                return 0
            if not msg.content.startswith("Transferring"):
                return 0
            if msg.channel != ch:
                return 0
            return 1
        try:
            t_msg=await client.wait_for('message',timeout=5,check = check)
        except asyncio.TimeoutError:
            await ch.send('…ん？竜巻返事ない。謎ｗ')
        else:
            code = t_msg.content.split("To confirm, type `")[1].split("` or type")[0]
            await asyncio.sleep(1)
            await ch.send(code)          

    #――――――――――――――――――――――――-------------------------#

    if ready != True:
        ready = True
        loop.start()
        skd_ch = client.get_channel(684483032618500108)
        SKD = (await skd_ch.history( limit = 1 ).flatten())
        if SKD :
            skd = SKD[0]
            SKD = skd
            if not skd.embeds:
                return
            if not skd.embeds[0].description:
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
        log_ch = client.get_channel(676505024435585055)
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

            
#【　個人用　コマンド　】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.author == me:

        if message.content.startswith('a)eval '):
            msg = message.content.split('a)eval ')[1]
            exec(msg)

        if message.content.startswith('a)on '):
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
            if 'yn' in message.content:
                yadonushi_flag = True
                await message.channel.send(f'>>> **Set YN**\n`{yadonushi_flag}`')             

    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith('a)off '):
            if 'fb' in message.content:
                FB_flag = False
                await message.channel.send(f'>>> **Set FB_flag**\n`{FB_flag}`')
            if 'kisei' in message.content:
                kisei_flag = False
                await message.channel.send(f'>>> **Set Kisei**\n`{kisei_flag}`')
            if 'tr' in message.content:
                T_flag = False
                await message.channel.send(f'>>> **Set TR**\n`{T_flag}`')
            if 'me' in message.content:
                await message.channel.send('>>> **Kill Me**')
                await client.logout()
                await sys.exit()
            if 'yn' in message.content:
                yadonushi_flag = False
                await message.channel.send(f'>>> **Set YN**\n`{yadonushi_flag}`')             


        if message.content.startswith('a)set_speed '):
            do_time = float(message.content.split(' ')[1])
            text = f'>>> **Set Speed**\n`Speed = {do_time}s`'
            await message.channel.send(text)

        if message.content.startswith('a)set_die '):
            die_word = message.content.split('die ')[1]
            text = f'>>> **Set DieWord**\n`Word = {die_word}`'
            await message.channel.send(text)
            
        if message.content.startswith('a)set_yn '):
            id = message.content.split('yn ')[1]
            kiseisya = client.get_user(int(id))
            text = f'>>> **Set Kiseisya**\n`User = {kiseisya}`'
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

#【　prest　】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#
    if m_num == 0 :
        sent = '>>> ⚙️❌**統計値がNoneです**'
    else:
        sent = (f">>> **統計📝**\n" +
            f"⚙️🚫Stop_Num = {stop_num}\n" +
            f"⚙️🎭Mob_Num = {m_num}\n" +
            f"⚙️🌛SSR_Mob = {SSR}/{m_num}({(SSR/m_num)*100}%)\n" +
            f"⚙️🆙Lv_Up = {lv}\n" +
            f"⚙️🎫Exp_Get = {all_exp}\n" +
            f"⚙️⚔️Best_Damage = {best_dmg}\n" +
            f"⚙️🔥Bukikon = {bukikon}")


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
        ch = client.get_channel(676498979017588737)
        time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
        if test_flag == True:
            if 1 == 1:
                test_flag = False
                
                B = await m_ch.send(f'>>> ⚙️🚫**System_Flag** = True')
                await asyncio.sleep(1)
                await B.edit(content = f'>>> ⚙️♻️**System_Flag** = False')
                A = await m_ch.send(f'>>> ⚙️🚫**Set_Channel** = {test_ch.name}')
                test_ch = None
                await asyncio.sleep(1)
                await A.edit(content = '>>> ⚙️♻️**Set_Channel** = ━━━━━━━━━━')
                C = await m_ch.send('>>> ⚙️🔄Loading[　　　　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬　　　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬　　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬▬　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬▬▬　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬▬▬▬]')
                await C.edit(content = '>>> ⚙️♻️**Loaded** [▬▬▬▬▬▬▬▬▬▬]')
                await m_ch.send('>>> ⚙️♻️**System AllGreen**')
                await asyncio.sleep(0.1)
                await m_ch.send('>>> ⚙️📴**System Stop**')
        
        if SKD:
            embed = discord.Embed(
                title = 'ABS Skd',
                description = f'False {test_ch.id}'
            )
            """
            for F in SKD.embeds[0].fields:
                if F:
                    embed.add_field(
                        name = f'{F.name}',
                        value = f'{F.value}')
            """
            await SKD.edit(embed=embed)




#【ABSスタート】＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝#

    if message.content.startswith("a)start") and message.author==me:
        test_ch = message.channel
        
        A = await test_ch.send(f'>>> ⚙️🚫**Set_Channel** = ━━━━━━━━━━')
        if test_ch:
            test_flag = True
            start_time = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S")
            ch = client.get_channel(676498979017588737)
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
            if not SKD:
                CH = client.get_channel(684483032618500108)
                SKD = await CH.send(embed=embed)
            if test_ch:
                await A.edit(content = f'>>> ⚙️♻️**Set_Channel** = {test_ch.name}')
                B = await test_ch.send(f'>>> ⚙️🚫**System_Flag** = False')
                await asyncio.sleep(1)
                await B.edit(content = f'>>> ⚙️♻️**System_Flag** = {test_flag}')
                C = await test_ch.send('>>> ⚙️🔄Loading[　　　　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬　　　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬　　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬　　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬　　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬　　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬　　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬　　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬▬　　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬▬▬　]')
                await C.edit(content = '>>> ⚙️🔄Loading[▬▬▬▬▬▬▬▬▬▬]')
                await C.edit(content = '>>> ⚙️♻️**Loaded** [▬▬▬▬▬▬▬▬▬▬]')
                await asyncio.sleep(0.2)
                await test_ch.send('>>> ⚙️♻️**System AllGreen**')
                await asyncio.sleep(0.1)
                await test_ch.send('>>> ⚙️📳**System Start**')

                if FB_flag == True:
                    await test_ch.send('::item f')
                else:
                    await test_ch.send(f'::attack ')
            do_time = 0.2

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

    if test_flag==False:
        return
    if message.channel!=test_ch:
        return
    #ー以下マクロチャンネル以外反応無くなるーーーーーーーーーーーーーーーーーーーーーーーー#
    tao = client.get_user(526620171658330112)
    if message.author != tao :
        return
    if message.embeds :
        if message.embeds[0].description:
            em_desc = message.embeds[0].description
        if message.embeds[0].title:
            em_title = message.embeds[0].title
            mob_p = r"属性:\[(.+)] \| ランク:【(.+)】(.+)が待ち構えている...！Lv\.(\d+)  HP:(\d+)"
            mob_r = re.search(mob_p,em_title.replace("\n",""))
            if mob_r:
                monster_name=mob_r.group(3)
                await asyncio.sleep(do_time)
                m_num+=1
                if "超激レア" in mob_r.group(2):
                    SSR += 1
                if "フロスト" in mob_r.group(3):
                    await test_ch.send(f"::item f ktkr")
                    fb_flag = True
                    return
                if yadonushi_flag != False:
                    return
                if fb_flag == True or FB_flag == True:
                    await test_ch.send(f'::item f')
                else:
                    await test_ch.send(f"::attack")

            if '戦闘結果' in em_title:
                #XP総量計算
                exp_p = r"(.+)は(\d+)経験値を獲得"
                exp_r = re.search(exp_p,em_desc)
                if exp_r and f"{client.user.mention}" == exp_r.group(1):
                    all_exp += int(exp_r.group(2))

                #Lv総量計算
                split3 = f"{client.user.mention}はレベルアップした！"
                if split3 in em_desc:
                    lv_p = r"(.+)はレベルアップした！`Lv.(\d+) -> Lv.(\d+)`"
                    lv_r = re.search(lv_p,em_desc)
                    lv += int(lv_r.group(3)) - int(lv_r.group(2))

                fb_flag = False
                SSR_flag = False

        if em_desc:
            if f'{me.mention}はもうやられている' in em_desc:
                await asyncio.sleep(0.2)
                await test_ch.send(die_word)

            if '回復' in em_desc or 'UNBAN' in em_desc:
                await asyncio.sleep(0.2)
                await test_ch.send(f'::attack')

            if '武器は耐久力が' in em_desc:
                bukikon -= 5
                print(f"{datetime.now(JST)}┃武器耐久0")
                test_flag = False
                await test_ch.send('::weapon')
                await asyncio.sleep(3)
                await test_ch.send('6')
                await asyncio.sleep(3)
                await test_ch.send('c')
                await asyncio.sleep(3)
                await test_ch.send('ok')
                await asyncio.sleep(3)
                test_flag = True
                await test_ch.send('::attack \n消費武器魂│`{bukikon}`個')

            if '仲間に' in em_desc:
                await asyncio.sleep(1)
                if  "クルーエル" in em_desc:
                    if 'ミニ' in em_desc or '無慈悲な' in em_desc:
                        await test_ch.send('no')
                        return
                    await test_ch.send('ok')
                else:
                    await test_ch.send('no')

            if 'ログイン' in em_desc:
                await test_ch.send('::login')
    


    if kisei_flag == True:
        return
    #ー以下寄生中は反応無くなるーーーーーーーーーーーーーーーーーーーーーーーーーー#
         
                
    if me.name in message.content or (yadonushi_flag == True and kiseisya and kiseisya.name in message.content):
        m_ctt = (message.content.split("```")[1])
        print(m_ctt)
        pattern = r"(.+)のHP:(\d+)/(\d+)"
        a_pattern_1 = r"(.+)の攻撃！(.+)に(\d+)のダメージを与えた！"
        a_pattern_2 = r"(.+)の攻撃！(.+)にかわされてしまった...！！"
        a_pattern_3 = r"(.+)の攻撃！会心の一撃！(.+)に(\d+)のダメージを与えた！"
        f_pattern = r"(.+)！(.+)は(.+)に(\d+)のダメージを与えた！"

        result_0 = re.search(pattern,m_ctt)
        result_1 = re.search(a_pattern_1,m_ctt)
        result_2 = re.search(a_pattern_2,m_ctt)
        result_3 = re.search(a_pattern_3,m_ctt)
        result_4 = re.search(f_pattern,m_ctt)
        dmg = 0
        if result_1:
            dmg = int(result_1.group(3))
        if result_2:
            dmg = 0        
        if result_3:
            dmg = int(result_1.group(3))
        if dmg > best_dmg:
            best_dmg = dmg
        await asyncio.sleep(do_time)
        if not result_0:
            return
        if result_0 and f"{me.name}はやられてしまった" in m_ctt:
            await test_ch.send(die_word)
            return
        if result_4 and (fb_flag == True or FB_flag == True):      
            await test_ch.send(f"::item f")
            return
        await test_ch.send(f"::attack")
                

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
