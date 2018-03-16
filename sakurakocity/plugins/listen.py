# -*- coding: utf-8 -*-
from slackbot.bot import listen_to
import random
from .dictionaries import *
import datetime

@listen_to('ん～|ん〜')
def nnn(message):
    message.send(random.choice(['ましゃーーー！']))

@listen_to('らこしてぃ|さく|らこすて')
def rakosute(message):
    message.send(random.choice(['なんだ？', 'よんだ？']))

@listen_to('よしよし')
def yoshiyoshi(message):
    message.send(random.choice(['よしよしまきゎ']))

@listen_to('ちゎ|ちわ|ちぁ|ちあ')
def chiwa(message):
    message.send(random.choice(['ちゎ！']))

@listen_to('のゎ|まきゎ|まきわ|のわ|のゎ|ちゎしてぃ|のゎしてぃ|のゎたしてぃ')
def nowa(message):
    message.send(random.choice(['ちゎしてぃ！']))

@listen_to('うんこ|しっこ')
def shicco(message):
    message.react('shit')
    message.send(random.choice(['うんこゎたしてぃ！', 'しっこゎたしてぃ！']))

@listen_to('らふこふ')
def listen(message):
    message.send('らこしてぃだぞ')

@listen_to('こちたまん')
def kochitaman(message):
    message.react('こちたまん')

@listen_to('ありがと')
def thankyou(message):
    message.react('まきちゎ')

@listen_to('user_info')
def user_info(message):
    user = get_user(message)
    message.send(str(user))

@listen_to('しごおわ')
def shigoowa(message):
    user = get_user(message)
    message.send(user_dict[user['name']] + 'おつかれさまきゎだぞ。:こちたまん:')

@listen_to('結婚して|けっこんして|marrige')
def marrige_count(message):
    diff_d = diff_day(day_dict['marrige_day'], datetime.date.today())
    message.send('結婚して' + str(diff_d) + u'日だぞ。')
    print(diff_year(day_dict['marrige_day'], datetime.date.today()))

@listen_to('付き合って|つきあって|couple|カップル')
def couple_count(message):
    diff_d = diff_day(day_dict['couple_day'], datetime.date.today())
    message.send('付き合って' + str(diff_d) + u'日だぞ。')

@listen_to('何の日|なんのひ')
def what_day(message):
    today = datetime.date.today()
    if today.month == 3 and today.day == 7:
        message.send('記念日だぞ')
    if today.month == 10 and today.day == 10:
        message.send('プロポーズの日だぞ')
    if today.month == 2 and today.day == 4:
        message.send('結婚式の日だぞ')
    if today.month == 1 and today.day == 1:
        message.send('まきちゎの誕生日だぞ')
    if today.month == 1 and today.day == 13:
        message.send('ゆきちゎの誕生日だぞ')
    else:
        message.send('ん？')

@listen_to('anniv')
def anniversary(message):
    message.send(str(day_dict))

@listen_to('何日目')
def day_count(message):
    diff_couple = diff_day(day_dict['couple_day'], datetime.date.today())
    diff_marrige = diff_day(day_dict['marrige_day'], datetime.date.today())
    message.send('付き合って' + str(diff_couple + 1) + u'日目、結婚して' + str(diff_marrige + 1) + u'日目だぞ。')

def diff_day(d1: datetime.date, d2: datetime.date) -> int:
    if d1 > d2:
        d1, d2 = d2, d1
    return (d2 - d1).days

def diff_month(d1: datetime.date, d2: datetime.date) -> int:
    if d1 > d2:
        d1, d2 = d2, d1
    return (d2.year - d1.year) * 12 + d2.month - d1.month

def diff_year(d1: datetime.date, d2: datetime.date) -> float:
    if d1 > d2:
        d1, d2 = d2, d1
    diff_m = (d2.year - d1.year) * 12 + d2.month - d1.month
    return diff_m/12
