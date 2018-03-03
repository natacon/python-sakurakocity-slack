# -*- coding: utf-8 -*-

from slackbot.bot import respond_to, listen_to, default_reply
import random

@listen_to('ん～')
@listen_to('ん〜')
def nnn(message):
    message.send(random.choice(['ましゃーーー！']))

@listen_to('らこしてぃ')
@listen_to('さく')
@listen_to('らこすて')
def rakosute(message):
    message.send(random.choice(['なんだ？', 'よんだ？']))

@listen_to('よしよし')
def yoshiyoshi(message):
    message.send(random.choice(['よしよしまきゎ']))

@listen_to('ちゎ')
@listen_to('ちわ')
@listen_to('ちぁ')
@listen_to('ちあ')
def chiwa(message):
    message.send(random.choice(['ちゎ！']))

@listen_to('まきのゎ')
@listen_to('まきゎ')
@listen_to('まきわ')
@listen_to('まきのわ')
@listen_to('ゆきのゎ')
@listen_to('ゆきのわ')
@listen_to('ちゎしてぃ')
@listen_to('のゎしてぃ！')
@listen_to('のゎたしてぃ！')
def nowa(message):
    message.send(random.choice(['のゎしてぃ！', 'ちゎしてぃ！']))

@listen_to('うんこ')
@listen_to('しっこ')
def shicco(message):
    message.send(random.choice(['うんこゎたしてぃ！', 'しっこゎたしてぃ！']))

@listen_to('らふこふ')
def listen(message):
    message.send('らこしてぃだぞ')
