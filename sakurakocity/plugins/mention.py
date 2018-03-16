# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
import random

@respond_to('ごはん')
def listen(message):
    message.reply('くれ')

@respond_to('お手|おて｜おかわり|たて|立て')
def respond(message):
    message.reply(random.choice(['ん？', 'ぽむむ〜？', 'お手だぞ', 'おかわりだぞ', '立てだぞ', 'もっと立てだぞ']))
