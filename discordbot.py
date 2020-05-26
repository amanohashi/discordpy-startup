# discordpy-startup
# -*- coding: utf-8 -*-
import sys
import discord
import random
import asyncio
import time
import datetime
import urllib.request
import json
import re
import requests
import os
import traceback
import math

from discord.ext import tasks
from datetime import datetime, timedelta, timezone


import logging

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')


client = discord.Client()
TOKEN = os.environ['DISCORD_BOT_TOKEN']
#TOKEN="NjI3MDUyNTc2ODEwMDc0MTEy////.XgTAtg.k6EBPNmQ9XfUJ3nXcBI6-tIlzx8"
dateTime = datetime.now(JST)
server_number = len(client.guilds)


talk_flag = True
last_resp = None
data_list = []


import citycode_data
citycodes = citycode_data.cc()


training_data = {}

client.already_quiz = {}

lust_lvup = None

CHANNEL_ID = 623154510662991883
client = discord.Client()
ModeFlag = 0
#━━━━━━━━━━━━━━━┓
atk_ch = 2
atk_ch2=2
#━━━━━━━━━━━━━━━┫
d_ch = 2
d_ch2= 2
d_num = 1
d_num2= 1
d_flag=False
d_flag2=False
#━━━━━━━━━━━━━━━┫
test_ch = None
test_user = None
test_guild = None
start_time = None
test_flag=False
exp=0
#━━━━━━━━━━━━━━━┫
ban_guild=1
already_quiz={}
q_ch=0
t_ch=0
t_flag=False
yui_ans_msg = None
edit_flag = True
edit_flag2 = True
global_list = []
t_data_dic = {}
t_q = None
t_qmsg = None
#━━━━━━━━━━━━━━━┫
lvup_time=None
lvup_timediff=None
total_timediff=0
lvup_renum=0
lvup_timeavg=0

deleuser=None
delech=None

developer=0


#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="起動中( ˘ω˘ ) ｽﾔｧ…"))
    global t_data_dic
    t_datach= client.get_channel(699128134167167006)


    global developer
    developer=client.get_user(690901325298401291)
    
    global t_ch
    t_ch=client.get_channel(699129290217750588)
    await t_ch.send('::t')

    for guild in client.guilds:
        tmp = discord.utils.get(guild.text_channels, name="global_yui")

    global t_flag
    t_flag=True

    loop.start()
    
    start_msg = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
    start_msg+=f'\n‣BOT NAME   『{client.user.name}』'
    start_msg+=f'\n‣BOT ID     『{client.user.id}』'
    start_msg+=f'\n‣LOGIN TIME 『{datetime.now(JST)}』'
    start_msg+= '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
    print(start_msg)

    dateTime = datetime.now(JST)
    embed = discord.Embed(title="YUI起動ログ", description="起動したよ", color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(
        ('https://yahoo.jp/box/3faN7k', 'https://yahoo.jp/box/c9L236', 'https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="起動時刻", value=f"{dateTime.year}年{dateTime.month}月{dateTime.day}日　{dateTime.hour}時{dateTime.minute}分{dateTime.second}秒", inline=False)
    embed.add_field(name="YUI news", value="YUIの開発は開発者が一身上の不幸によりdiscordを引退するため終了しました。\n不具合等ございましたら対応するかはわかりませんが```y!report [内容]```で御申し付け下さい", inline=True)
    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui起動ログ'))
    
    user = client.get_user(446610711230152706)
    await user.send(embed=embed)
    
    ready_log_ch = client.get_channel(699128721273126973)
    await ready_log_ch.send(embed=embed)

    await client.change_presence(activity=discord.Game(name="y!help│" + str(len(set(client.guilds))) + 'の鯖に所属中'))

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

@tasks.loop(seconds=60)
async def loop():
    await client.change_presence(activity=discord.Game(name=(
        "y!help│" + 
        str(len(set(client.guilds))) + 'servers│'+
        str(len(set(client.users))) + 'users│' +
        str(datetime.now(JST))
        )))

#━トレーニングチェック━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
    if t_flag==True:

        tao=client.get_user(688300266331701273)
        if tao:
            def test_check (t_msg):
                if t_msg.author != tao:
                    return 0
                if t_msg.channel!=t_ch:
                    return 0
                return 1

            try:
                t_res=await client.wait_for('message',timeout=10,check = test_check)
            except asyncio.TimeoutError:
                await t_ch.send('::t loop')
            else:
                return

#━自動戦闘チェック━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
    if test_flag==True:
        if tao:
            def test_check (d_msg):
                if d_msg.author != tao:
                    return 0
                if d_msg.channel!=test_ch:
                    return 0
                return 1

            try:
                t_res=await client.wait_for('message',timeout=60,check = test_check)
            except asyncio.TimeoutError:
                print('::attack')
                await test_ch.send('::attack とまってない?')
            else:
                return

#━00:00チェック━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
    now = datetime.now(JST).strftime('%H:%M')
    if now == '00:00':
        em = discord.Embed(title="24:00の時報をお伝えします\nなんちゃって", description=random.choice((
            '日付変わったから寝ようね！？',
            'まだ起きてるとかみんな狂乱なの？',
            '夜更かしは体に悪いよ……え、私？\nBOTだから支障ZEROですｗｗ',
            'ねろ（辛辣\nさっさと寝ろ',
            '別にいいけどさ……\n夜更かしは体壊さない程度にね',
            'えーと、これ読めばいいの？ \n(台本ﾊﾟﾗﾊﾟﾗ)\nねえこの「お兄ちゃんもう寝ないと！」ってなに？\n殺されたいの？')),
                           inline=False)
        em.set_thumbnail(url="https://yahoo.jp/box/roWwt8")
        for c in client.get_all_channels():
            if c.name == 'yui時報ログ':
                client.loop.create_task(c.send(embed=em))
        print("チャンネル判定終了")
        login_ch = client.get_channel(659964329264676886)
        await login_ch.send('::login')

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

@client.event
async def on_disconnect():
    print("YUI was death")
    embed = discord.Embed(title="YUIが切断されあぁ！", description="原因は知らんけど切断されちゃった(灬ºωº灬)てへっ♡", color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(
        ('https://yahoo.jp/box/3faN7k', 'https://yahoo.jp/box/c9L236', 'https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="切断時刻",value=datetime.now(JST), inline=True)
    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui起動ログ'))

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢


@client.event
async def on_guild_join(guild):
    log_ch=client.get_channel(659925765974130700)
    inviteurl_list = await guild.invites()
    embed = discord.Embed(
        title = "( 'ω'o[サーバー参加]oログ♡",
        description = f"参加鯖名\n『{guild.name}』\n参加鯖ID\n『{guild.id}』\n[鯖URL]({inviteurl_list[0]})")
    embed.set_thumbnail(url = guild.icon_url)
    embed.timestamp = datetime.now(JST)
    await log_ch.send(embed=embed)

    
@client.event
async def on_guild_remove(guild):
    log_ch=client.get_channel(659925811628867637)
    embed = discord.Embed(
        title = "( 'ω'o[サーバー退出]oログ♡",
        description = f"退出鯖名\n『{guild.name}』\n退出鯖ID\n『{guild.id}』\n[鯖URL]({inviteurl_list[0]})")
    embed.set_thumbnail(url = guild.icon_url)
    embed.timestamp = datetime.now(JST)
    await log_ch.send(embed=embed)
#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤
#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢


@client.event
async def on_message(message):
    yui_url = "https://discordapp.com/api/oauth2/authorize?client_id=697262684227371059&permissions=8&scope=bot"
    if message.content.startswith("y!ban "):
        await message.delete
   
        id = int(message.content.split("y!ban ")[1])
        print(id)
        uSer = client.get_user(id)
        if not user:
            print("no")
            return
        await message.guild.ban(user,resone = "u r not Tsukumo's True friend") 
    
    if not message.guild:
        return
    
    amano = client.get_user(690901325298401291)
    if message.content.startswith("y!setst "):
        if message.author != amano:
            await message.channel.send("開発者専用コマンドです")
            return
        st_text = message.content.split("y!setst ")[1]
        await client.change_presence(activity=discord.Game(name=st_text))
        
    if message.author == amano:
        if message.content.startswith("y!setnick "):
            m_ctt = message.content
            id = int(m_ctt.split('"')[1])
            nick = m_ctt.split('"')[3]
            print(f"ID = {id} /nNick = {nick}")
            member = message.guild.get_member(id)
            if not member:
                await message.channel.send(f"{id}というIDのメンバーはいません")
                return
            await member.edit(nick = f"{nick}")
        
    if message.content == "y!rest":
        if message.author != amano:
            await message.channel.send("開発者専用コマンドです")
            return
        await client.change_presence(activity=discord.Game(name="y!help│" + str(len(client.guilds)) + 'の鯖に所属中'))
        
    global deleuser
    global delech

    if deleuser and delech and message.channel==delech and message.author==deleuser:
        await message.delete()
        embed = discord.Embed(
            title = f"{deleuser}の発言",
            description = f"||{message.content}||")
        await message.channel.send(embed = embed)


    if message.content.startswith('y!dele'):
        deleuser_id=int(message.content.split(' ')[1])
        deleuser=client.get_user(deleuser_id)
        delech_id=int(message.content.split(' ')[2])
        delech=client.get_channel(delech_id)
        await message.channel.send(embed = discord.Embed(title = f"{deleuser}を{delech.name}で全力ミュートします"))

    if message.content=='y!deleNone':
        delech=None
        deleuser=None

#━━━━❮ダンジョン+αで使うグローバル変数と変数❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    global atk_ch
    global atk_ch2
    global d_ch
    global d_num
    global d_ch2
    global d_flag
    global d_flag2
    mio = client.get_user(644153226597498890)
    tao = client.get_user(526620171658330112)


#━━━━❮Trainingコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    me = client.user
    tao = client.get_user(526620171658330112)
    TAO = client.get_user(688300266331701273)
    t_ch = client.get_channel(659923091027132416)
    global t_data_dic
    global t_flag
    global yui_ans_msg
    global t_q
    

    if message.content == "y!t":
        await message.channel.send("::t")

    if message.channel == t_ch and message.author == mio or message.author == TAO:
        msg = message
        if msg.embeds:
            if msg.embeds[0].author.name == f"Training | {client.user}さんの問題":
                await asyncio.sleep(0.5)
                t_q = msg.embeds[0].description
                if t_q in t_data_dic:
                    await t_ch.send(t_data_dic[t_q])
                    return
                
                def mio_check(mio_msg):
                    if mio_msg.author!=mio:
                        return 0
                    if not mio_msg.embeds:
                        return 0
                    if mio_msg.channel!=t_ch:
                        return 0
                    return 1

                try:
                    mio_resp=await client.wait_for('message',timeout=2,check=mio_check)
                except asyncio.TimeoutError:
                    return
                else:
                    await mio_resp.delete()
                    t_ans=(mio_resp.embeds[0].description).split('`')[1]
                    await asyncio.sleep(0.5)
                    A = await t_ch.send(t_ans)
                    await A.delete()
                    t_datach= client.get_channel(666173722163412995)
                    t_data_dic.setdefault(t_q,t_ans)
                    
                    embed = discord.Embed(
                        title = t_q,
                        description = t_ans)
                    await t_datach.send(embed = embed)
                    t_q = None
                    t_ans = None
                

    if message.content=='y!tstart':
        t_flag=True
        embed = discord.Embed(
        title=f"トレーニング開始\nt_flag = {t_flag}"
        )
        await message.author.send(embed = embed)
        await t_ch.send('::t start')

    if message.content=='y!tstop' :
        t_flag=False                   
        embed = discord.Embed(
        title=f"トレーニング終了\nt_flag = {t_flag}"
        )
        await message.author.send(embed = embed)

#━━━━❮YUIpingコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content=='y!ping':
        await message.channel.send(embed=discord.Embed(title=f'**Pong!\n{(client.latency)*1000}ms**'))

#━━━━❮YUIhelpコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    help_ch = 659922476641288211
    if message.content == "y!help":
        log_ch = client.get_channel(659922476641288211)
        help_logch = client.get_channel(id=help_ch)        
        author_id=str(message.author.id)

        #Helpの0ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em0desc = ('➤[]は不要です\n`y![example]→y!example`' +
                   '\n➤スペースの有無を確認して下さい' +
                   '\n`y!example []→有り\ny!example[]→無し`' +
                   '\n➤管理者権限必須です' +
                   '\n`YUIに管理者権限が無い場合基本このページから進みません。`' +
                   '\n➤管理者権限があるのにHelpが見れない不具合' +
                   f'\n`Helpがこのページから進まない場合は`[こちら]({yui_url})`からYUIを招待し直してください。\n不具合はy!report [内容]`')
        em0 = discord.Embed(
            title="⚠️YUI注意事項一覧⚠️",
            description=em0desc ,
            color=discord.Colour.green())

        #━Helpの1ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em1desc='```ヘルプ目次　　│P.1\n'
        em1desc += 'ＴＡＯコマンド│P.2\n'
        em1desc += 'メイン機能　　│P.3\n'
        em1desc += '特殊チャンネル│P.4\n'
        em1desc += 'ガチャ　　　　│P.5\n'
        em1desc += 'その他娯楽　　│P.6\n'
        em1desc += 'ユイ関連ＵＲＬ│P.7```'
        em1 = discord.Embed(title="YUIヘルプ目次",
            description=em1desc,
            color=discord.Colour.green())
        em1.set_thumbnail(url=random.choice(
            ('https://yahoo.jp/box/3faN7k', 'https://yahoo.jp/box/c9L236', 'https://yahoo.jp/box/Jxj1Jd')))
        em1.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.1/7")

        #━Helpの2ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em2desc='y!atkch [channel mention]│`指定チャンネルで自動戦闘`'
        em2desc += '\ny!atkstop│`自動戦闘の終了`'
        em2desc += '\ny![atk,i f,i e,i,st,rmap,re]`│各種TAOコマンド`'
        em2desc += '\ny!role [役職番号]│`役職変更(0冒険職,1戦士,魔法職,3盗賊)`'
        em2desc += '\ny!nekoshima│`超激出現占`'
        em2 = discord.Embed(
            title="TAOコマンド系ヘルプ", 
            description=em2desc, 
            color=discord.Colour.green())
        em2.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.2/7")

        #━Helpの3ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em3desc='y!help│`helpコマンド`'
        em3desc += '\ny!sinfo│`サーバーの情報`'
        em3desc += '\ny!mkch [名前]│`チャンネル作成`'
        em3desc += '\ny!myicon│`使用者のアイコン表示`'
        em3desc += '\ny!clean [消去数]│`ログ消去(管理者権限必須)`'
        em3desc += '\ny!say1 [内容]│`発現代理(メンションは管理者権限必須)`'
        em3desc += '\ny!say2 "見出し" "内容"│`embed送信(　〃　)`'
        em3desc += '\ny!ping│`botの反応速度測定`'
        em3desc += '\ny!gban [id]│`指定USERをグローバルBAN`'
        em3desc += '\ny!report [内容]│`開発者にレポートを送信`'
        em3 = discord.Embed(
            title="メイン機能ヘルプ",
            description=em3desc,
            color=discord.Colour.green())
        em3.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.3/7")

        #━Helpの4ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em4 = discord.Embed(
            title='特殊チャンネル系',
            description='```チャンネル内容│チャンネル名\nチャンネル作成コマンド```', color=discord.Colour.green())
        em4.add_field(name='グローバルチャット│global_yui'
                                , value='```y!yui global```', inline=False)
        em4.add_field(name='YUIの起動ログ│yui起動ログ'
                                , value='```y!yui log```', inline=False)
        em4.add_field(name='日付変更ログ│yui時報ログ'
                                , value='```y!yui timelog```')
        em4.add_field(name='YUIレベルアップログ│yuiレベルアップログ'
                                , value='```y!lv```',inline=False)
        em4.add_field(name='TAOモンスター出現ログ│tao出現ログ:'
                                , value='```y!tao 1│通常モンスター用のチャンネル\ny!tao 1.5│強敵モンスター用のチャンネル\ny!tao 5│経験値倍率５倍モンスター用のチャンネル\ny!tao 33│経験値倍率33倍モンスター用のチャンネル\ny!tao 100│経験値倍率100倍モンスター用のチャンネル\n```', inline=False)
        em4.add_field(name='YUIの起動ログ│yui起動ログ'
                                , value='```y!yui log```', inline=False)
        em4.add_field(name='日付変更ログ│yui時報ログ'
                                , value='```y!yui timelog```')
        em4.add_field(name='YUIレベルアップログ│yuiレベルアップログ'
                                , value='```y!lv```',inline=False)
        em4.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.4/7")

        #━Helpの5ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em5 = discord.Embed(
            title="ガチャ機能だよ🎯 ", 
            description="コマンドはy!gacha [ガチャ番号]", 
            color=discord.Colour.green(), inline=False)
        em5.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
        em5.add_field(name="ガチャ種類＋番号一覧",
                        value="‣__**通常ガチャ**　番号：1__\n色々よくわからないものが出てくるよ。\nたまに隠しコマンドが出てくるとかなんとか\ny!gacha 1\n\n‣__**おにゃのこガチャ**　番号：2__\n可愛いおにゃのこの画像がいっぱいだよ\n可愛いの純度１００％！\ny!gacha 2")
        em5.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.5/7")

        #━Helpの6ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em6desc='y!kuji│`御籤`'
        em6desc += '\ny!dice [上限] [下限]│`サイコロ`'
        em6desc += '\ny!slot│`絵文字スロット`'
        em6desc += '\ny!fsg│`絵文字釣り`'
        em6 = discord.Embed(title="その他娯楽だよ",description=em6desc, color=discord.Colour.green())
        em6.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/635993816297504809/642579874816720916/money_slot_machine.png")
        em6.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.6/7")

        #━Helpの7ページ目━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        em7 = discord.Embed(
            title='YUI関連URL\n',
            description = (f"[YUI招待URL]({yui_url})\n" +
                           "[YUIサポートBot Mio 招待URL](https://discordapp.com/oauth2/authorize?client_id=644153226597498890&permissions=8&scope=bot)" + 
                           "\n[YUI Official Server 招待URL](https://discord.gg/Qn5QDfJ)"
        ))
        em7.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.7/7")

        page_count = 0  # ヘルプの現在表示しているページ数
        page_content_list = [em0,em1,em2,em3,em4,em5,em6,em7]  # ヘルプの各ページ内容

        send_message = await message.channel.send(embed=page_content_list[0])  # 最初のページ投稿
        await send_message.add_reaction("❎")
        await send_message.add_reaction("☑️")

        def help_react_check(reaction, user):

            if reaction.message.id != send_message.id:
                return 0
            if reaction.emoji in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '⬅️', '➡️', '🗑', '☑️', '❎', '⏭️', '⏮️']:
                if user != message.author:
                    return 0
                else:
                    return reaction, user

        while not client.is_closed():

            try:
                reaction, user = await client.wait_for('reaction_add', check=help_react_check, timeout=40.0)
            except:
                return

            else:

                if reaction.emoji in ["➡️", "☑️"] and page_count < 8:
                    page_count += 1
                if reaction.emoji == "⬅️" and page_count > 0:
                    page_count -= 1
                if reaction.emoji == "⏮️" and page_count > 2:
                    page_count -= 2
                if reaction.emoji == "⏭️" and page_count > 0 and page_count < 7:
                    page_count += 2
                if reaction.emoji in ['🚮', '❎','🗑']:
                    await send_message.delete()

                await send_message.clear_reactions()
                await send_message.edit(embed=page_content_list[page_count])
                reactions0 = ["⏮️","⬅️","🗑","➡️","⏭️"]
                reactions1 = ["⏮️","⬅️","🗑"]
                reactions2 = [":ballot_box_with_check:","❎"]
                reactions3 = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","","🗑"]
                if page_count == 0:
                    for reaction in reactions2:
                        await send_message.add_reaction(reaction)
                elif page_count == 1:
                    for reaction in reactions0:
                        await send_message.add_reaction(reaction)
                elif page_count == 2:
                    for reaction in reactions0:
                        await send_message.add_reaction(reaction)
                elif page_count == 3:
                    for reaction in reactions0:
                        await send_message.add_reaction(reaction)
                elif page_count == 4:
                    for reaction in reactions0:
                        await send_message.add_reaction(reaction)
                elif page_count == 5:
                    for reaction in reactions0:
                        await send_message.add_reaction(reaction)
                elif page_count == 6:
                    for reaction in reactions0:
                        await send_message.add_reaction(reaction)
                elif page_count == 7:
                    for reaction in reactions1:
                        await send_message.add_reaction(reaction)

        embed=discord.Embed(
            title=f"( 'ω'o[**help**]oログ♡",
            description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{author_id}』\n使用ch名│『{message.channel.name}』```')
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text = datetime.now(JST))
        await log_ch.send(embed=embed)

#━━━━❮YUI強制シャットダウンコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith('y!kill'):
        embed = discord.Embed(title=f"**Received command!!**",
                                  description="**checking user ID** <a:loadinfo:651635984068378663>")
        embed.set_footer(icon_url=message.author.avatar_url, text=f"認証中│{message.author.name}")
        test_send = await message.channel.send(embed=embed)
        await asyncio.sleep(2)
        if message.author == amano:
            
            embed = discord.Embed(
                title=f"**Received command!!**",
                description="**Agreement! Continue?**")
            embed.set_footer(icon_url=message.author.avatar_url, text=f"認証済み│{message.author.name}")
            await test_send.edit(embed = embed)
            reactions = ["❎","☑️"]
            for reaction in reactions:
                await test_send.add_reaction(reaction)

            def kill_react_check(reaction, user):
                if reaction.message.id != test_send.id:
                    return 0
                if reaction.emoji in ['☑️', '❎']:
                    if user != message.author:
                        return 0
                    else:
                        return reaction, user
                return 1
            try:
                reaction, user = await client.wait_for('reaction_add', check=kill_react_check, timeout=40)
            except asyncio.TimeoutError:
                await message.channel.send("time out")
            else:
                if reaction.emoji == '☑️':
                    await message.channel.send(embed=discord.Embed(title='Start LogOut'))
                    await client.logout()
                    await sys.exit()
                elif reaction.emoji == '❎':
                    await test_send.delete()
        else:
            embed = discord.Embed(
                title=f"**Not Authenticated!!**",
                description="**Your ID has not been registered**")
            embed.set_footer(icon_url=message.author.avatar_url, text=f"認証失敗│{message.author.name}")
            await test_send.edit(embed = embed)
#━━━━❮Cleanコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith ('y!clean '):
        log_ch = client.get_channel(699123211232739528)
        clean_num = message.content.split("y!clean ")[1]
        if message.author.guild_permissions.administrator or message.author == amano:
            await message.channel.purge(limit=int(clean_num))
            embed = discord.Embed(title = "メッセージ消去完了！",
                description=f"{clean_num}のメッセージを消去したよ",
                color = discord.Color.green())
            embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/635993816297504809/652423808086573096/57_20191206171856.png")
            embed.set_footer(icon_url=message.author.avatar_url, text=f"コマンド使用者│{message.author}")
            sendmsg = await message.channel.send(embed=embed)
            await asyncio.sleep(10)
            await sendmsg.delete()
            author_id=str(message.author.id)
            embed=discord.Embed(
                title=f"( 'ω'o[**clean**]oログ♡",
                description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{author_id}』\n使用ch名│『{message.channel.name}』\nメッセージ消去数│『{clean_num}』```')
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text = datetime.now(JST))
            await log_ch.send(embed=embed)
        else:
            embed = discord.Embed(title = "権限エラー！",
            description=f"{clean_num}のメッセージを消去しようとしたけど、どうやら君は管理者権限を持ってないみたいだね。\n悪いけど、このコマンドは荒らし対策として管理者以外使えないようになってるんだ。\nつまり出直して来いってこと",
            color = discord.Color.green())
            embed.set_thumbnail(url = "https://media.discordapp.net/attachments/635993816297504809/650725910915317773/4c2218f5cc96ba76c0e590cd1dadb1bc.gif")
            embed.set_footer(icon_url=message.author.avatar_url, text="コマンド使用未遂者│{message.author}")
            await message.channel.send(embed=embed)

#━━━━❮入っている鯖URL一覧コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == "y!glist" and message.author == amano:
        Num = 1
        guilds = set(client.guilds)
        for G in guilds:
            M = G.get_member(client.user.id)
            if M.guild_permissions.administrator:
                URL = await G.invites()
                if URL:
                    text = f"{Num})[{G.name}]({URL[0]})"
            else:
                text = f"{Num}){G.name}"
            Num += 1
            embed = discord.Embed(description = text)
            MSG = await message.channel.send(embed = embed)



#━━━━❮atkchコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    global test_ch
    global test_flag
    global test_user
    global test_guild
    global start_time

    if message.content.startswith("y!atkch "):
        g_ch=discord.utils.get(message.guild.text_channels,name=f'global_yui') 
                                                                   
        if not g_ch:
            embed = discord.Embed(
                title = 'global_yuiチャンネルがありません!!',
                description = f'この鯖には`global_yui`チャンネルがありません。\natkchコマンドの使用に関する通知が送信されてくるため、必ず`global_yui`チャンネルを設置してください。',
                color = discord.Color.red())
            await message.channel.send(embed = embed)
            return   
                                                                   
        if test_flag==True:
            embed = discord.Embed(
                title = '他の人が使用中です!!',
                description = f'```現在の使用者『{test_user}』\n使用中の場所『{test_guild}の{test_ch}』\n使用開始時刻『{start_time}』```',
                color = discord.Color.red())
            await message.channel.send(embed = embed)
            return 

        test_ch_m = message.content.split('y!atkch ')[1]
        test_ch = discord.utils.get(message.guild.text_channels, mention=test_ch_m)
        test_user = message.author
        test_guild = message.guild
        start_time = datetime.now(JST)
        
        if not test_ch:
            return
        
        test_flag=True
        await test_ch.send("::attack")
        log_ch = client.get_channel(699123211232739528)
        embed=discord.Embed(
            title=f"( 'ω'o[**atkch**]oログ♡",
            description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{message.author.id}』\n使用ch名│『{message.channel.name}』\n指定ch名│『{test_ch.name}』```')
        embed.set_thumbnail(url=message.author.avatar_url)
        await log_ch.send(embed=embed)
        embed=discord.Embed(title='Auto Battle開始')
        await message.author.send(embed=embed)
        embed = discord.Embed(
            title = "自動戦闘機能始動通知",
            description=f"**{test_ch.name}**でのYUIの自動戦闘を開始しました。\n[現在戦闘中のサーバーURL]({inviteurl_list[0]})",
            color=discord.Color.blue())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/659916967628767252/682888152180064256/mail_notification_27004-300x300.jpg")
        embed.set_author(icon_url=message.author.avatar_url,name = f"{message.author}")
        embed.set_footer(icon_url=message.guild.icon_url, text=f"{message.guild.name}")
        embed.timestamp = datetime.now(JST)
        await message.delete()
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == "global_yui":
                    await channel.send(embed=embed)


    if message.content=='y!atkstop':
        if test_flag == False:
            embed = discord.Embed(title = '現在Auto Battleは使用されていません。')
            await message.channel.send(embed=embed)
            return

        test_flag=False
        await asyncio.sleep(10)
        await test_ch.send('::re')
        embed=discord.Embed(title='Auto Battle停止')
        await message.author.send(embed=embed)
        embed=discord.Embed(title=f'{message.author}さんがAuto Battleを止めました')
        await test_user.send(embed = embed)        
        embed = discord.Embed(
            title = "自動戦闘機能停止通知",
            description=f"**{test_ch.name}**でのYUIの自動戦闘を停止しました。\n[現在戦闘中のサーバーURL]({inviteurl_list[0]})",
            color=discord.Color.blue())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/659916967628767252/682888152180064256/mail_notification_27004-300x300.jpg")
        embed.set_author(icon_url=message.author.avatar_url,name = f"{message.author}")
        embed.set_footer(icon_url=message.guild.icon_url, text=f"{message.guild.name}")
        embed.timestamp = datetime.now(JST)
        await message.delete()
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == "global_yui":
                    await channel.send(embed=embed)
        test_user = None
        test_guild = None
        test_ch = None

                    
    if message.channel == test_ch and message.embeds and test_flag==True:
        if message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:
            lv=message.embeds[0].title.split('Lv.')[1].split(' ')[0]
            type=message.embeds[0].title.split('[')[1].split(']')[0]
            rank=message.embeds[0].title.split('【')[1].split('】')[0]
            name=message.embeds[0].title.split('\n')[1].split('が待ち構えている')[0]
 

            if rank == '超激レア':
                pass
                if 1 == 1:
                    if 'フロスト' in name :
                        await test_ch.send('::re')
                    else:
                        await test_ch.send('::attack')
            
            else:
                await test_ch.send("::attack 先手必勝!!")

    if message.channel==test_ch and test_flag==True:
        if f"{client.user.name}はやられてしまった" in message.content:
            def mio_check(mio_msg):
                if mio_msg.author!=tao:
                    return 0
                if mio_msg.channel!=test_ch:
                    return 0
                if not mio_msg.embeds:
                    return 0
                if not f'{client.user.mention}は復活した' in mio_msg.embeds[0].description:
                    return 0
                return 1
            try:
                re_msg=await client.wait_for('message',timeout=0.5,check=mio_check)
            except asyncio.TimeoutError:
                await test_ch.send('::i e　復活')
            else:
                if f'{client.user.mention}は復活した' in re_msg.embeds[0].description:
                    await asyncio.sleep(0.5)
                    await test_ch.send('::attack　復活！')

        elif f"{client.user.name}の攻撃" in message.content and f"{client.user.name}のHP" in message.content and not f"{client.user.name}はやられてしまった" in message.content:
            await asyncio.sleep(0.2)
            await message.channel.send("::attack")

        elif message.embeds and message.embeds[0].description:
            if 'このチャンネルの全てのPETが全回復した！' in message.embeds[0].description:
                await asyncio.sleep(0.2)
                await test_ch.send('::attack 復活乁( ˙ ω˙乁)')

            elif f"{client.user.mention}はもうやられている！" in message.embeds[0].description:
                await asyncio.sleep(0.2)
                await test_ch.send("::i e 復活！")
                
                
                
                
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
                await test_ch.send(f'::item f ')
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
                await test_ch.send(f'::attack ')
            else:
                pass
 
#━━━━❮おーとFBコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith("y!ifch "):
        atk_ch_m = message.content.split('y!ifch ')[1]
        atk_ch2 = discord.utils.get(message.guild.text_channels, mention=atk_ch_m)
        log_ch = client.get_channel(699123211232739528)
        author_id=str(message.author.id)
        embed=discord.Embed(
        title=f"( 'ω'o[**ifch**]oログ♡",
        description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{author_id}』\n使用ch名│『{message.channel.name}』\n指定ch名│『{atk_ch2.name}』```')
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text = datetime.now(JST))
        await log_ch.send(embed=embed)
        await atk_ch2.send(f"{message.author.mention}\nチャンネル指定完了")
        await atl_ch2.send('::item f')

    if tao:
        if message.channel==atk_ch2:
            if f"{client.user.name}は" in message.content and 'のHP' in message.content:
                await asyncio.sleep(0.2)
                await message.channel.send(f"::item ファイアボールの書")

            if "やられてしまった" in message.content:
                if not mio:
                    await asyncio.sleep(1)
                    await atk_ch2.send("::i e　あわわヾ(・ω・`；))やられちゃった")
                    try:
                        await client.wait_for('message',timeout=300)
                    except asyncio.TimeoutError:
                        await message.channel.send('::attack TAO息してる…?')
                if mio :
                    def mio_msg(m_msg):
                        if m_msg.author!=mio:
                            return 0
                        if m_msg.channel!=message.channel:
                            return 0
                        return 1
                    try:
                        m_return=await client.wait_for('message',timeout=3,check = mio_msg)
                    except asyncio.TimeoutError:
                        await message.channel.send('::i e みおが返事してくれない……')
                    else:
                        if "::i i {client.user.mention}" in m_return.content:
                            try:
                                tao_return=await client.wait_for('message',timeout=5)
                            except asyncio.TimeoutError:
                                await message.channel.send('::i e TAOが反応しなかった…………')
                            else:
                                if tao_return.embeds and f"{client.user.mention}は復活した" in tao_return.embeds[0].description:
                                    await asyncio.sleep(2)
                                    await message.channel.send("::attack 私復活！　ありがと、みおちゃん")
            if message.embeds:
                if message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:
                    await asyncio.sleep(0.2)
                    await atk_ch2.send("::item f 先手必勝!!")

                elif message.embeds[0].description:
                    if f"{client.user.mention}はもうやられている！（戦いをやり直すには「::reset」だ）" in message.embeds[0].description:
                        members=message.guild.members
                        if not mio in members:
                            await asyncio.sleep(3)
                            await message.channel.send("::item e　あれ!? 私死んでるの!?")
                            try:
                                await client.wait_for('message',timeout=300)
                            except asyncio.TimeoutError:
                                await message.channel.send('::item e TAO息してる…?')

                    elif "エリクサーを" in message.embeds[0].description :
                        await asyncio.sleep(0.2)
                        await message.channel.send("::i f 私復活!!")

        
#━━━━❮YuiLvUPログコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.embeds and message.embeds[0].description and message.author in [tao,TAO] :
        pass
        if f"{client.user.mention}はレベルアップした！" in message.embeds[0].description:
            dateTime = datetime.now(JST)
            lv = message.embeds[0].description.split("`")[1]
            log_embed = discord.Embed(
                title = "━<:Lv:643122451500367902><:UP:643122445213106176>━",
                description = f"**__{lv}__**",
                color = discord.Color.green())
            log_embed.add_field(name = "**‣LvUP鯖Name**" ,value = f"『{message.guild.name}』",inline = False)
            log_embed.add_field(name = "**‣LvUP鯖ID**" ,value = f"『{message.guild.id}』",inline = False)
            log_embed.add_field(name = "**‣LvUPチャンネルName**" ,value = f"『{message.channel.name}』",inline = False)
            log_embed.add_field(name = "**‣LvUPチャンネルID**" ,value = f"『{message.channel.id}』",inline = False)
            log_embed.set_footer(text = f"{dateTime.year}年{dateTime.month}月{dateTime.day}日　{dateTime.hour}時{dateTime.minute}分{dateTime.second}秒")
            lvlog_ch = client.get_channel(699124286425792522)
            await asyncio.gather(*(c.send(embed=log_embed) for c in client.get_all_channels() if c.name == "yuiレベルアップログ"))
            await lvlog_ch.send(embed = log_embed)

#━━━━❮TAO敵出現ログコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.author==tao and message.embeds and message.embeds[0].title:

        if '待ち構えている' in message.embeds[0].title:
            dateTime = datetime.now(JST)
            lv=message.embeds[0].title.split('Lv.')[1].split(' ')[0]
            type=message.embeds[0].title.split('[')[1].split(']')[0]
            rank=message.embeds[0].title.split('【')[1].split('】')[0]
            name=message.embeds[0].title.split('】\n')[1].split('が待ち構えている')[0]
            image_url=message.embeds[0].image.url
            hp=message.embeds[0].title.split(':')[3]
            exp=int(lv)

            if rank=='超強敵' or rank=='レア':
                exp=int(lv)*5

            elif rank=='強敵':
                exp=int(lv)*1.5

            elif rank=='激レア':
                exp=int(lv)*33

            elif rank=='超激レア':
                exp=int(lv)*100

            embed=discord.Embed(title=f'モンスター出現ログ',description=f'\n**‣Name:**\n`{name}`\n**‣Type Rank:**\n`{type}┃{rank}`\n**‣Status:**\n`Lv.{lv}┃HP.{hp}`\n**‣Exp:**\n`{exp+1}`\n**‣Channel:**\n{message.channel.mention}',color=discord.Color.green())
            embed.set_thumbnail(url=image_url)
            embed.set_footer(text = f"{dateTime.year}年{dateTime.month}月{dateTime.day}日　{dateTime.hour}時{dateTime.minute}分{dateTime.second}秒")
            ch1=discord.utils.get(message.guild.text_channels, name=f'tao出現ログ：×1')
            ch2=discord.utils.get(message.guild.text_channels, name=f'tao出現ログ：×1．5')
            ch3=discord.utils.get(message.guild.text_channels, name=f'tao出現ログ：×5')
            ch4=discord.utils.get(message.guild.text_channels, name=f'tao出現ログ：×33')
            ch5=discord.utils.get(message.guild.text_channels, name=f'tao出現ログ：×100')

            if rank == "通常" and ch1:
                await ch1.send(embed=embed)
            if rank == "強敵" and ch2:
                await ch2.send(embed=embed)
            if rank in ["超強敵","レア"] and ch3:
                await ch3.send(embed=embed)
            if rank == "激レア" and ch4:
                await ch4.send(embed=embed)
            if rank == "超激レア" and ch5:
                await ch5.send(embed=embed)

            if message.guild.id == 674983696977362965:
                ch = (message.channel.name).split('-')[0]
                chlv = (message.channel.name).split('-')[1]
                LV = int(int(lv)/10)*10
                if chlv != LV:
                    await message.channel.edit(name = f'{ch} Lv{LV}')


    if message.content.startswith('y!sinka 0'):
        num=message.content.split('y!sinka ')
        await message.channel.send('::sinka')
        def role_check(tao_msg):
            if not tao_msg.embeds:
                return 0
            if tao_msg.channel != message.channel:
                return 0
            return 1

        try:
            re_msg = await client.wait_for('message', timeout=40, check=role_check)
        except:
            embed = discord.Embed(title='Error!!', description='もう一度試して見てね（￣▽￣;）\nもしかして以下の点が該当してないかな？\n‣TAOからの反応が40秒以内に来なかった\n‣TAOがオフライン\n‣TAOが修理中', color=discord.Color.green())
            await message.channel.send(embed=embed)
        else:
            await asyncio.sleep(2)
            await re_msg.add_reaction('👍')
            await asyncio.sleep(4)
            await re_msg.add_reaction('\u0030\u20e3')
 
    if message.content.startswith('y!sinka 1'):
        num=message.content.split('y!sinka ')
        await message.channel.send('::sinka')
        def role_check(tao_msg):
            if not tao_msg.embeds:
                return 0
            if tao_msg.channel != message.channel:
                return 0
            return 1

        try:
            re_msg = await client.wait_for('message', timeout=40, check=role_check)
        except:
            embed = discord.Embed(title='Error!!', description='もう一度試して見てね（￣▽￣;）\nもしかして以下の点が該当してないかな？\n‣TAOからの反応が40秒以内に来なかった\n‣TAOがオフライン\n‣TAOが修理中', color=discord.Color.green())
            await message.channel.send(embed=embed)
        else:
            await asyncio.sleep(2)
            await re_msg.add_reaction('👍')
            await asyncio.sleep(4)
            await re_msg.add_reaction('\u0031\u20e3')


#━━━━❮Say系コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#


    if message.content.startswith("y!say1 "):
        msg=message.content.split("y!say1 ")[1]
        if msg:
            if message.mentions or message.mention_everyone:
                if message.author.guild_permissions.administrator:
                    await message.delete()
                    await message.channel.send(msg)

                else:

                    embed = discord.Embed(title="権限エラー！！",description=f"{message.author.mention}\n君…管理者権限ないよね?\nメンション出来ると思ってるの?"
                                 ,color=0x2ECC69)
                    embed.set_thumbnail(url="https://yahoo.jp/box/JAzR8X")
                    await message.channel.send(embed=embed)
            else:
                await message.delete()
                await message.channel.send(msg)

    if message.content.startswith("y!say2 "):
        await message.delete()
        msg=message.content.split('"')[1]
        msg2=message.content.split('"')[3]
        if msg and msg2:
            embed=discord.Embed(title=msg,description=msg2)
            embed.set_footer(icon_url=message.author.avatar_url,text=f'発言者│{message.author}')
            if message.mentions or message.mention_everyone:
                if message.author.guild_permissions.administrator:

                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title="権限エラー！！",description=f"{message.author.mention}\n君…管理者権限ないよね?\nメンション出来ると思ってるの?"
                                 ,color=0x2ECC69)
                    embed.set_thumbnail(url="https://yahoo.jp/box/JAzR8X")
                    await message.channel.send(embed=embed)
            else:
                await message.channel.send(embed=embed)

    if message.content.startswith("y!report "):
        report_ch = client.get_channel(699123602787795018)
        reply = message.content.split('y!report ')[1]
        embed = discord.Embed(title=f'レポート内容\n```{reply}```', description=f"{developer.mention}\n発言者{message.author.mention}", color=0x2ECC69)
        embed.add_field(name="レポート提出時刻",
        value=f"{datetime.now(JST)}", inline=True)
        await report_ch.send(embed=embed)
        embed = discord.Embed(title='レポート提出完了！',
        description=f"{message.author.mention}さん\nレポート提出有り難う！\n君のレポートは無事研究所に届けられたよ！\n```{reply}```",
        color=0x2ECC69)
        embed.add_field(name="レポート提出時刻",
        value=f"{datetime.now(JST)}", inline=True)
        await message.channel.send(embed=embed)

#━━━━❮TAO系コマンド基本コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == 'y!st':
        await message.channel.send('::st')
        log_ch=client.get_channel(699123211232739528)
        embed=discord.Embed(
        title=f"( 'ω'o[**status window**]oログ♡",
        description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{message.author.id}』\n使用ch名│『{message.channel.name}』```')
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text = datetime.now(JST))
        await log_ch.send(embed=embed)

    if message.content == 'y!re':
        await message.channel.send('::reset')

    if message.content == 'y!i e':
        await message.channel.send('::i e')

    if message.content == 'y!atk':
        await message.channel.send("::attack")
        log_ch=client.get_channel(699123211232739528)
        embed=discord.Embed(
            title=f"( 'ω'o[**attack**]oログ♡",
            description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{message.author.id}』\n使用ch名│『{message.channel.name}』```')
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text = datetime.now(JST))
        await log_ch.send(embed=embed)

    if message.content == 'y!i f':
        await message.channel.send('::i f')
        log_ch=client.get_channel(699123211232739528)
        embed=discord.Embed(
            title=f"( 'ω'o[**i f**]oログ♡",
            description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{message.author.id}』\n使用ch名│『{message.channel.name}』```')
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text = datetime.now(JST))
        await log_ch.send(embed=embed)

    if message.content == 'y!rmap':
        await message.channel.send('::rmap')

    if message.content.startswith('y!sinka '):
        await message.channel.send('::sinka')
        reaction=message.content.split('y!sinka ')[1]
        def role_check(tao_msg):
            if not tao_msg.embeds:
                return 0
            if tao_msg.channel != message.channel:
                return 0
            return 1

        try:
            ans_msg = await client.wait_for('message', timeout=40, check=role_check)
        except:
            embed = discord.Embed(title='Error!!', description='もう一度試して見てね（￣▽￣;）\nもしかして以下の点が該当してないかな？\n‣TAOからの反応が40秒以内に来なかった\n‣TAOがオフライン\n‣TAOが修理中', color=discord.Color.green())
            await message.channel.send(embed=embed)
        else:
            await asyncio.sleep(2)
            await ans_msg.add_reaction(reaction)
            
    if message.content.startswith('y!role '):
        role_num = message.content.split('y!role ')[1]
        if not role_num in ["0","1","2","3"] or message.content==('y!role'):
            embed = discord.Embed(
                              title='番号エラー!',
                              description=f'{role_num}に該当する役職はないよ!\n**役職番号**\n0│Adventure系\n1│Warrior系\n2│Mage系\n3│Thief系\nコマンドは`y!role [役職番号]`だよ。',
                              color=discord.Color.red())
            embed.set_footer(icon_url={message.author.avatar_url},text=f"{message.author.name}")
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(f'::role　{role_num}')

                
    if message.content == 'y!i':
        await message.channel.send('::i')

    if message.content == 'y!login':
        await message.channel.send('::login')

#━━━━❮TAO出現ログ役職コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == 'y!tgrare':
        role = discord.utils.get(message.guild.roles, name='超激レア通知')  # YUI通知
        if role:
            await message.author.add_roles(role)
            reply = discord.Embed(title='役職を付与完了!!',description=f'{message.author.mention} に{role.mention}をつけたよ')
            await message.channel.send(embed=reply)
        else:
            role = await message.guild.create_role(name='激レア通知',mentionable=True)
            await message.author.add_roles(role)
            reply = discord.Embed(title='役職を付与完了!!',description=f'役職がなかったから新たに作って{message.author.mention} に{role.mention}をつけたよ')

    if message.content == 'y!grare':
        role = discord.utils.get(message.guild.roles, name='激レア通知')  # YUI通知
        if role:
            await message.author.add_roles(role)
            reply = discord.Embed(title='役職を付与完了!!',description=f'{message.author.mention} に{role.mention}をつけたよ')
            await message.channel.send(embed=reply)
        else:
            role=await message.guild.create_role(name='激レア通知',mentionable=True)
            await message.author.add_roles(role)
            reply = discord.Embed(title='役職を付与完了!!',description=f'役職がなかったから新たに作って{message.author.mention} に{role.mention}をつけたよ')


#━━━━❮くじコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == "y!kuji":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        num_random = random.randrange(1, 6)
        url1 = 'https://cdn.discordapp.com/attachments/635993816297504809/641195024033251328/29_20191105173957.png'
        url2 = 'https://cdn.discordapp.com/attachments/635993816297504809/641196128137904128/29_20191105174422.png'
        url3 = 'https://cdn.discordapp.com/attachments/635993816297504809/641197802436952065/29_20191105174815.png'
        url4 = 'https://cdn.discordapp.com/attachments/635993816297504809/641198139537227776/29_20191105175219.png'
        url5 = 'https://cdn.discordapp.com/attachments/635993816297504809/641200232826142730/29_20191105180042.png'
        await message.channel.send('くじ引いてく？')
        await asyncio.sleep(3)
        embed = discord.Embed(title="**ディスコ神社│御籤コーナー\n( 厂˙ω˙ )厂うぇーい**", description='''がさ
 がさ
  がさ''', color=0x2ECC69)
        embed.add_field(name='**紙切れがでてきた…！！**', value='さあさあ今日の運勢は……!?')
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/635993816297504809/641207863506632715/28_20191105183055.png')
        embed.set_footer(icon_url=message.author.avatar_url, text=f"御籤使用者│{message.author.name}")
        if num_random == 1:
            embed.set_image(url=url1)
            await message.channel.send(embed=embed)
            wards = ['お、大吉!!\nいいねいいね!!',
                     'いいじゃん大吉！',
                     '大吉だよ、今日はついてるんじゃない？',
                     'ラッキーだね。なんかいいことあるかもだよ。',
                     'あ＾～大吉入りました！',
                     '大吉ktkr!!',
                     '大吉　やるやん。',
                     '大吉も数引きゃ当たるってね'
                    ]
            ward = random.choice(wards)
            await message.channel.send(ward)

        elif num_random == 2:
            embed.set_image(url=url2)
            await message.channel.send(embed=embed)
            wards = ['小吉かぁ～、このくじ中吉ないからそこまで落ち込むこともないよ(汗',
                     '凶とかじゃないだけまだましだって',
                     'まあおみくじなんて当たるも八卦当たらぬも八卦と言うしね',
                     '最高で５連続凶出した人いるからセーフだよ',
                     'まあこのおみくじ無料だし']
            ward = random.choice(wards)
            await message.channel.send(ward)

        elif num_random == 3:
            embed.set_image(url=url3)
            await message.channel.send(embed=embed)
            await message.channel.send('ん...んん、末吉\nまぁまぁまぁ…ね?')

        elif num_random == 4:
            embed.set_image(url=url4)
            await message.channel.send(embed=embed)
            await message.channel.send('大凶!?\nえ、死ぬの!?')

        elif num_random == 5:
            embed.set_image(url=url5)
            await message.channel.send(embed=embed)
            await message.channel.send('すみませぇえええん\nこの御籤呪われてまあああああああす!!')

#━━━━❮ガチャコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == 'y!gacha':
        await message.channel.send('gachaばんごうをしていしてね......?')
        embed = discord.Embed(title="ガチャ機能だよ", description="コマンドはy!gacha [ガチャ番号]", color=0x2ECC69)
        embed.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
        embed.add_field(name="ガチャ種類＋番号一覧",
                        value="‣__**通常ガチャ**　番号：1__\n色々よくわからないものが出てくるよ。\nたまに隠しコマンドが出てくるとかなんとか\n\n‣__**おにゃのこガチャ**　番号：2__\n可愛いおにゃのこの画像がいっぱいだよ\n可愛いの純度１００％！")
        await message.channel.send(embed=embed)

    if message.content == "y!gacha 1":
        embed = discord.Embed(title = "□◑")
        tmp = await message.channel.send(embed = embed)
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　◒"))
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　　◐"))
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　　　◓"))
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　　　◖◗ﾊﾟｶｯ"))
        embed = discord.Embed(title="何かが出てきたよ!\nこれは…", color=0x2ECC69)
        embed.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
        embed.set_image(url=random.choice(("https://yahoo.jp/box/tpeHgW",
                                           "https://yahoo.jp/box/roWwt8", "https://yahoo.jp/box/M8DDfm",
                                           "https://yahoo.jp/box/5yaQwS", "https://yahoo.jp/box/snmtCk",
                                           "https://yahoo.jp/box/WI0bCW", "https://yahoo.jp/box/2DeZEI",
                                           "https://yahoo.jp/box/seZwkN", "https://yahoo.jp/box/UHhqck",
                                           "https://yahoo.jp/box/ZdKwTS", "https://yahoo.jp/box/coBg_L",
                                           "https://yahoo.jp/box/D8lFL8", "https://yahoo.jp/box/LU1JLi",
                                           "https://yahoo.jp/box/2tGQPm", 
                                           "https://yahoo.jp/box/2tGQPm", "https://yahoo.jp/box/W6sq6m",
                                           "https://yahoo.jp/box/o8_WCa", "https://yahoo.jp/box/bnadWl",
                                           "https://yahoo.jp/box/wvFtaX", "https://yahoo.jp/box/t6DACy",
                                           "https://yahoo.jp/box/Iz8VoJ", "https://yahoo.jp/box/QqiwDa",
                                           "https://yahoo.jp/box/XMZ_-6", "https://yahoo.jp/box/HYqbOS",
                                           "https://media.discordapp.net/attachments/635993816297504809/636080181991178250/20_20191022145513.png",
                                           "https://cdn.discordapp.com/attachments/635993816297504809/687348487288913941/108_20200312021725.png")))
        embed.add_field(name=random.choice(('最高に需要無いんだけど……', 
                                            'うわ何これ……いる？', 
                                            '……こんなのガチャガチャから出てこないよね普通',
                                            'ごめんちょっと意味わからないんだけどナニコレ', 
                                            "これもらって喜ぶ人いるのかな", '………ノーコメント',
                                            'なんて言えばいいんだろう',
                                            'なんでこれをガチャガチャに入れたし…'
                                           )
                                          ),
                        value='YUIは出てきたものをそっとポッケに入れた', inline=False)
        embed.set_footer(text = datetime.now(JST))
        await message.channel.send(embed=embed)

    if message.content == "y!gacha 2":
        embed = discord.Embed(title = "□◑")
        tmp = await message.channel.send(embed = embed)
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　◒"))
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　　◐"))
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　　　◓"))
        await asyncio.sleep(1)
        await tmp.edit(embed = discord.Embed(title = "□　　　◖◗ﾊﾟｶｯ"))
        embed = discord.Embed(title="なんか出てきた",
        color=discord.Colour.from_rgb(255, 133, 214))
        embed.set_thumbnail(url="https://yahoo.jp/box/lc5-cP")
        embed.set_image(url=random.choice(
                                          ("https://yahoo.jp/box/C5OhZ6","https://yahoo.jp/box/7wCPzz",
                                           "https://yahoo.jp/box/NTtrKt","https://yahoo.jp/box/1lR9DJ",
                                           "https://yahoo.jp/box/uIdpqC","https://yahoo.jp/box/YQlvC2",
                                           "https://yahoo.jp/box/sxklm2","https://yahoo.jp/box/LpiAUS",
                                           "https://yahoo.jp/box/xkG1WU","https://yahoo.jp/box/4T6wmr",
                                           "https://yahoo.jp/box/WEgd7D","https://yahoo.jp/box/6VLJXh",
                                           "https://yahoo.jp/box/yDuiFh","https://yahoo.jp/box/gtay8J",
                                           "https://yahoo.jp/box/-zJbpA","https://yahoo.jp/box/xH_xpw",
                                           "https://yahoo.jp/box/KQDNjd","https://yahoo.jp/box/XT5J4M",
                                           "https://yahoo.jp/box/AoWqBP","https://yahoo.jp/box/3CKNvk",
                                           "https://yahoo.jp/box/pFKU2Z","https://yahoo.jp/box/nH4vvY",
                                           "https://yahoo.jp/box/cqTkgv","https://yahoo.jp/box/kvCkil",
                                           "https://yahoo.jp/box/rvDbkR","https://yahoo.jp/box/znUdy5",
                                           "https://yahoo.jp/box/wmzu-Z","https://yahoo.jp/box/kXnYQf",
                                           "https://yahoo.jp/box/0cRE1S","https://yahoo.jp/box/Mz2rPI",
                                           "https://yahoo.jp/box/JzZEBY","https://yahoo.jp/box/o1Uma1",
                                           "https://yahoo.jp/box/YPaIEe","https://yahoo.jp/box/MANLfg",
                                           "https://yahoo.jp/box/e09Dte","https://yahoo.jp/box/iFQl2O",
                                           "https://yahoo.jp/box/EjWQbT",'https://yahoo.jp/box/3faN7k',
                                           'https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd'
                                          )
                                         )
                       )
        embed.add_field(
        name=random.choice( ('いや可愛いけどコメントに困る', 
                             'あ、かわいい', 
                             'ちょくちょくエッチなのは入ってるよねこれ（）', 
                             '可愛いというより萌えのほうが正しいのかなこれ', 
                             "普通にかわいいこれ", 
                             'あー悪くないかも')),
        value='YUIは出てきたおにゃのこカードをそっとポケットに仕舞った', inline=False)
        embed.set_footer(text = datetime.now(JST))
        await message.channel.send(embed=embed)

#━━━━❮フィッシングコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content=='y!fsg':
        emono_dect={
'⚙️歯車':'…錆びてるね',
'🔰ビギナーマークシール':'誰か運転初心者が車ごと突っ込んだのかな…?',
'🛡盾':'盾…うん盾……いやなんで釣れた…?',
'⌨️キーボード':'キーボード!?\n誰かがクラッシュしたの…!?',
'📱スマホ':'…さすがに電源は…\nいや、もしかしたら乾かしたら付くんじゃ…!?',
'🍑桃':'桃!?え、桃!?\n中から赤ちゃんが出てくるの!?',
'🍩ドーナッツ':'釣ったものじゃなかったら食べてたよ!',
'🏹弓':'…弓…?\nなんで弓…?',
'🚗車':'私車釣っちゃったの!????!!?',
'🚲自転車':'自転車の不法投棄は犯罪だよ…',
'🏆謎のトロフィー':'ん?\nこれ釣れていい奴…?',
'👁目':'目がぁあ\nメガァァアアア!\nｱｧｱｧｱ!!\nこっち見んな',
'⚔️双剣':'いや危な!?',
'💻パソコン':'パソコン!?\nキーボードでは飽き足らずついに本体が釣れちゃった!?',
'🐙タコ':'タコ。うん',
'🦀蟹':'カニかぁ\n好きだけど魚が釣りたいんだよねぇ',
'🐳クジラ':'くじっ、くじらぶふぉ!?',
'🦈サメ':'って、さめえええええええええええ!!??',
'🌿草ぁ！':'草ァ…',
'☘️草ぁ！':'くさァ…',
'🌱草ぁ！':'くさァ…',
'🍀四葉のクローバー':'草に変わりはないけど\n四つ葉のクローバーとはまたレアなものが…',
'🍄謎キノコ':'これだけはわかる\nこれ絶対食用じゃない()',
'🐟すごく普通な魚':'ま…まともなものが釣れた…!',
'🐊わに':'ｱﾘｹﾞｴｴﾀｧｧｱｱｱｱ!?!',
'📷カメラ':'流石にもう動かないね',
'🎷楽器':'楽器って高いんだけどなぁ',
'🎮ゲーム機':'…本体はあるのかな…?',
'🗑ダストボックス':'ゴミ箱かぁw\nゴミはよく釣れるけど\nゴミ箱かぁw',
'💉ちょっと危ない注射器':'…警察案件…!?',
'💊謎のお薬':'これもしかして\n危ないお薬…!?',
'💊💉薬＆注射器':'すごく危険なセット!!??',
'🛸UFOの残骸':'……え?',
'💎だぃやもんどぉ':'いやすごいけれども!?\nなんでここで釣れた!?',
'🖱マウス':'お、おうふ、マウスw\nキーボードもあるし本体もあるし\nこの池どうなってるの…w',
'🔋電池':'電池…\nさすがに動かないねぇ',
'💵かね':'金!?',
'🔧スパナ':'工具…',
'⌚腕時計':'絶妙に高そうな腕時計だね…',
'📺テレビ':'テレビwww\n前ゲーム機釣れたw\n一式揃ったwww',
'☎️金正恩':'電話…\n黒電話…\nキムjおっと誰か来たようだ',
'💣ﾊﾞｸﾀﾞｧﾝ！':'ｳﾜｱｱｱｱｱｱｱｱｱ!??!\nって、湿気てた()',
'🔪包丁':'いや危な!?',
'⚰️中身がありそうな棺桶':'………つっちゃってごめんなさあああああい!!',
'🍌Banana':'oh…\nIts so very good banana★',
'🍆心なしか汚い':'…なんか汚い',
'⚽名前が書いてあるボール':'ボールだ\nきっと間違って落としちゃったんだね…',
'🐱濡れたネコ':'ヌ(れたね)コw',
'🚽便座':'トイレ!?!?!',
}
        result_key=random.choice(list(emono_dect.keys()))
        result=emono_dect[result_key]
        embed=discord.Embed(title=f'**-YUIの釣り!-**\nお?　{result_key}が釣れたね!\n{result}',color=discord.Color.blue())
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/635993816297504809/659805550443233290/58_20191227021126.png')
        embed.timestamp = datetime.now(JST)

        await message.channel.send(embed=embed)

#━━━━❮アイコン表示コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == "y!myicon":
        embed = discord.Embed(title="**アイコン表示**\n", description='`アイコンを表示したよ`',
                              color=discord.Color(random.randint(0, 0xFFFFFF)))
        embed.set_image(url=message.author.avatar_url_as(size=1024))
        embed.set_footer(icon_url=message.author.avatar_url, text=f"表示者│{message.author}")
        await message.delete()
        await message.channel.send(embed=embed)

#━━━━❮サイコロコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith("y!dice "): 
        if client.user != message.author:
            x = message.content.split(" ", 2)
            dice = x[1]
            dice2 = x[2]
            num_random = random.randrange(int(dice), int(dice2))
            embed = discord.Embed(title="ゆいがサイコロ振るだけ", description='''指定範囲は''' + (dice) + 'から' + (dice2) + '!!\n' + '''なにがでるかなー
**__　''' + str(num_random) + ''' __**٩( 'ω' )و!!''', color=0x2ECC69)
            await message.channel.send(embed=embed)

    if message.content.startswith("y!nekoshima"):  # ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1, 10000)
            embed = discord.Embed(title="YUIの超激レア占い", description='''次の超激レア枠は～!!
**''' + str(num_random) + '''**体後!!　がんばー٩( 'ω' )و''', color=0x2ECC69)
            embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k',
                                                   'https://yahoo.jp/box/c9L236',
                                                   'https://yahoo.jp/box/Jxj1Jd')))
            await message.channel.send(embed=embed)

#━━━━❮スロットコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == "y!slot":
        slot_list = ['🍆', '🍒', '🔷', '🔶', '7️⃣', '💎','🔔', '🍆', '🍆', '🍆']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        A1 = random.choice(slot_list)
        A2 = random.choice(slot_list)
        A3 = random.choice(slot_list)
        B1 = random.choice(slot_list)
        B2 = random.choice(slot_list)
        B3 = random.choice(slot_list)
        C1 = random.choice(slot_list)
        C2 = random.choice(slot_list)
        C3 = random.choice(slot_list)
        if message.author != client.user:
            embed = discord.Embed(title=f'━━━━━━\n{A}│{B}│{C}\n{A1}│{B1}│{C1}◀\n{A2}│{B2}│{C2}',
                                  color=0x2ECC69)
            slot_em = await message.channel.send(embed=embed)
            await asyncio.sleep(1)
            await slot_em.edit(embed=discord.Embed(title=f'━━━━━━\n{A1}│{B1}│{C1}\n{A2}│{B2}│{C2}◀\n{A3}│{B3}│{C3}',color=0x2ECC69))
            await asyncio.sleep(1)
            await slot_em.edit(embed=discord.Embed(title=f'━━━━━━\n{A2}│{B2}│{C2}\n{A3}│{B3}│{C3}◀\n{A}│{B}│{C}',color=0x2ECC69))
            await asyncio.sleep(1)

            if A3 == B3 and B3 == C3:

                await slot_em.edit(embed=discord.Embed(title=f'━━━━━━\n{A2}│{B2}│{C2}\n{A3}│{B3}│{C3}◀\n{A}│{B}│{C}',description=f'結果\n{A3}のゾロ目だよ',color=discord.Color.blue()))
            else:

                await slot_em.edit(embed=discord.Embed(title=f'━━━━━━\n{A2}│{B2}│{C2}\n{A3}│{B3}│{C3}◀\n{A}│{B}│{C}',description=f'結果\n{A3}{B3}{C3}残念…',color=discord.Color.blue()))

#━━━━❮特殊チャンネル作成コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith("y!yui"):
        if message.content.split()[1] == "log":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='yui起動ログ')
            reply = f'{new_channel.mention} をつくったよ。私が起きたら此処で挨拶するから'
            return await message.channel.send(reply)

        elif message.content.split()[1] == "timelog":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='yui時報ログ')
            reply = f'{new_channel.mention} をつくったよ。日付が変わるタイミングでここでお知らせするから'


        elif message.content.split()[1] == "global":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='global_yui')
            reply = f'{new_channel.mention} をつくったよ。globalチャットに登録完了'

        elif message.content.split()[1] == "lv":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='global_yui')
            reply = f'{new_channel.mention} をつくったよ。YUIがLvUpしたら通知が届くよ'

            return await message.channel.send(reply)

    if message.content.startswith("y!tao "):
        if message.content.split()[1] == "1":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='tao出現ログ：×1')
            reply = f'{new_channel.mention} をつくったよ。TAOの通常モンスターの出現ログだよ'

        elif message.content.split()[1] == "1.5":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='tao出現ログ：×1．5')
            reply = f'{new_channel.mention} をつくったよ。TAOの強敵モンスターの出現ログだよ'

        elif message.content.split()[1] == "5":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='tao出現ログ：×5')
            reply = f'{new_channel.mention} をつくったよ。TAOの経験値５倍モンスターの出現ログだよ'

        elif message.content.split()[1] == "33":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='tao出現ログ：×33')
            reply = f'{new_channel.mention} をつくったよ。TAOの経験値倍率３３倍モンスターの出現ログだよ'

        elif message.content.split()[1] == "100":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='tao出現ログ：×100')
            reply = f'{new_channel.mention} をつくったよ。TAOの経験値倍率100倍モンスターの出現ログだよ'

        return await message.channel.send(reply)

#━━━━❮YUIWEATHERコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith("y!wt "):
        city = message.content.split("y!wt ")[1]
        if city in citycodes :
            city_num = citycodes[city]
            resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%city_num).read()
            resp = json.loads(resp.decode('utf-8'))

            desc = f"""{(resp['forecasts'][0]['date']).split('-')[1]}月{(resp['forecasts'][0]['date']).split('-')[2]}日
{resp['forecasts'][0]['dateLabel']}の天気は**{resp['forecasts'][0]['telop']}**"""
            desc += "\n"
            desc += "\n"
            desc += f"""{(resp[f'forecasts'][1]['date']).split('-')[1]}月{(resp['forecasts'][1]['date']).split('-')[2]}日
{resp['forecasts'][1]['dateLabel']}の天気は**{resp['forecasts'][1]['telop']}**"""
            desc += "\n"
            desc += f"最高気温**{resp['forecasts'][1]['temperature']['max']['celsius']}℃/{resp['forecasts'][1]['temperature']['max']['fahrenheit']}℉**"
            desc += "\n"
            desc += f"最低気温**{resp['forecasts'][1]['temperature']['min']['celsius']}℃/{resp['forecasts'][1]['temperature']['min']['fahrenheit']}℉**"
            desc += "\n"
            desc += "\n"
            desc += f"""{(resp[f'forecasts'][2]['date']).split('-')[1]}月{(resp['forecasts'][2]['date']).split('-')[2]}日
{resp['forecasts'][2]['dateLabel']}の天気は**{resp['forecasts'][2]['telop']}**"""

            embed = discord.Embed(
            title = "YUI Weather",
            description = f"**{city}の天気だよ！**\n\n{desc}",
            color = discord.Color.blue()
            )
            embed.set_footer(
            icon_url=message.author.avatar_url,
            text=f"コマンド使用者｜{message.author}"
            )
            embed.set_thumbnail(
            url=message.author.avatar_url
            )

        else:
            embed = discord.Embed(
            title = f"{city}なんて場所は私には登録されてないなー……"
            )

        await message.channel.send(embed=embed)

#━━━━❮サーバー情報コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content == 'y!sinfo':
        guild = message.guild
        role = next(c for c in guild.roles if c.name == '@everyone')
        t_locked = 0
        v_locked = 0
        online = 0
        offline = 0
        idle = 0
        dnd = 0
        pin = 0
        if guild.mfa_level == 0:
            mfamsg = "メンバーに2要素認証を必要としていません"
        else:
            mfamsg = "メンバーに2要素認証を必要としています"
        if guild.premium_subscription_count == None:
            pmmc = "0"
        else:
            pmmc = guild.premium_subscription_count
        for member in guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.status == discord.Status.dnd:
                dnd += 1
        for channel in guild.text_channels:
            if channel.overwrites_for(role).read_messages is False:
                t_locked += 1
        for channel in guild.voice_channels:
            if channel.overwrites_for(role).connect is False:
                v_locked += 1
        total = online + offline + idle + dnd
        if total > 499:
            large = "大"
        elif total > 249:
            large = "中"
        else:
            large = "小"
        embed = discord.Embed(title=f"サーバー情報", color=0x2ECC69)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="‣サーバー名", value=f"**{guild.name}**", inline=False)
        embed.add_field(name="‣サーバーの説明", value=f"**{guild.description}**", inline=False)
        embed.add_field(name="‣サーバーID", value=f"**{guild.id}**")

        embed.add_field(name="‣サーバーの大きさ", value=f"**{large}**")
        embed.add_field(name="‣サーバー地域", value=f"**{guild.region}**")
        embed.add_field(name="‣サーバーの旗", value=f"**{guild.banner}**")
        embed.add_field(name="‣オーナー", value=f"**{guild.owner.mention}**", inline=False)
        embed.add_field(name="‣チャンネル数",
                        value=f"総合チャンネル数　:**{len(guild.text_channels) + len(guild.voice_channels)}個**(🔒×**{t_locked + v_locked}**)\nテキストチャンネル:**{len(guild.text_channels)}個**(🔒×**{t_locked}**)\nボイスチャンネル　:**{len(guild.voice_channels)}個**(🔒×**{v_locked}**)")
        embed.add_field(name="‣カテゴリー数", value=f"**全て:{len(guild.categories)}**")
        embed.add_field(name="‣役職数", value=f"**{len(guild.roles)}職**", inline=False)
        embed.add_field(name="‣メンバー数",
                        value=f"総メンバー:**{total}人**\nオンライン:**{online}人**\nオフライン:**{offline}人**\n退席中　　:**{idle}人**\n取り込み中:**{dnd}人**",
                        inline=False)
        embed.add_field(name="‣サーバーのブースト状態",
                        value=f"サーバーブーストレベル　:**Lv.{guild.premium_tier}**\nサーバーブーストユーザー:**{pmmc}人**", inline=False)
        embed.add_field(name="‣二段階認証", value=f"**{mfamsg}**", inline=False)
        embed.set_footer(text = datetime.now(JST))
        await message.channel.send(embed=embed)

#━━━━❮チャンネル作成コード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith("y!mkch "):
        await message.delete()
        reply_one = message.content.split('y!mkch ')[1]
        guild = message.guild
        new_channel = await guild.create_text_channel(name=reply_one)
        reply = f'{new_channel.mention} を作成したよ!'

        await message.channel.send(reply)

#━━━━❮無駄隠しコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if message.content.startswith("y!timer "):
        await message.delete()
        time = int(message.content.split('y!timer ')[1])
        if timer > 60:
            await message.channel.send("60以下にしてね")
        if not time:
            embed = discord.Embed(
                title = '秘伝コマンド取扱説明書',
                description = '`y!timer [秒数]\nexample)\ny!timer 10`')
            await message.author.send(embed = embed)
            return

        m = await message.channel.send(embed = discord.Embed(title = f'COUNTDOWN\n{time}s'))
        await asyncio.sleep(1)
        while time >= 1:
        
            time -= 1
            if time == 0:
                await m.edit(embed = discord.Embed(title = f'COUNTDOWN\nTimeUp!!'))
                return
            await m.edit(embed = discord.Embed(title = f'COUNTDOWN\n{time}s'))
            await asyncio.sleep(1)


    if message.content == "y!gorogoro":
        await message.delete()
        tmp = await message.channel.send("(:3\_ヽ)_......")  # 編集するメッセージを保持
        await asyncio.sleep(0.5)
        await tmp.edit(content="(:3\_ヽ)_......ねむい......")
        await asyncio.sleep(0.5)
        await tmp.edit(content=".　( ε: )")
        await asyncio.sleep(0.5)
        await tmp.edit(content=".　　(.ω.)")
        await asyncio.sleep(0.5)
        await tmp.edit(content=".　　　( :3 )")
        await asyncio.sleep(0.5)
        await tmp.edit(content=".　　　　('ω')")
        await asyncio.sleep(0.5)
        await tmp.edit(content=".　　　　　(:3\_ヽ)_....")
        await asyncio.sleep(3)
        await tmp.edit(content=".　　　　　(:3\_ヽ)_....なにがしたかったんだろ")

    if message.content == "y!amanohashi":
        await message.delete()
        embed =discord.Embed(
            title = "私の生みの親だね。身内に不幸があってショックのあまり一時的にdiscordは引退してたけどなんだかんだあって一応復帰はしてるよ。\n何か用があったらLineからどうぞ")
        embed.set_image(url = "https://media.discordapp.net/attachments/659916967628767252/691476976212377600/my_qrcode_1575889719190.jpg")
        await message.channel.send(embed = embed)

    if message.content.startswith('y!send '):
        await message.delete()
        x = message.content.split(" ", 2)
        riptext2 = int(x[2])
        channel = client.get_channel(riptext2)
        riptext = x[1]
        await channel.send(riptext)

    """
    if message.content.startswith('y!books'):
        db_ch = client.get_channel(676442417414668289)
        msgs = await db_ch.history( limit = None ).flatten()
        j_list = []
        for msg in msgs:
            msgem = msg.embeds[0].description
            for match in re.finditer('【(.+?)】',msgem):
                print(j_list)
                if not match[1] in j_list:
                    j_list.append(match[1])
        J_list = list(set(j_list))     
        genres = '│'.join(j_list)
        embed = discord.Embed(
            title='見つかったジャンル(太文字は閲覧注意です)',
            description=f'||{genres}||')
        embed.timestamp = datetime.now(JST)
        await message.author.send(embed = embed)
    """
   

    if message.content.startswith("y? "):
        word_list = message.content.split(" ")
        del word_list[0]
        print(word_list)
        words = word_list[0]
        del word_list[0]
        for word in word_list:
            words += "+"
            words += word

        kensaku = f'https://www.google.com/search?q={words}'
        embed = discord.Embed(title = f"**{words}**の検索結果だよ！",description = f"[ここからどうぞ]({kensaku})")
        embed.timestamp = datetime.now(JST)
        await message.channel.send(embed =embed)
        

#━━━━❮グローバルチャットコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

    if (len(message.embeds) == 0) and (message.channel.name == "global_yui") and (not "discord.gg" in message.author.name):
        list_ch = client.get_channel(699849279875055657)
        tmp = await list_ch.history( limit = None ).flatten()
        if message.author.id in tmp:
            await message.channel.send(embed = discord.Embed(title = "あなたにグローバルチャットを使う権限がありません。"))
            return
        content = re.sub(r"(https://discord.gg/)([\w]*)", r"||\1\2||", message.content)
        msg_at = message.attachments
        await message.add_reaction("📤")
        if content:
            embed = discord.Embed(
                description=f"{content}",
                color=discord.Color(random.randint(0, 0xFFFFFF)))
            embed.set_author(icon_url=message.author.avatar_url,name = f"{message.author}")
            embed.set_footer(icon_url=message.guild.icon_url, text=f"{message.guild.name}")
            embed.timestamp = datetime.now(JST)
            if msg_at:
                embed.set_image(url = message.attachments[0].url)
            for guild in client.guilds:
                for channel in guild.channels:
                    if channel.name == "global_yui":
                        await channel.send(embed=embed)
            else:
                await message.add_reaction("✅")
                await asyncio.sleep(1)
                await message.delete()
        else:
            embed = discord.Embed(color=discord.Color(random.randint(0, 0xFFFFFF)))
            embed.set_author(icon_url=message.author.avatar_url,name = f"{message.author}")
            embed.set_footer(icon_url=message.guild.icon_url, text=f"{message.guild.name}")
            embed.timestamp = datetime.now(JST)
            if msg_at:
                embed.set_image(url = message.attachments[0].url)
            for guild in client.guilds:
                for channel in guild.channels:
                    if channel.name == "global_yui":
                        await channel.send(embed=embed)
            else:
                await message.add_reaction("✅")
                await asyncio.sleep(1)
                await message.delete()


    if message.content.startswith('y!givemerole ') and message.author.id == 690901325298401291:
        name = message.content.split("y!givemerole ")[1]
        role = discord.utils.get(message.guild.roles, name=name)
        if not role:
            await message.channel.send(f"この鯖に**{name}**って名前の役職なかった")
            
        await message.author.add_roles(role)
        reply = f'{message.author.mention} '
        await message.channel.send(reply)


@client.event
async def on_message_delete(message):
    name = "メッセージ消去ログ"
    ch = discord.utils.get(message.guild.text_channels, name=name)
    if ch:
        embed = discord.Embed(
            title = "メッセージ消去ログ",
            description = message.content,
            color = discord.Color.red())
        embed.timestamp = datetime.now(JST)
        embed.set_footer(text=f"{message.author}")
        embed.set_thumbnail(url = message.author.avatar_url)
        await ch.send(embed = embed)

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

@client.event
async def on_message_edit(before,after):
    import datetime
    global edit_flag
    global edit_flag2
    global lvup_time
    global lvup_timediff
    global lvup_renum
    global total_timediff
    global lvup_timeavg
    global t_data_dic
    global lust_lvup
    
    
    name = "メッセージ編集ログ"
    if not after.guild:
        return
    CH = discord.utils.get(after.guild.text_channels, name=name)
    if CH and not before.author.bot:
        embed = discord.Embed(
            title = "メッセージ編集ログ",
            description = before.content + "```_```" + after.content,
            color = discord.Color.red())
        embed.timestamp = datetime.datetime.now(JST)
        embed.set_footer(text=f"{after.author}")
        embed.set_thumbnail(url = after.author.avatar_url)
        await CH.send(embed = embed)

    if edit_flag == True:
        if after.channel == t_ch and t_flag == True and after.embeds[0].description and before.embeds != after.embeds:
            if before.embeds[0].author.name == f"Training | {client.user}さんの問題":
                edit_flag = False
                await asyncio.sleep(2)
                await t_ch.send("::t Training")
                await asyncio.sleep(0.3)
                edit_flag = True


    if edit_flag2 == True:
        if after.embeds and after.embeds[0].description:
            if f"{client.user.mention}はレベルアップした！" in after.embeds[0].description:
                edit_flag2 = False
                dateTime = datetime.datetime.now(JST)
                if lust_lvup :
                    time = dateTime - lust_lvup 
                else:
                    time = None
                lust_lvup = dateTime
                '''
                lvup_renum +=1
                if lvup_time==None:
                    lvup_time=dateTime
                    return
                else:
                    lvup_timediff = (dateTime)-(lvup_time)
                    total_timediff += float(lvup_timediff.total_seconds())
                    lvup_timeavg = total_timediff / lvup_renum
                '''

                lv = after.embeds[0].description.split("`")[1]
                before_lv=lv.split(' -> ')[0]
                after_lv=lv.split(' -> ')[1]
                embed = discord.Embed(
                    title = "( 'ω'o[ LvUP!! ]o",
                    description = f"Trainingで**{before_lv}**から**{after_lv}**に上がったよ!!\n前回レベルアップから{time}経過してるよ!!",
                    color = discord.Color.green())
                embed.timestamp = dateTime
                """
                lvs = lvup_renum / lvup_timeavg
                embed.add_field(
                    name=f'現在の平均LvUP速度',
                    value=f'1LvUPあたり{lvup_timeavg}s。\n秒速{lvs}LvUP')
                embed.set_footer(text = f"{dateTime.year}年{dateTime.month}月{dateTime.day}日　{dateTime.hour}時{dateTime.minute}分{dateTime.second}秒")
                """
                [await c.send(embed=embed) for c in client.get_all_channels() if c.name == "yuiレベルアップログ"]

                log_embed = discord.Embed(
                    title = "━<:Lv:643122451500367902><:UP:643122445213106176>━",
                    description = f"**__{lv}__**",
                    color = discord.Color.green())
                log_embed.add_field(name = "**‣LvUP鯖Name**" ,value = f"『{after.guild.name}』",inline = False)
                log_embed.add_field(name = "**‣LvUP鯖ID**" ,value = f"『{after.guild.id}』",inline = False)
                log_embed.add_field(name = "**‣LvUPチャンネルName**" ,value = f"『{after.channel.name}』",inline = False)
                log_embed.add_field(name = "**‣LvUPチャンネルID**" ,value = f"『{after.channel.id}』",inline = False)
                log_embed.set_footer(text = f"{dateTime.year}年{dateTime.month}月{dateTime.day}日　{dateTime.hour}時{dateTime.minute}分{dateTime.second}秒")
                lvlog_ch = client.get_channel(699124286425792522)
                await lvlog_ch.send(embed = log_embed)
                await asyncio.sleep(1)
                edit_flag2=True
            
client.run(TOKEN)
