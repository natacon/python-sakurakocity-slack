# -*- coding: utf-8 -*-

from slackbot.bot import respond_to, listen_to, default_reply


@default_reply()
def default(message):
    message.reply('なんだ？')


@listen_to('ごはん')
def listen(message):
    message.reply('くれ')


@respond_to('お手')
def respond(message):
    message.reply('ん？')

@listen_to('らふこふ')
def listen(message):
    message.send('らこしてぃだぞ')
