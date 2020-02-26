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

check_flag = False

R = 0
SR = 0
SSR = 0
SSR_flag = False
kisei_flag = False
do_time = 0

@client.event
async def on_ready():
    log_ch = client.get_channel(676505024435585055)
    await log_ch.send('```起動ログ\n{datetime.now(JST)}```')
    loop.start()


@tasks.loop(seconds=40)
async def loop():
    global test_flag
    global test_ch
    global SSR_flag
    global check_flag
    global stop_num
    tao = client.get_user(526620171658330112)


    if test_flag==True and SSR_flag == False and check_flag == False:
        check_flag = True
        if tao :
            check_m1 = await test_ch.send('```Checking......```')
            
            if 1 == 1:
                def test_check (tao_msg):
                    if tao_msg.author != tao:
                        return 0
                    if tao_msg.channel!=test_ch:
                        return 0
                    return 1

                try:
                    t_res=await client.wait_for('message', timeout=10, check = test_check)
                    

                except asyncio.TimeoutError:
                    await check_m1.edit(content = '```Checked```')
                    stop_num+=1
                    a = await test_ch.send(f'::attack')
                    await a.edit(content = "```I tried to check for Auto Battle System\nAnd it isn't active!!( 'ω')ｷﾞｬｧｧｧｧｧｧ" + datetime.now(JST).strftime("\n`%Y/%m/%d %H:%M:%S` ```"))
                 
                else:
                    await check_m1.edit(content = '```Checked```')
                    await test_ch.send(("```I tried to check for Auto Battle System\nAnd it is active!!⸜(* ॑꒳ ॑*  )⸝" + datetime.now(JST).strftime("\n`%Y/%m/%d %H:%M:%S` ```")))

                check_flag = False
                

    now = datetime.now(JST).strftime('%H:%M')
    if now == '00:00':
        channel = client.get_channel(676499145208627201)
        await channel.send('::login')  


@client.event
async def on_message(message):
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

    sent = "None"


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
                await message.channel.send(f'**Set FB_flag**\n`{FB_flag}`')
            if 'kisei' in message.content:
                kisei_flag = True
                await message.channel.send(f'**Set Kisei**\n`{kisei_flag}`')

        if message.content.startswith('a)off'):
            if 'fb' in message.content:
                FB_flag = False
                await message.channel.send(f'**Set FB_flag**\n`{FB_flag}`')
            if 'kisei' in message.content:
                kisei_flag = False
                await message.channel.send(f'**Set Kisei**\n`{kisei_flag}`')

        if message.content.startswith('a)setspeed '):
            do_time = float(message.content.split(' ')[1])
            await message.channel.send(f'**Set Speed**\n`{do_time}s`')

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

    """
    if message.content == 'a)i m' and not message.author.bot;
        async with message.channel.typing():
            asyncio.sleep(0.2)
            await message.channel.send('::i m')
    """
    if message.content == 'a)login' and not message.author.bot:
        await message.channel.send('::login')

    if message.content=='a)stop'  :
        if test_flag==True:
            if message.author==me or message.author.guild_permissions.administrator:
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
                await message.channel.send(f'**__Auto Battle System Stop__**\n**戦闘開始時刻**：{start_time}\n**総合敵討伐数**：{m_num}\n**停止検知回数**：{stop_num}\n**死亡復活回数**：{revive_num}')
                ch = client.get_channel(676498979017588737)
                time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
                embed = discord.Embed(
                    title = f'**Auto Battle System Stop**',
                    description = f"**開始時刻**\n{start_time}**停止時刻**\n{time}\n**戦闘場所**n{message.guild.name}({message.guild.id})\n{message.channel.name}({message.channel.id})\n{asent}",
                    color = discord.Color.green()
                )
                await ch.send(embed =embed)
            else:
                await message.author.send('スマンがこのコマンドは俺と鯖缶以外使えねえ…')
        else:
            await message.channel.send("Macro System hasn't started")
        
    if message.content.startswith("a)start ") and message.author==me:
        #async with message.channel.typing():
        test_ch = message.channel
        if test_ch:
            test_flag = True
            start_time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
            ch = client.get_channel(676498979017588737)
            time = datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
            await ch.send(embed = discord.Embed(
                title = f'**Auto Battle System Start**', 
                description = f'**開始時刻**\n{time}\n**戦闘場所**\n{message.guild.name}({message.guild.id})\n{message.channel.name}({message.channel.id})',
                color = discord.Color.blue()
            )
            )                           
                                                                         
            if test_ch:
                if FB_flag == True:
                    await test_ch.send('::item f')
                else:
                    await test_ch.send(f'::attack ')
            do_time = float(message.content.split(' ')[1])

    if message.channel==test_ch and test_flag==True and message.author == tao :
        #async with message.channel.typing():
        if kisei_flag == False:
            if f"{me.name}の攻撃" in message.content:
                if not 'かわされてしまった' in message.content:
                    atk_num+=1
                    if not monster_name == None:
                        all_damage+=int((message.content.split(f'{monster_name}に')[1]).split('のダメージ')[0])

            if f"{me.name}はやられてしまった" in message.content:
                revive_num+=1
                await asyncio.sleep(do_time)
                await test_ch.send('::item e　復活')

            elif (f'符の参：恋符『マスタースパーク』' in message.content and 'HP' in message.content) and (fb_flag == True or FB_flag == True):
                await asyncio.sleep(do_time)
                await test_ch.send(f"::item f")
                atk_num += 1

            elif (f"{me.name}の攻撃" in message.content and f"{me.name}のHP" in message.content and not f"{me.name}はやられてしまった" in message.content):    
                await asyncio.sleep(do_time)
                await test_ch.send(f"::attack")
    

    if message.channel==test_ch and test_flag==True and message.author == me:
        if kisei_flag == False:
            if message.content.startswith('::item f') and FB_flag == True:
                def remsg_check(msg):
                    if msg.author!=tao:
                        return 0
                    elif msg.channel!=test_ch:
                        return 0
                    elif not '符の参：恋符『マスタースパーク』！' in msg.content:
                        return 0
                    return 1
                try:
                    res_msg=await client.wait_for('message',timeout=10,check=remsg_check)
                except asyncio.TimeoutError:
                    stop_num+=1
                    await test_ch.send(f'::item f')
                else:
                    pass
 
            elif message.content.startswith('::attack'):
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
                    await test_ch.send(f'::attack \n**停止検知回数：**`{stop_num}`')
                else:
                    pass
 
   

    if message.channel == test_ch and message.embeds and test_flag==True :
        #async with message.channel.typing():
        if 1 == 1:
            if message.embeds[0].description and f'{me.mention}はもうやられている' in message.embeds[0].description and kisei_flag == False:
                await asyncio.sleep(0.2)
                await test_ch.send('::item e')
  
            elif message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:

                monster_name=((message.embeds[0].title).split('】\n')[1]).split('が待ち構えている')[0]
                await asyncio.sleep(do_time)
                m_num+=1

                if kisei_flag == True:
                    await asyncio.sleep(do_time)
                    await test_ch.send('::attack')
                    return
                if "超激レア" in message.embeds[0].title:
                    SSR += 1

                elif "激レア" in message.embeds[0].title or "シリーズ" in message.embeds[0].title:
                    SR += 1

                elif "レア" in message.embeds[0].title or "超強敵" in message.embeds[0].title: 
                    R += 1

                if "超激レア" in message.embeds[0].title:
                    SSR_flag = True
                    await test_ch.send('**超激レア出現\n一分間のカウントダウンを開始します**\nCOUNTDOWN\n__60__')
                    await asyncio.sleep(10)
                    await test_ch.send('COUNTDOWN\n__50__')
                    await asyncio.sleep(10)
                    await test_ch.send('COUNTDOWN\n__40__')
                    await asyncio.sleep(10)
                    await test_ch.send('COUNTDOWN\n__30__')
                    await asyncio.sleep(10)
                    await test_ch.send('COUNTDOWN\n__20__')
                    await asyncio.sleep(10)
                    await test_ch.send('COUNTDOWN\n__10__')
                    await asyncio.sleep(10)
                    await test_ch.send('COUNTDOWN\n__0__')
                    SSR_flag = False
                    if not "フロスト" in message.embeds[0].title:
                        await test_ch.send(f"::item f")
                        fb_flag = True
                    else:
                        await test_ch.send(f"::attack")

                else:
                    if fb_flag == True or FB_flag == True:
                        await test_ch.send(f'::item f')
                    else:
                        await test_ch.send(f"::attack")
                

            if kisei_flag == False and message.embeds[0].description and ('回復' in message.embeds[0].description or 'UNBAN' in message.embeds[0].description):
                await asyncio.sleep(0.2)
                await test_ch.send(f'::attack')
    

            if message.embeds[0].title and '戦闘結果' in message.embeds[0].title:
                fb_flag = False
                SSR_flag = False
                all_exp+=int(((message.embeds[0].description).split(f'{me.mention}は')[1]).split('経験値')[0])
                lv_before = int(((message.embeds[0].description).split('Lv.')[1]).split(' -> ')[0])
                lv_after = int(((message.embeds[0].description).split('Lv.')[2]).split('`')[0])
                lv += lv_after - lv_before


    if message.channel==test_ch and test_flag==True:
        if not message.author in [tao,me]:
            log_ch = client.get_channel(676498863628222496)
            await log_ch.send(embed = discord.Embed(title = 'test_ch発言ログ', description = f'**発言者**\n{message.author}\n**時刻**\n{datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")}\n**内容**\n{message.content}'))
      

    if message.content.startswith('a)?user='):
        id = int(message.content.split('=')[1])
        user = client.get_user(id)
        m_ch = message.channel
        await m_ch.send(f"Checking ID『{id}』")
        if user:
            await message.channel.send(f'**Found The User**\n『{user}』')
        else:
            await m_ch.send("**Couldn't Found The User**")

            
    if message.content == 'a)check' :
        await message.channel.send(f'check_flag = {check_flag}')        


    if message.content == '::item f' and message.author == client.user:
        await message.edit(content = '**スペルカード発動！**')
    
    """
    if message.content == a)history and message.author == me :
        msgs = await message.channel.history( limit = 5 ).flatten()
        for msg in msgs:
            if msg.author == tao and msg.embeds and msg.embeds[0].title:
                if '待ち構えている' in msg.embeds[0].title:
                    ALL_m = msg
    """


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
