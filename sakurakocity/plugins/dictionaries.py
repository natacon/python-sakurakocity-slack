# -*- coding: utf-8 -*-
import datetime

user_dict = {'yukinowacity': 'ゆきちゎ', 'makinowacity': 'まきちゎ'}
day_dict = {
    'couple_day': datetime.date(2015, 3, 7),
    'propose_day': datetime.date(2015, 10, 10),
    'marrige_day': datetime.date(2016, 3, 7),
    'wedding_day': datetime.date(2018, 2, 4),
}
day_dict2 = {
    'couple_day': datetime.date(2015, 3, 7),
    'propose_day': datetime.date(2015, 10, 10),
    'marrige_day': datetime.date(2016, 3, 7),
    'wedding_day': datetime.date(2018, 2, 4),
}

def get_user(message):
    return message._client.users[message.body['user']]
