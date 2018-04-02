import re
import requests

url = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/2017/league/00_full_schedule_week.json';
urls = [];
#
# for index in range(1, 27):
#     tmp_url = re.sub('/#!?(.*?)&PD', '/#!?Week=%d&PD' % index, url)
#     urls.append(tmp_url)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
html = requests.get(url, headers=headers)
# html = requests.get(url)
html.encoding = 'utf-8'
print(html.json())

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