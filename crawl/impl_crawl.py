import requests
import re
from bs4 import BeautifulSoup

res = requests.get('https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2017/league/00_full_schedule_week.json')
gid = re.findall('"gid": "(.*?)",', res.text, re.S)

link_patent = 'http://stats.nba.com/game/%d/'
links = []

for index in gid:
    link ='http://stats.nba.com/game/'+index + '/'
    links.append(link)

players_info = []
for i in range(0, links.__len__()):
    # 球員數據
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Referer': links.__getitem__(i)}
    player_date = 'http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID=' + gid.__getitem__(
        i) + '&RangeType=0&Season=2017-18&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'
    # 'http://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate=10/17/2017'
    player_info = requests.get(player_date, headers=headers)
    player_info.encoding = 'utf-8'
    print('get game_info : '+player_info.text)
    players_info.append(player_info.text)


#
# f = open('game_info.txt', 'wb')
# f.write(players_info.content)
# f.close()