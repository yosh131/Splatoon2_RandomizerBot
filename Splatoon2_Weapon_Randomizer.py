# -*- coding: utf-8 -*-
import sys
import discord
import numpy as np
from numpy.random import *
import pandas as pd

TOKEN = 'NjkzMTMxMDk5NDU4NTAyNjk2.Xn4yZg._VSvM8CR6pMpRyF2l1yqiR09p9I'

shorts = pd.read_table('short.txt', 
                     encoding='shift_jis',
                     header = None)

middles = pd.read_table('middle.txt', 
                     encoding='shift_jis',
                     header = None)

longs = pd.read_table('long.txt', 
                     encoding='shift_jis',
                     header = None)

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')
    
@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == '/neko':
        await message.channel.send('にゃーん')
        
    if message.content == '/random':
        S = ''
        S += getWeapon(0) + '\n'
        S += getWeapon(0) + '\n'
        S += getWeapon(1) + '\n'
        S += getWeapon(2) + '\n'
        await message.channel.send(S)
        


def getWeapon(distance):
    # distance:0~2で短・中・長射程
    if distance==0:
        L = shorts.size
        return shorts[0][randint(0,L)]
    elif distance==1:
        L = middles.size
        return middles[0][randint(0,L)]
    elif distance==2:
        L = longs.size
        return longs[0][randint(0,L)]
    else:
        return -1
        
client.run(TOKEN)