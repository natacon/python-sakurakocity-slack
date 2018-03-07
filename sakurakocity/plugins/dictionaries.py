# -*- coding: utf-8 -*-
import datetime

user_dict = {'yukinowacity': 'ゆきちゎ', 'makinowacity': 'まきちゎ'}
day_dict = {'couple_day': datetime.date(2015, 3, 7), 'marrige_day': datetime.date(2016, 3, 7)}

def get_user(message):
    return message._client.users[message.body['user']]
