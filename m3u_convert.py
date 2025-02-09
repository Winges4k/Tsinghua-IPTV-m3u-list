# -*- coding: utf-8 -*-

from urllib import request
import json

channels_url = 'https://raw.githubusercontent.com/ericziethen/ez-iptvcat-scraper/master/data/countries/france.json'
channels_json = request.urlopen(channels_url).read().decode('utf8')
channels = json.loads(channels_json)

f = open('channels.m3u', 'w+', encoding='utf-8')

f.write('#EXTM3U\n')

for i in range(len(channels['Categories'])):
    for j in range(len(channels['Categories'][i]['Channels'])):
        line_1 = '#EXTINF:-1 group-title="' + channels['Categories'][i]['Name'] + '",' + channels['Categories'][i]['Channels'][j]['Name'] + '\n'
        m3u8_url = 'https://github.com/ericziethen/ez-iptvcat-scraper/blob/master/data/countries/' + channels['Categories'][i]['Channels'][j]['Vid'] + '.m3u8'
        f.write(line_1)
        f.write(m3u8_url + '\n')

f.close()
