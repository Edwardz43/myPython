import re
import requests
import json

def get_game_info(week):

    url = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2017/league/00_full_schedule_week.json';

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'}
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    JSON_Dict = json.loads(html.text)
    JSON_lscd = JSON_Dict['lscd']
    game_info = []
    for data in JSON_lscd:
        JSON_mscd = data['mscd']
        JSON_GAMES = JSON_mscd['g']

        for game in JSON_GAMES:
            g = game['gweek']
            if g == week:
                game_info.append(game)

def get_game_id(game_info_list):
    game_id = []
    

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