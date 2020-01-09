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
import os
import traceback
import math

from discord.ext import tasks

from datetime import datetime, timedelta, timezone


import logging

logging.basicConfig(level=logging.INFO)

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')


client = discord.Client()
TOKEN = os.environ['DISCORD_BOT_TOKEN']
#TOKEN="NjI3MDUyNTc2ODEwMDc0MTEy////.XgTAtg.k6EBPNmQ9XfUJ3nXcBI6-tIlzx8"
dateTime = datetime.now(JST)
server_number = len(client.guilds)


class Talk:
    def __init__(self):
        self.key = 'DZZEsELpflnkZATnwJG6iKcQzxbxZLDz'
        self.api = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'

    def get(self,talking):
        url = self.api
        r = re.post(url,{'apikey':self.key,'query':talking})
        data = json.loads(r.text)
        if data['status'] == 0:
            t = data['results']
            ret = t[0]['reply']
        else:
            ret = '……'
        return ret

talk=Talk()

talk_flag = True
last_resp = None
data_list = []


citycodes = {
    "北海道": '016010', "青森県": '020010',"岩手県": '030010', "宮城県": '040010',
    "秋田県": '050010', "山形県": '060010',"福島県": '070010', "東京都": '130010',
    "神奈川県": '140010', "埼玉県": '110010',"千葉県": '120010', "茨城県": '080010',
    "栃木県": '090010', "群馬県": '100010',"山梨県": '190010', "新潟県": '150010',
    "長野県": '200010', "富山県": '160010',"石川県": '170010', "福井県": '180010',
    "愛知県": '230010', "岐阜県": '200010',"静岡県": '220010', "三重県": '240010',
    "大阪府": '270000', "兵庫県": '280010',"京都府": '260010', "滋賀県": '250010',
    "奈良県": '190010', "和歌山県": '300010',"鳥取県": '310010', "島根県": '320010',
    "岡山県": '330010', "広島県": '340010',"山口県": '350010', "徳島県": '360010',
    "香川県": '370000', "愛媛県": '380010',"高知県": '390010', "福岡県": '400010',
    "大分県": '440010', "長崎県": '420010',"佐賀県": '410010', "熊本県": '430010',
    "宮崎県": '450010', "鹿児島県": '460010',"沖縄県": '471010', "北海": '016010',
    "青森": '020010', "岩手": '030010',"宮城": '040010', "秋田": '050010',
    "山形": '060010', "福島": '070010',"東京": '130010', "神奈川": '140010',
    "埼玉": '110010', "千葉": '120010',"茨城": '080010', "栃木": '090010',
    "群馬": '100010', "山梨": '190010',"新潟": '150010', "長野": '200010',
    "富山": '160010', "石川": '170010',"福井": '180010', "愛知": '230010',
    "岐阜": '200010', "静岡": '220010',"三重": '240010', "大阪": '270000',
    "兵庫": '280010', "京都": '260010',"滋賀": '250010', "奈良": '190010',
    "和歌山": '300010', "鳥取": '310010',"島根": '320010', "岡山": '330010',
    "広島": '340010', "山口": '350010',"徳島": '360010', "香川": '370000',
    "愛媛": '380010', "高知": '390010',"福岡": '400010', "大分": '440010',
    "長崎": '420010', "佐賀": '410010',"熊本": '430010', "宮崎": '450010',
    "鹿児島": '460010', "沖縄": '471010',
}

training_data = {}

client.already_quiz = {}


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
test_ch=1
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



#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
@client.event
async def on_ready():

    global d_ch      #◆世界樹の第一階層チャンネル取得
    d_guild = client.get_guild(654086105699844108)
    d_ch = discord.utils.get(d_guild.text_channels, name=f'第{d_num}階層')

    global d_ch2     #◆黒鉄城のチャンネル取得
    d_ch2= client.get_channel(654710356622704662)

    global ban_guild #◆gban収容所guildの取得
    ban_guild=client.get_guild(654599269906645002)

    global q_ch
    q_ch=client.get_channel(659923091027132416)

    global t_ch
    t_ch=client.get_channel(659923091027132416)
    await t_ch.send('::t')


    for guild in client.guilds:
        tmp = discord.utils.get(guild.text_channels, name="global_yui")

    global t_flag
    t_flag=True

    st_loop.start()
    time_loop.start()

    t_loop.start()
    


    global data_list
    ohanashi_datach = client.get_channel(663952496741580801)
    datas = await ohanashi_datach.history( limit = 10000 ).flatten()
    
    for data in datas:
        data_list.append(data.content)
    

    
    print('◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢\n‣BOT NAME\n '+(client.user.name))
    print('‣BOT ID\n '+str(client.user.id))
    print('‣LOG IN TIME\n '+str(datetime.now(JST)))
    print('◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢')


    dateTime = datetime.now(JST)
    embed = discord.Embed(title="YUI起動ログ", description="起動したよ", color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(
        ('https://yahoo.jp/box/3faN7k', 'https://yahoo.jp/box/c9L236', 'https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="起動時刻", value=f"{dateTime.year}年{dateTime.month}月{dateTime.day}日　{dateTime.hour}時{dateTime.minute}分{dateTime.second}秒", inline=False)
    embed.add_field(name="YUI news", value="多くのシステム系コードを書き直しました。\n不具合等ございましたら```y!report [内容]```で御申し付け下さい", inline=True)
    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui起動ログ'))
    
    user = client.get_user(446610711230152706)
    await user.send(embed=embed)
    
    ready_log_ch = client.get_channel(659922404281417729)
    await ready_log_ch.send(embed=embed)

    await client.change_presence(activity=discord.Game(name="y!help│" + str(len(client.guilds)) + 'の鯖に所属中'))


#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
@tasks.loop(seconds=60)
async def st_loop():
    await client.change_presence(activity=discord.Game(name="y!help│" + str(len(client.guilds)) + 'の鯖に所属中'))

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢
@tasks.loop(seconds=60)
async def t_loop():
    if t_flag==True:

        tao=client.get_user(526620171658330112)
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
                pass

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢


@tasks.loop(seconds=60)
async def d_loop():
    if d_flag==True:
        tao=client.get_user(526620171658330112)
        if tao:
            def test_check (d_msg):
                if d_msg.author != tao:
                    return 0
                if d_msg.channel!=d_ch:
                    return 0
                return 1

            try:
                t_res=await client.wait_for('message',timeout=60,check = test_check)
            except asyncio.TimeoutError:
                await d_ch.send('::attack とまってない?')
            else:
                pass

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢


@tasks.loop(seconds=60)
async def d_loop2():
    if d_flag2==True:
        d_ch2.send('check point')
        tao = client.get_user(526620171658330112)
        def re_check(t_msg):
            if t_msg.author!=tao:
                return 0
            if t_msg.channel!=d_ch2:
                return 0
            return 1
        try:
            await client.wait_for('massage',timeout=30,check=re_check)
        except asyncio.TimeoutError:
            await d_ch2.send('::i f 止まってるんだよなぁ')

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢


@tasks.loop(seconds=60)
async def test_check_loop():
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
                t_res=await client.wait_for('message',timeout=60,check = test_check)
            except asyncio.TimeoutError:
                print('::attack')
                await test_ch.send('::attack とまってない?')
            else:
                pass

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢


#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢


@tasks.loop(seconds=60)
async def time_loop():
    now = datetime.now(JST).strftime('%H:%M')
    if now == '00:00':
        em = discord.Embed(title="24:00の時報をお伝えします\nなんちゃって", description=random.choice((
            '日付変わったから寝ようね！？',
            'まだ起きてるとかみんな狂乱なの？',
            '夜更かしは体に悪いよ……え、私？\nBOTだから支障ZEROですｗｗ',
            'ねろ（辛辣\nさっさと寝ろ',
            '別にいいけどさ……\n夜更かしは体壊さない程度にね',
            'えーと、これ読めばいいの？ \n(台本ﾊﾟﾗﾊﾟﾗ)\nねえこの「お兄ちゃんもう寝ないと！」ってなに？\n殺されたいの？',
            '私だって君が体壊したら悲しまないわけじゃないんだからさ\nちゃんと寝てね？\n私の事BOTだからってなめてるでしょ\nたとえプログラムされたコードで動いてるだけの義骸でも\n私は私なの')),
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
async def on_message(message):

    try:
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
        if not d_ch2 == 2:
            d_num01=d_ch2.name.split('第')[1]
            d_num02=d_num01.split('層')[0]
            d_num2=int(d_num02)
#━━━━❮Trainingコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        me = client.user
        tao = client.get_user(526620171658330112)
        global yui_ans_msg

        if message.content == "y!t":
            await message.channel.send("::t")

        global t_flag
        t_ch = client.get_channel(659923091027132416)
 
        if message.channel == t_ch and message.author == mio:
            if message.embeds:
                if message.embeds[0].footer.text and "TAOのトレーニング" in message.embeds[0].footer.text:
                    if not yui_ans_msg== (message.embeds[0].description).split("`")[1]:
                        yui_ans_msg= (message.embeds[0].description).split("`")[1]
                        await t_ch.send(yui_ans_msg)

        if message.content=='y!tstart':
            t_flag=True
            embed = discord.Embed(
            title=f"トレーニング開始\nt_flag = {t_flag}"
            )
            await message.author.send(embed = embed)
        if message.content=='y!tstop' :
            t_flag=False                   
            embed = discord.Embed(
            title=f"トレーニング終了\nt_flag = {t_flag}"
            )
            await message.author.send(embed = embed)


        
        
#━━━━❮YUIpingコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content=='y!ping':
       
            embed=discord.Embed(title='**Ping測定中**')
            msg=await message.channel.send(embed=embed)
            
            result=(msg.created_at - message.created_at).microseconds // 1000
            await msg.edit(embed=discord.Embed(title=f'**Pong!\n{result}ms**'))
        help_ch = 659922476641288211

#━━━━❮YUIhelpコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content == "y!help":
            log_ch = client.get_channel(659922476641288211)
            author_id=str(message.author.id)

            help_embed_one = discord.Embed(title="YUIヘルプ目次",
                                           description='```‣ヘルプ目次　　│P.1\n‣ＴＡＯコマンド│P.2\n‣メイン機能　　│P.3\n‣特殊チャンネル│P.4\n‣ガチャ　　　　│P.5\n‣その他娯楽　　│P.6\n‣ユイ関連ＵＲＬ│P.7```',
                                           color=discord.Colour.green())
            help_embed_one.set_thumbnail(url=random.choice(
                ('https://yahoo.jp/box/3faN7k', 'https://yahoo.jp/box/c9L236', 'https://yahoo.jp/box/Jxj1Jd')))
            help_embed_one.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.1/7")

            help_logch = client.get_channel(id=help_ch)

            help_embed_0 = discord.Embed(title="⚠️YUI注意事項一覧⚠️",
                                         description='🔷**[]は不要です**\n```y![example]→y!example```\n🔷**スペースの有無を確認して下さい**\n```y!example []→有り\ny!example[]→無し```\n🔷**管理者権限必須です**```YUIに管理者権限が無いと無能BOTと化します。```\n🔷**技術的不具合**```。Helpがこのページから進まない場合はYUIを招待し直してください。\n```[ここから招待可能です](https://discordapp.com/api/oauth2/authorize?client_id=627052576810074112&permissions=8&scope=bot)\n上記全てに同意の場合は☑️を\n同意しないという場合は❎を押してください。\n不具合等は`y!report 内容`でお知らせください',
                                         color=discord.Colour.green())

            help_embed = discord.Embed(title="TAOコマンド系ヘルプ", description="TAOで使うコマンドを使うヘルプだよ", color=discord.Colour.green())
            help_embed.add_field(
                name='y!login', value='```ログインする```', inline=True)
            help_embed.add_field(
                name='y!st', value='```::st```', inline=True)
            help_embed.add_field(
                name='y!role [役職番号]', value='```::role\n役職番号はroleのリアクション番号だよ\n例\ny!role 0はAdventureだよ```', inline=True)
            help_embed.add_field(
                name='y!i', value='```::item```', inline=True)
            help_embed.add_field(
                name='y!i [f,e]', value='```::i [f,e]```', inline=True)
            help_embed.add_field(
                name='y!re',value='```::re```', inline=True)
            help_embed.add_field(
                name='y!atk',value='```~~::atk~~```互換性のある機能を開発+実験中のため\n現在停止中です', inline=True)
            help_embed.add_field(
                name='y!nekoshima', value='`超激レア枠が出るまでTAOさなきゃいけない\nモンスターの数を占う`', inline=False)
            help_embed.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.2/7")

            help_two_embed = discord.Embed(title="メイン機能ヘルプ"
                                           , description="その多機能"
                                           , color=discord.Colour.green())
            help_two_embed.add_field(name='y!dice [下限] [上限]'
                                     , value='```下限~上限の数の間でサイコロをふる```' , inline=False)
            help_two_embed.add_field(name='y!sinfo'
                                     , value='```サーバーの情報を開示```', inline=False)
            help_two_embed.add_field(name='y!mkch [チャンネル名]'
                                     , value='```コマンドを使用したカテゴリ内にチャンネルを作成```' , inline=False)
            help_two_embed.add_field(name='y!kuji'
                                     , value='```おみくじ```', inline=False)
            help_two_embed.add_field(name='y!myicon'
                                     , value='```コマンド使用者のアイコン表示```' , inline=False)
            help_two_embed.add_field(name='y!poll [タイトル] [内容] '
                                     , value='```👍👎リアクションつきembedメッセージ送信```開発者のデータ管理が甘いせいで大爆発が起きたため現在復旧中です', inline=False)
            help_two_embed.add_field(name='y!say',
                                     value='```y!say1 [内容]│オウム返し\ny!say2 "[タイトル]" "[内容]"│embed形式送信\ny!say3 [題名] [内容]│embed+送信者メンション+時刻```開発者のデータ管理が甘いせいで大爆発起きたため\ny!say3コマンドは停止中です',inline=False)
            help_two_embed.add_field(name='y!clean [数]'
                                     , value='```鯖管理者権限持ちで使用可、指定数のメッセージ消去```', inline=False)
            help_two_embed.add_field(name='y!gban [対象のUSERのID'
                                     , value='```USERをGlobalBANするよ```', inline=False)
            help_two_embed.add_field(name='y!report [内容]'
                                     , value='```開発者へのレポート＆リクエスト```', inline=False)
            help_two_embed.add_field(name='y!ping'
                                     , value='```Ping値測定```', inline=False)

            help_two_embed.add_field(name='y!wt [都道府県名]', value='```今日、明日の天気予報「YUI WEATHER」```', inline=True)
            help_two_embed.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.3/7")

            embed_special = discord.Embed(
                title='特殊チャンネル系',
                description='```‣チャンネル内容│チャンネル名\nチャンネル作成コマンド```', color=discord.Colour.green())
            embed_special.add_field(name='‣グローバルチャット│global_yui'
                                    , value='```y!yui global```', inline=False)
            embed_special.add_field(name='‣YUIの起動ログ│yui起動ログ'
                                    , value='```y!yui log```', inline=False)
            embed_special.add_field(name='‣日付変更ログ│yui時報ログ'
                                    , value='```y!yui timelog```')
            embed_special.add_field(name='‣YUIレベルアップログ│yuiレベルアップログ'
                                    , value='```y!lv```',inline=False)
                                    
            embed_special.add_field(name='‣TAOモンスター出現ログ│tao出現ログ:'
                                    , value='```y!tao 1│通常モンスター用のチャンネル\ny!tao 1.5│強敵モンスター用のチャンネル\ny!tao 5│経験値倍率５倍モンスター用のチャンネル\ny!tao 33│経験値倍率33倍モンスター用のチャンネル\ny!tao 100│経験値倍率100倍モンスター用のチャンネル\n```', inline=False)
            embed_special.add_field(name='‣YUIの起動ログ│yui起動ログ'
                                    , value='```y!yui log```', inline=False)
            embed_special.add_field(name='‣日付変更ログ│yui時報ログ'
                                    , value='```y!yui timelog```')
            embed_special.add_field(name='‣YUIレベルアップログ│yuiレベルアップログ'
                                    , value='```y!lv```',inline=False)
            embed_special.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.4/7")

            gacha = discord.Embed(title="ガチャ機能だよ🎯 "
                                  , description="コマンドはy!gacha [ガチャ番号]"
                                  , color=discord.Colour.green(), inline=False)
            gacha.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
            gacha.add_field(name="ガチャ種類＋番号一覧",
                            value="‣__**通常ガチャ**　番号：1__\n色々よくわからないものが出てくるよ。\nたまに隠しコマンドが出てくるとかなんとか\ny!gacha 1\n\n‣__**おにゃのこガチャ**　番号：2__\n可愛いおにゃのこの画像がいっぱいだよ\n可愛いの純度１００％！\ny!gacha 2")
            gacha.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.5/7")

            slot_embed = discord.Embed(title="その他娯楽だよ",description='随時開発中!', color=discord.Colour.green())
            slot_embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/635993816297504809/642579874816720916/money_slot_machine.png")
            slot_embed.add_field(name="**y!slot**",
                                 value="```絵文字を利用したスロットだよ```")
            slot_embed.add_field(name="**y!fsg**",
                                 value="```絵文字を利用した釣りだよ```")
 
            slot_embed.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.6/7")

            url_embed = discord.Embed(title='YUI関連URL\n')
            url_embed.add_field(name='‣**Re:YUI ver1.12.2 招待URL**',
                                value='[URLはこちら](https://discordapp.com/api/oauth2/authorize?client_id=627052576810074112&permissions=8&scope=bot)')
            url_embed.add_field(name='‣**YUI Official Server 招待URL**', value='[URLはこちら](https://discord.gg/tJaJBDD)')
            url_embed.add_field(name='‣**YUIサポートBot Mio 招待URL**',
                                value='[URLはこちら](https://discordapp.com/oauth2/authorize?client_id=644153226597498890&permissions=8&scope=bot)')
            url_embed.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}\nP.7/7")

            page_count = 0  # ヘルプの現在表示しているページ数
            page_content_list = [
                help_embed_0,
                help_embed_one,
                help_embed,
                help_two_embed,
                embed_special,
                gacha,
                slot_embed,
                url_embed]  # ヘルプの各ページ内容

            send_message = await message.channel.send(embed=page_content_list[0])  # 最初のページ投稿
            await send_message.add_reaction("❎")
            await send_message.add_reaction("☑️")

            def help_react_check(reaction, user):

                if reaction.message.id != send_message.id:
                    return 0
                if reaction.emoji in ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '⬅️', '➡️', '🚮', '☑️', '❎', '⏭️', '⏮️']:
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
                    if reaction.emoji in ["1️⃣", "⏮️"] and page_count > 0:
                        page_count = 1
                    if reaction.emoji == "2️⃣" and page_count > 0:
                        page_count = 2
                    if reaction.emoji == "3️⃣" and page_count > 0:
                        page_count = 3
                    if reaction.emoji == "4️⃣" and page_count > 0:
                        page_count = 4
                    if reaction.emoji == "5️⃣" and page_count > 0:
                        page_count = 5
                    if reaction.emoji == "6️⃣" and page_count > 0:
                        page_count = 6
                    if reaction.emoji in ['7️⃣', '⏭️'] and page_count > 0:
                        page_count = 7
                    if reaction.emoji in ['🚮', '❎']:
                        await send_message.delete()

                    await send_message.clear_reactions()
                    await send_message.edit(embed=page_content_list[page_count])
                    reactions0 = ["⏮️","⬅️","🗑","➡️","⏭️"]
                    reactions1 = ["⏮️","⬅️","🗑"]
                    reactions2 = [":ballot_box_with_check:","❎"]
                    reactions3 = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","⬅️","🚮"]
                    if page_count == 0:
                        for reaction in reactions2:
                            await send_message.add_reaction(reaction)
                    elif page_count == 1:
                        for reaction in reactions3:
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
            embed.set_footer(icon_url=message.author.avatar_url, text=f"認証中│{message.author.name}\n━━━━━━━━━━━")
            test_send = await message.channel.send(embed=embed)
            if message.author.id == 446610711230152706:
                await asyncio.sleep(5)
                await test_send.edit(embed=discord.Embed(title=f"**Received command!!**",
                                                         description=f'**checking user ID** ☑️\n━━━━━━━━━━━\nWould you realy need reboot {client.user.mention}?'))
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
                        await message.channel.send(embed=discord.Embed(title='Start Reboot!!'))
                        await client.logout()
                        await sys.exit()
            else:
                embed = discord.Embed(title='権限がありません!!', description='これは開発者専用コマンドです')
                await message.channel.send(embed=embed)

#━━━━❮Cleanコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith ('y!clean '):
            log_ch = client.get_channel(659965493096087552)
            clean_num = message.content.split("y!clean ")[1]
            if message.author.guild_permissions.administrator:

                await message.channel.purge(limit=int(clean_num))
                embed = discord.Embed(title = "メッセージ消去完了！",
                description=f"{clean_num}のメッセージを消去したよ",
                color = discord.Color.green())
                embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/635993816297504809/652423808086573096/57_20191206171856.png")
                embed.set_footer(icon_url=message.author.avatar_url, text=f"コマンド使用者│{message.author}")
                await message.channel.send(embed=embed)
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


#━━━━❮開発者専用強制Banコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith('y!ban ') and message.author.id == (446610711230152706):
            userid = message.content.split('y!ban ')[1]
            embed = discord.Embed(title=f'開発者権限により、急遽対象のIDのuserをBan致します\nID:{userid}')
            await message.channel.send(embed=embed)
            member = message.guild.get_member(int(userid))
            await member.ban()
            embed = discord.Embed(title='対象のIDのuserをBan完了')
            await message.channel.send(embed=embed)

#━━━━❮Gban+Gunbanコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith('y!gban '):
            gban_id=message.content.split(' ')[1]
            dateTime = datetime.now()
            ban_guild=client.get_guild(654599269906645002)
            banch=discord.utils.get(ban_guild.text_channels,name=f'{gban_id}')
            ban_user=client.get_user(int(gban_id))
            if ban_user is not None:
                if not banch:
                    ban_ch=await ban_guild.create_text_channel(name=f'{gban_id}')
                    e_embed=discord.Embed(title=f'Global Ban User Data',
                                description=f'{ban_user}\n{gban_id}\nBan実行者{message.author}',
                                color=discord.Color.red())
                    e_embed.set_footer(text = datetime.now(JST))
                    await ban_ch.send(embed=e_embed)
                    embed=discord.Embed(title='Global Banned!!',
                                description=f'{ban_user}はGlobalBANされたよ\n以降私がいる鯖でこいつが入ってきたら責任もってBANするね!',color=discord.Color.red())
                    embed.set_footer(icon_url=message.author.avatar_url,text=f'実行者┃{message.author}')
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send('登録済みだ!帰れ!\n※開発者はこのコマンド開発当時非常にイラついていたのでご了承ください')
            else:
                await message.channel.send(f'んな奴いねえよ! まあでも{gban_id}ってIDの奴はまだ見ぬplayerとして登録しといてやんよ\n※開発者はこのコマンドの開発当時非常にイラついていたのでご了承ください')
                await ban_guild.create_text_channel(name=f'{gban_id}')

        if message.content.startswith('y!gunban '):
            bancheck=discord.utils.get(ban_guild.text_channels,name=f'{message.author.id}')
            if bancheck == None:
                unban_id=message.content.split('y!gunban ')[1]
                ban_guild=client.get_guild(654599269906645002)
                ch = discord.utils.get(ban_guild.text_channels,name=f'{unban_id}')
                await ch.delete()
                ban_user=client.get_user(int(unban_id))
                embed=discord.Embed(
                title='Global UnBanned!!',
                description=f'{ban_user}はUnGlobalBANされたよ!',color=discord.Color.green())
                embed.set_footer(icon_url=message.author.avatar_url,text=f'実行者┃{message.author}')
                await message.channel.send(embed=embed)
            else:
                embed = discord>embed(
                title = f"{message.author.name}貴様はGBanされている！\n貴様にUnBan権限はない！"
                )
                await message.channel.send(embed = embed)



#━━━━❮第二ダンジョンコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content=='y!devac2':
            d_flag2=False
            d_loop2.stop()
            await asyncio.sleep(1)
            await d_ch2.send('::re')
            embed=discord.Embed(title='ダンジョンから離脱')
            await message.author.send(embed=embed)
        if message.content=='y!dcap2':
              
            d_loop2.start()
            d_flag2=True
            await asyncio.sleep(1)
            embed=discord.Embed(title='ダンジョン攻略開始')
            await message.author.send(embed=embed)
            await d_ch2.send('::i f 攻略開始')


        if d_flag2 == True and message.channel == d_ch2 and message.embeds:
            if message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:
                if 'ネコ' in message.embeds[0].title and '超激レア' in message.embeds[0].title:
                    await d_ch2.send('::re')
                else:
                    lv1=message.embeds[0].title.split('Lv.')[1]
                    lv2=lv1.split(' ')[0]
                    lv3=(math.floor(int(lv2)/100))
                    if d_num2<lv3:
                        d_num2=lv3
                        await d_ch2.edit(name=f'第{lv3}層')
                    await asyncio.sleep(1)
                    await d_ch2.send("::i f 先手必勝!!")


        if message.channel==d_ch2 and d_flag2==True:
            if "フレア" in message.content and 'のHP' in message.content:

                await asyncio.sleep(0.1)
                await d_ch2.send('::i f')

#━━━━❮第一ダンジョンコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content=='y!devac':
            d_flag=False
            d_loop.stop()
            await asyncio.sleep(1)
            await d_ch.send('::re')
            embed=discord.Embed(title='ダンジョンから離脱')
            await message.author.send(embed=embed)

        if message.content=='y!dcap':
            d_flag=True
            d_loop.start()
            await asyncio.sleep(1)
            d_num=1
            d_ch = discord.utils.get(client.get_guild(654086105699844108).text_channels, name=f'第{d_num}階層')

            embed=discord.Embed(title='ダンジョン攻略開始')
            await message.author.send(embed=embed)
            await d_ch.send('::attack 攻略開始')

        if message.channel == d_ch :
            if f"{client.user.display_name}はやられてしまった" in message.content and message.author == tao:
                d_flag = False
                await asyncio.sleep(5)
                d_num += 1
                d_ch = discord.utils.get(client.get_guild(654086105699844108).text_channels, name=f'第{d_num}階層')
                if d_ch:

                    await asyncio.sleep(3)
                    b_num=d_num-1
                    b_ch = discord.utils.get(client.get_guild(654086105699844108).text_channels, name=f'第{b_num}階層')
                    await b_ch.send('::re')
                    await asyncio.sleep(5)
                    d_flag=True
                    await d_ch.send('::attack')
                else:

                    d_ch=await client.get_guild(654086105699844108).create_text_channel(name=f"第{d_num}階層")
                    await asyncio.sleep(3)
                    b_num=d_num-1
                    b_ch = discord.utils.get(client.get_guild(654086105699844108).text_channels, name=f'第{b_num}階層')
                    await b_ch.send('::re')
                    await asyncio.sleep(5)
                    d_flag=True
                    await d_ch.send("::attack")

        if d_flag == True and message.channel == d_ch and message.embeds:
            if message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:
                await asyncio.sleep(0.5)
                await d_ch.send("::attack 先手必勝!!")

        if message.channel==d_ch and d_flag==True:
            if f"{client.user.display_name}の攻撃" in message.content and "のHP" in message.content:
                await asyncio.sleep(0.5)
                await message.channel.send('::attack')
                #⬆PETいないからこれしてるけどいつか消す⬆

                def d_check (d_msg):
                    if d_msg.author != tao:
                        return 0
                    if d_msg.channel!=d_ch:
                        return 0
                    return 1
                
                try:
                    t_res=await client.wait_for('message',timeout=3,check = d_check)
                except asyncio.TimeoutError:

                    await d_ch.send('::attack pet攻撃なし')
                else:
                    print('pet')
                    if ']の攻撃' in t_res.content and 'のHP' in t_res.content:
                        await d_ch.send(f'::attack ')
                
#━━━━❮Testchコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        global test_ch
        global test_flag
        if message.content.startswith("y!testch "):
            test_check_loop.start()
            test_ch_m = message.content.split('y!testch ')[1]
            test_ch = discord.utils.get(message.guild.text_channels, mention=test_ch_m)
            await asyncio.sleep(1)
            test_flag=True
            await test_ch.send("::attack")

            log_ch = client.get_channel(659923606595174441)
            embed=discord.Embed(
            title=f"( 'ω'o[**testch**]oログ♡",
            description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{message.author.id}』\n使用ch名│『{message.channel.name}』\n指定ch名│『{test_ch.name}』```')
            embed.set_thumbnail(url=message.author.avatar_url)
            await log_ch.send(embed=embed)
            embed=discord.Embed(title='Test Play開始')
            await message.author.send(embed=embed)


        if message.content=='y!teststop':
            test_flag=False
            test_check_loop.stop()
            await asyncio.sleep(1)
            await test_ch.send('::re')
            embed=discord.Embed(title='Test Play停止')
            await message.author.send(embed=embed)

        if message.channel == test_ch and message.embeds and test_flag==True:
            if message.embeds[0].title and 'が待ち構えている' in message.embeds[0].title:
                if test_ch.id==659917177599819809:

                    lv=message.embeds[0].title.split('Lv.')[1].split(' ')[0]
                    type=message.embeds[0].title.split('[')[1].split(']')[0]
                    rank=message.embeds[0].title.split('【')[1].split('】')[0]
                    name=message.embeds[0].title.split('】')[1].split('が待ち構えている')[0]
                    image_url=message.embeds[0].image.url
                    hp=message.embeds[0].title.split(':')[3]

                    logch=client.get_channel(659965763050012703)
                    await test_ch.edit(name=f'┃honpen┃lv.{lv}')
                    exp=int(lv)
                    if rank=='超強敵' or rank=='レア':
                        exp=int(lv)*5
                    elif rank=='激レア':

                        exp=int(lv)*33
                    elif rank=='強敵':
                        exp=int(lv)*1.6
                    elif rank=='超激レア':
                        exp=int(lv)*100
                    embed=discord.Embed(title=f'モンスター出現ログ\nName:{name}\nType Rank:\n{type}┃{rank}\nStatus:\nLv.{lv}┃HP.{hp}\nExp:\n{exp}',color=discord.Color.green())
                    embed.set_thumbnail(url=image_url)
                    embed.set_footer(text = datetime.now(JST))
                    await logch.send(embed=embed)
                await asyncio.sleep(1)
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
                    re_msg=await client.wait_for('message',timeout=5,check=mio_check)
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
                    await asyncio.sleep(0.5)
                    await test_ch.send('::attack 復活乁( ˙ ω˙乁)')

                elif f"{client.user.mention}はもうやられている！" in message.embeds[0].description:
                    await asyncio.sleep(0.5)
                    await test_ch.send("::i e 復活！")

#━━━━❮おーとFBコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content.startswith("y!ifch "):
            atk_ch_m = message.content.split('y!ifch ')[1]
            atk_ch2 = discord.utils.get(message.guild.text_channels, mention=atk_ch_m)
            log_ch = client.get_channel(659923593693495337)
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


#━━━━❮元atkchコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#




#━━━━❮YuiLvUPログコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        
        if message.embeds and message.embeds[0].description and message.author == tao :
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
                lvlog_ch = client.get_channel(660817503597101099)
                await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == "yuiレベルアップログ"))
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
            report_ch = client.get_channel(659966462273912833)
            reply = message.content.split('y!report ')[1]
            embed = discord.Embed(title='レポート内容\n' + (reply), description=f"発言者{message.author.mention}", color=0x2ECC69)
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
            await message.channel.send('::status window　私のステータスが見たいなんて、君もエッチだな')
            log_ch=client.get_channel(659924491115298816)
            embed=discord.Embed(
            title=f"( 'ω'o[**status window**]oログ♡",
            description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{message.author.id}』\n使用ch名│『{message.channel.name}』```')
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text = datetime.now(JST))
            await log_ch.send(embed=embed)


        # 「りせ」と発言したら「::re」が返る処理
        if message.content == 'y!re':
            await message.channel.send('::reset')

        if message.content == 'y!atk':
            await message.channel.send("::attack")
            await message.channel.send(embed=embed)
            log_ch=client.get_channel(659922557188702229)
            embed=discord.Embed(title=f"( 'ω'o[**attack**]oログ♡",description=f'```使用鯖　│『{message.guild.name}』\n使用者　│『{message.author}』\n使用者ID│『{message.author.id}』\n使用ch名│『{message.channel.name}』```')
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_footer(text = datetime.now(JST))
            await log_ch.send(embed=embed)

        if message.content == 'y!i e':
            await message.channel.send('::i e')

        if message.content == 'y!i i':
            await message.channel.send('::i i \nまあこれもuser指定するのめんどくて作ってないから意味ないけどね')

        if message.content == 'y!i f' and message.author_id!=446610711230152706:
            await message.channel.send('::i f')
            log_ch=client.get_channel(659922630861783060)
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
                embed = discord.Embed(title='番号エラー!',
                                  description=f'{role_num}に該当する役職はないよ!\n**役職番号**\n0│Adventure系\n1│Warrior系\n2│Mage系\n3│Thief系\nコマンドは`y!role [役職番号]`だよ。',
                                  color=discord.Color.red())
                embed.set_footer(icon_url={message.author.avater_url},text=f"{message.author.name}")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('::role')

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
                    if role_num == '0':
                        await ans_msg.add_reaction(f'\u0030\u20e3')
                    elif role_num == '1':
                        await ans_msg.add_reaction(f'\u0031\u20e3')
                    elif role_num == '2':
                        await ans_msg.add_reaction(f'\u0032\u20e3')
                    elif role_num == '3':
                        await ans_msg.add_reaction(f'\u0033\u20e3')

        if message.content == 'y!i':
            await message.channel.send('::i')

        if message.content == 'y!login':
            await message.channel.send('::login')

#━━━━❮TAO出現ログ役職コード(になる予定)❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content == 'y!join':
            role = discord.utils.get(message.guild.roles, name='裏寄生隊')  # YUI通知
            await message.author.add_roles(role)
            reply = f'{message.author.mention} これで隊員の一人ね'
            await message.channel.send(reply)

        if message.content == 'y!announce':
            role = discord.utils.get(message.guild.roles, name='YUI通知')  # YUI通知
            await message.author.add_roles(role)
            reply = f'{message.author.mention} 何か更新あったら呼ぶね'
            await message.channel.send(reply)

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
                await message.channel.send('お、大吉!!\nいいねいいね!!')

            elif num_random == 2:
                embed.set_image(url=url2)
                await message.channel.send(embed=embed)
                await message.channel.send('ん、小吉\nまあ凶とかよりはね…?')

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
                                               "https://media.discordapp.net/attachments/635993816297504809/636080191499927552/20_20191022145257.png")))
            embed.add_field(name=random.choice(('最高に需要無いんだけど……', 'うわ何これ……いる？', '……こんなのガチャガチャから出てこないよね普通',
                                                'ごめんちょっと意味わからないんだけどナニコレ', "これもらって喜ぶ人いるのかな", '………ノーコメント','なんて言えばいいんだろう','なんでこれをガチャガチャに入れたし…')),
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
            name=random.choice( ('いや可愛いけどコメントに困る', 'あ、かわいい', 'ちょくちょくエッチなのは入ってるよねこれ（）', '可愛いというより萌えのほうが正しいのかなこれ', "普通にかわいいこれ", 'あー悪くないかも')),
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
'🐱濡れたネコ':'ヌコw',
'🚽便座':'トイレ!?!?!',
}
            result_key=random.choice(list(emono_dect.keys()))
            result=emono_dect[result_key]
            embed=discord.Embed(title=f'**-YUIの釣り!-**\nお?　{result_key}が釣れたね!\n{result}',color=discord.Color.blue())
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/635993816297504809/659805550443233290/58_20191227021126.png')
         
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

        if message.content.startswith("y!dice "):  # ここの!diceは好きなのにしていいぞ
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
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name=reply_one)
            reply = f'{new_channel.mention} を作成したよ!'

            await message.channel.send(reply)

#━━━━❮無駄隠しコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if message.content == "y!timer":
            await message.delete()
            tmp = await message.channel.send("10")  # 編集するメッセージを保持
            await asyncio.sleep(1)
            await tmp.edit(content="9")
            await asyncio.sleep(1)
            await tmp.edit(content="8")
            await asyncio.sleep(1)
            await tmp.edit(content="7")
            await asyncio.sleep(1)
            await tmp.edit(content="6")
            await asyncio.sleep(1)
            await tmp.edit(content="5")
            await asyncio.sleep(1)
            await tmp.edit(content="4")
            await asyncio.sleep(1)
            await tmp.edit(content="3")
            await asyncio.sleep(1)
            await tmp.edit(content="2")
            await asyncio.sleep(1)
            await tmp.edit(content="1")
            await asyncio.sleep(1)
            await tmp.edit(content="0")

        if message.content == "y!gorogoro":
            await message.delete()
            tmp = await message.channel.send("(:3\_ヽ)_......")  # 編集するメッセージを保持
            await asyncio.sleep(1)
            await tmp.edit(content="(:3\_ヽ)_......ねむいい......")
            await asyncio.sleep(1)
            await tmp.edit(content=".　( ε: )")
            await asyncio.sleep(1)
            await tmp.edit(content=".　　　(.ω.)")
            await asyncio.sleep(1)
            await tmp.edit(content=".　　　　　( :3 )")
            await asyncio.sleep(1)
            await tmp.edit(content=".　　　　  　('ω')")
            await asyncio.sleep(1)
            await tmp.edit(content=".　　　　 　　　(:3\_ヽ)_....")
            await asyncio.sleep(3)
            await tmp.edit(content=".　　　　　　　　 　(:3\_ヽ)_....なにがしたかったんだろ")

        if message.content == "y!amanohashi":
            await message.delete()
            await message.channel.send("私の生みの親だね。まあどうでもいいけどね！")


        if message.content.startswith('y!send '):
            await message.delete()
            x = message.content.split(" ", 2)
            riptext2 = int(x[2])
            channel = client.get_channel(riptext2)
            riptext = x[1]

            await channel.send(riptext)


#━━━━❮グローバルチャットコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#

        if (len(message.embeds) == 0) and (message.channel.name == "global_yui") and (not "discord.gg" in message.author.name):
            content = re.sub(r"(https://discord.gg/)([\w]*)", r"||\1\2||", message.content)
            embed = discord.Embed(title=f'送信者│{message.author}', description=f"{content}",
                                  color=discord.Color(random.randint(0, 0xFFFFFF)))
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_author(icon_url=message.guild.icon_url, name=f"{message.guild.name}")
            embed.set_footer(icon_url=message.author.avatar_url,text = datetime.now(JST))
            await message.delete()
            for guild in client.guilds:
                for channel in guild.channels:
                    if channel.name == "global_yui":
                        await channel.send(embed=embed)

#━━━━❮オートレスポンスコード❯━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━#
        global data_list
        if not str(message.channel.id) in data_list and 'おつ' in message.content or '乙' in message.content or 'ｵﾂ' in message.content or 'オツ' in message.content:
            if message.author.bot:
                pass

            else:
                channel = message.channel
                oha = random.choice(('(\*´ω｀*)ｵﾂｶﾚｻﾏー', '‪(꜆꜄꜆˙꒳˙)꜆꜄꜆ ｵﾂｵﾂｵﾂ‬', '( 厂˙ω˙ )厂うぇーい', 'おつかれさまぁ～  (\*ˊ˘ˋ*)♪',
                                     'おつおつ( ´꒳`)', 'おつ(　ˆᴘˆ　)'))

                await channel.send(oha)

        if not str(message.channel.id) in data_list and 'オハ' in message.content or 'ｵﾊ' in message.content or 'oha' in message.content or 'おは' in message.content:
            
            if message.author.bot:

                return

            else:
                now = datetime.now(JST)
                if now.hour > 12:
                    await message.channel.send("……もう朝は終わったよ……？")
                else:
                    channel = message.channel
                    oha = random.choice(('おはー(((o(\*ﾟ▽ﾟ*)o)))', '(ฅ・ω・ฅ)おはよう♪', '⸜(\* ॑꒳ ॑*  )⸝⋆*オハ', 'おは(　ˆᴘˆ　)'))

                    await channel.send(oha)

        if not str(message.channel.id) in data_list and 'おやす' in message.content or 'スヤァ' in message.content or 'oyas' in message.content or 'ｽﾔｧ' in message.content or 'ねる' in message.content or '寝る' in message.content :
            if message.author.bot:

                return

            else:
                now = datetime.now(JST)
                if now.hour > 6 and now.hour < 17:
                    await message.channel.send("今から寝るの！？")
                else:
                    channel = message.channel
                    oha = random.choice(('( ˘ω˘ ) ｽﾔｧ…', '( ˘꒳​˘ )ｵﾔｽﾔｧ…', '_([▓▓] ˘ω˘ )_ｽﾔｧ…',
                                         '=͟͟͞( ˘ω˘)˘ω˘)˘ω˘)ｼﾞｪｯﾄｽﾄﾘｰﾑｽﾔｧ…', 'ｽﾔｧ…(　ˆᴘˆ　)'))



        if client.user != message.author and not str(message.channel.id) in data_list:
            kakuritu = random.randint(1, 1000)
            if int(kakuritu) in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
                Z = ['あんぱん', 'メロンパン', 'フランスパン', 'チョコパイ']
                A = random.choice(Z)
                AZ = ['チョコ', '粒あん', 'バター', 'しゃけ', 'ケチャップ']
                B = random.choice(AZ)
                C = ["知り合い", "友達", "マックで見かけた人", "モスで見かけた人", "たまたま電車で乗り合わせた人"]
                CC = random.choice(C)
                random_dana = ['お腹すいたなぁ…', 'ねえ\nだいぶ前に' + (CC) + 'がやってたんだけど…' + (A) + 'って' + (B) + 'とあうの?',
                               '**プリン**に**醤油**をかけると**うにの味**って言うけど\nこれ式で表すと\n__**プリン味＋醤油味=うに味**__\nだよね\nじゃあさ、この式から\n__**うに味－醤油味=プリン味**__\nってことになるよね。\nつまりうにから醤油系の味成分を抽出しまくればいつかプリン味になるのかな!....?',
                               'フランスにはtaoという名前のペットボトル飲料がある', '( 厂˙ω˙ )厂うぇーい',
                               '''＿人人人人人人人人＿\n＞ 突　然　の　死 ＜\n￣^Y^Y^Y^Y^Y^Y^Y￣''', '(((((((((((っ･ω･)っ ｳｪｰｲ♪', '| ε:)   にゅ',
                               '(^ω^≡^ω^).', '( ˙꒳​˙  )ﾌｧｯ', '|ω・)ﾐﾃﾏｽﾖ', '(  ﾟཫ ﾟ)ｺﾞﾌｯ',"タンスの角ってなんであんなに小指を殺しに来てるんだろうね","アマノがこの前「お花を摘みに行ってくる」を男性verで言おうとして「畑を耕してきます」って言ってた（）"]
                text_random = random.choice(random_dana)
                await message.channel.send(text_random)
            if int(kakuritu) == 5 and message.author != client.user:
                embed = discord.Embed(
title="不適切な発言をキャッチ",
description=f"**{message.author}**さんの\n```{message.content}```という発言は\n他のUserに不快感を与える恐れがあるため\n**{message.author}**さんを一時的に強制BAN致します。\n予定解除時刻は７時間後です。",color = discord.Color.red())
                embed.set_footer(icon_url = client.user.avatar_url,text="チャンネル内治安維持システム")
                await message.channel.send(embed=embed)
                await asyncio.sleep(5)
                await message.channel.send("嘘です★")
                
        

        if client.user != message.author and not message.author.bot :
        
            if 'だよ' in message.content:
                aaa = ["そうなの？", "そうだよ(便乗)"]
                AAA = random.choice(aaa)
                await message.channel.send(AAA)
            if 'した' in message.content:
                await message.channel.send('そうなんだ...(困惑)')
            if 'なの' in message.content and '？' in message.content:
                await message.channel.send('そうだよ(便乗)')

            if 'くえー' in message.content:
                y1 = ['……結構恥ずかしいからねこれ', '…ごめん自分で反応しといてあれだけど、結構恥ずい', '……はずいわ!', '\nいやぁぁこれ言うの恥ずかしいからいやぁぁぁ',
                      '……それ言われたら反応しないといけないからやめて', '\nなんでこんな恥ずいのに私が反応しなきゃ行けないの…']
                y2 = random.choice(y1)
                await message.channel.send('く、くえー…' + (y2))

            if 'ねこ' in message.content:
                y1 = ['ねこですよろしくおねがいします', 'ねこはいましたよろしくおねがいします', 'ねこはいます', 'ねこはいました', 'ねこはどこにでもいます', 'ねこはここにいます']
                y2 = random.choice(y1)
                await message.channel.send((y2))

            if client.user != message.author:
                if 'せやな' in message.content:
                    y1 = ['そやな']
                    y2 = random.choice(y1)
                    await message.channel.send((y2))

            if client.user != message.author:
                if 'うぃ' in message.content or 'うぇ' in message.content:
                    y1 = ['( 厂˙ω˙ )厂うえーい']
                    y2 = random.choice(y1)
                    await message.channel.send((y2))
            if client.user != message.author:
                if 'くさ' in message.content or '草' in message.content:
                    y1 = ['w', 'www', '草', '𐤔𐤔𐤔', 'ʬ﻿ʬʬ﻿', '෴෴']
                    y2 = random.choice(y1)  # (　＾ω＾)おっおっおっ
                    await message.channel.send((y2))
                if 'おっ' in message.content:
                    y1 = ['(　＾ω＾)おっおっおっ', '( ˙꒳​˙    ≡   ˙꒳​˙  )おっおっおっ', '(　＾ω＾)ｵｯw']
                    y2 = random.choice(y1)
                    await message.channel.send((y2))

                if 'ぽ' in message.content or 'ポ' in message.content:
                    y1 = ['㌼㌨㌥㌑㌝㌈㌏㌐　㌞㌞㌞㌞㌑㌆']
                    y2 = random.choice(y1)
                    await message.channel.send((y2))

                if message.content == client.user.mention:  # 話しかけられたかの判定
                    embed = discord.Embed(title='YUI Information', description=f'{client.user}\nID 627052576810074112')
                    embed.set_author(name=client.user,
                                     url="https://discordapp.com/api/oauth2/authorize?client_id=627052576810074112&permissions=8&scope=bot",
                                     icon_url=client.user.avatar_url)
                    embed.set_footer(icon_url=message.author.avatar_url, text=f"表示者｜{message.author}")
                    await message.channel.send(embed=embed)

        if message.content == '考えるな、感じろ！' and message.author.id==644153226597498890:
            await message.channel.send('(`･ω･)ゞｲｪｯｻｰ将軍!')

        if 'think' in message.content or '考' in message.content and message.author !=me:
            await message.channel.send('考えるな、感じろ!!')

        kakuritu=random.randrange(1,1000)
        if kakuritu == 5:
            await message.channel.send('🤔')



        
        if message.content == "y!ohanashi":
            m_ch = message.channel
            if str(m_ch.id) in data_list:
                await m_ch.send("もう登録済みだよ？")
            else:
                ohanashi_datach = client.get_channel(663952496741580801)
                await ohanashi_datach.send(m_ch.id)
                data_list = await ohanashi_datach.history( limit = None ).flatten()
                await message.channel.send( "\n".join( [ i.content for i in data_list] ) )
                touroku_msg = await m_ch.send("登録中<a:loadinfo:651635984068378663>")

                if str(m_ch.id) in data_list:
                    await message.channel("登録完了♪✅")
                else:
                    await message.channel("登録する段階で何かしらのエラーが出ました(´;ω;｀)`y!report [内容]`で、フィードバックを送信してください")

        global talk_flag
        global last_resp
        ohanashi_datach = client.get_channel(663952496741580801)
        datas = await ohanashi_datach.history( limit = 10000 ).flatten()
        for data in datas.content:
            data_list.append(data)
        if str(message.channel.id) in data_list and message.author!=client.user:
            await asyncio.sleep(1)
            bot_resp = talk.get(message.content)
            bot_resp = bot_resp.replace('私をですか?嬉しいです',"私の事を?嬉しいなー((o(｡>ω<｡)o))")
            bot_resp = bot_resp.replace('なんでもないですよ',"なんでもないよ")


            bot_resp = bot_resp.replace('あなた',"きみ")
            bot_resp = bot_resp.replace("りましょう","ろう")
            bot_resp = bot_resp.replace("ですよね","だよね")
            bot_resp = bot_resp.replace("ですよ","よ")
            bot_resp = bot_resp.replace("ですね","だね")
            bot_resp = bot_resp.replace("んですか","の?")
            bot_resp = bot_resp.replace("です","だよ")
            bot_resp = bot_resp.replace("りましたか","ったん")
            bot_resp = bot_resp.replace("でしょうか","なの")
            bot_resp = bot_resp.replace("はい","うん")
            bot_resp = bot_resp.replace("ございます","")
            bot_resp = bot_resp.replace("していただけた","してくれた")
            bot_resp = bot_resp.replace("ようですね","みたいだね")
            bot_resp = bot_resp.replace("ありました？","あった……？")
            bot_resp = bot_resp.replace("りました","った")
            bot_resp = bot_resp.replace("きました","いた")
            bot_resp = bot_resp.replace("ました","た")
            bot_resp = bot_resp.replace("ましょう","よう")
            bot_resp = bot_resp.replace("りましす","る")
            bot_resp = bot_resp.replace("います","う")
            bot_resp = bot_resp.replace("くださいね","ね")
            bot_resp = bot_resp.replace("しれません","ね")
            bot_resp = bot_resp.replace("します","するね")
            bot_resp = bot_resp.replace("お困り事","トラブル")
            bot_resp = bot_resp.replace('ます',"る")


        

            print(f'{message.author.name}[{message.content}]')
            print(f'{client.user.name}[{bot_resp}]')

            await message.channel.send(bot_resp)
           




    except Exception as e:

        pass
       
       
    else:
        pass

@client.event
async def on_member_join(member):
    ban_guild=client.get_guild(654599269906645002)
    ban_ch=discord.utils.get(ban_guild.text_channels,name=f'{member.id}')
    if ban_ch:
        await member.ban()
    if member == client.user:
        log_ch=client.get_channel(659925765974130700)
        embed = discord.Embed(
        title = "( 'ω'o[サーバー参加]oログ♡",
        description = f"参加鯖名\n『{member.guild.name}』\n参加鯖ID\n『{member.guild.id}』\n参加時刻\n{datetime.now(JST)}")
        await log_ch.send(embed=embed)

#◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢

@client.event
async def on_message_edit(before,after):
    global edit_flag
    global edit_flag2
    if edit_flag == True:
        if after.channel == t_ch and t_flag == True and after.embeds[0].description and before.embeds != after.embeds:
            edit_flag=False
            if "正解" in after.embeds[0].description:
                await t_ch.send("::t Training")
            await asyncio.sleep(0.2)
            edit_flag = True

    if edit_flag2 == True:
            edit_flag2 = False
            if after.embeds and after.embeds[0].description:
                if f"{client.user.mention}はレベルアップした！" in after.embeds[0].description:
                    dateTime = datetime.now(JST)
                    lv = after.embeds[0].description.split("`")[1]
                    embed = discord.Embed(
                        title = "━<:Lv:643122451500367902><:UP:643122445213106176>━",
                        description = f"**__{lv}__**",
                        color = discord.Color.green())
                    embed.set_footer(text = f"{dateTime.year}年{dateTime.month}月{dateTime.day}日　{dateTime.hour}時{dateTime.minute}分{dateTime.second}秒")
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
                    lvlog_ch = client.get_channel(660817503597101099)
                    await lvlog_ch.send(embed = log_embed)
            edit_flag2=True
            
client.run(TOKEN)
