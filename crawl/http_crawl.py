import re
import requests
import json

url = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2017/league/00_full_schedule_week.json';
urls = [];
#
# for index in range(1, 27):
#     tmp_url = re.sub('/#!?(.*?)&PD', '/#!?Week=%d&PD' % index, url)
#     urls.append(tmp_url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
html = requests.get(url, headers=headers).content
# html = requests.get(url)
# html.encoding = 'utf-8'
JSON_Dict = json.loads(html)
JSON_lscd = JSON_Dict['lscd']

game_info = []

for data in JSON_lscd:
    JSON_mscd = data['mscd']
    JSON_GAMES = JSON_mscd['g']

    for game in JSON_GAMES:
        g = game['gweek']
        if g == 1:
            game_info.append(game)

print(game_info)

# fp = open('tmp.txt', 'wb')
# fp.write(html.content)
# fp.close()


# patent = 'class="nav_content_block_entry">(.*?)</div>'
# tmp_links = re.findall(patent, html.text, re.S)
#
# patent_class = '">(.*?)</a>'
# links = re.findall(patent_class, tmp_links.__str__(), re.S)
#
# for each in links:
#     print(each)