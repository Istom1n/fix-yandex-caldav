#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re

import requests as r
from ics import Calendar, Event


URL = "https://{0}:{1}@caldav.yandex.ru/calendars/{0}%40yandex.ru/events-7492773/".format(YANDEX_LOGIN, YANDEX_PASSWORD)
REGEX_PATTERN = r"(?:.{8}yandex.ru.ics)+"


def get_all_ics():
    res = r.get(URL).text

    return re.findall(REGEX_PATTERN, res, re.MULTILINE | re.IGNORECASE)


def get_all_events():
    icses = get_all_ics()
    
    #cals = [Calendar(requests.get(URL + ics).text) for ics in icses]
    res = r.get(URL + icses[0])
    res.encoding = 'ISO-8859-1'
    print(res.text)


def upgrade_all_events():
    icses = get_all_ics()

    return [event for event in icses]


def link_on_ics_file():
    pass


get_all_events()