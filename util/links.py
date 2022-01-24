#!/usr/bin/env python3

import re
import sys
from dateutil import parser
from transliterate import translit

corpus_directory = ''
redis_prefix = ''

re_header = re.compile(r'^\[(\d+)\]\w+')
re_link = re.compile(r'^\s+(\d+)\.\s+(https\:\/\/[^\?]+)\?.*')
re_distill_link = re.compile(r'(https\:\/\/[^\?]+)-[^-]+$')
re_date = re.compile(r'^\s+on\s+(Jan|Dec|Nov|Oct|Sep|Aug|Jul|Jun|May|Apr|Mar|Feb)\s+(\d+)\,?\s+?(\d+)?.*')


def distill(value):
    value = re.match(re_distill_link, value).groups(1)[0]
    return translit(value, 'ru', reversed=True).lower().strip() \
            .replace(' ', '-') \
            .replace(',', '')  \
            .replace('?', '')  \
            .replace('!', '')  \
            .replace('@', '')  \
            .replace(':', '')  \
            .replace(';', '')  \
            .replace('"', '')  \
            .replace("'", '')  \
            .replace("«", '')  \
            .replace("»", '')  \
            .replace('.', '-')


headers = []
dates = {}
 
 
for line in sys.stdin:
    m = re.match(re_header, line)
    if m:
        headers.append(m.groups(1)[0])
        print(headers[-1])
        continue
    m = re.match(re_date, line)
    if m:
        header = headers[-1]
        mdy = list(m.groups(1))
        if mdy[2] == 1:
            mdy[2] = '2022'
        date = parser.parse(' '.join(mdy)).isoformat()[0:10]
        dates[header] = date
    m = re.match(re_link, line)
    if m:
        header = m.groups(1)[0]
        if header not in headers: continue
        url = m.groups(1)[1]
        #print('wget', url, '-O', f'{dates.get(header, list(dates.values())[-1])}-{distill(url)[26:]}.md')
        print(url, f'{dates.get(header, list(dates.values())[-1])}-{distill(url)[26:]}.md')

