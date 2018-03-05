# -*- coding: utf-8 -*-

from slackbot.bot import listen_to
import random
# from sakurakocity.dictionaries import user_dict
# from sakurakocity.libs import get_user

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
    message.send(random.choice(['のゎしてぃ！', 'ちゎしてぃ！']))

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
    message.send(user_dict[user['name']] + 'おつかれさまきゎだぞ:こちたまん:')

# 以下はimportしたい。
def get_user(message):
    return message._client.users[message.body['user']]

user_dict = {'yukinowacity': 'ゆきちゎ', 'makinowacity': 'まきちゎ'}
