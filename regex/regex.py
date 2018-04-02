import re
import requests
# from re import findall, search, S;
#
# secret_code = '1615156165xxIxx161561xxlovexx15115xxyouxx';
#
# a = re.findall('xx.?', secret_code);
# print(a);
#
# b = re.findall('xx.*', secret_code);
# print(b);
#
# c = re.findall('xx.*?', secret_code);
# print(c);
#
# d = re.findall('xx.*?xx', secret_code);
# print(d);
#
#
# e = re.findall('xx(.*?)xx', secret_code);
#
# for each in e:
#     print(each)
#
#
# s = '''1615156165xxI
#     xx161561xxlovexx15115xxyouxx''';
#
# f = re.findall('xx(.*?)xx', s, re.S);
# print(f);

# s2 = 'asdfxxIxx123xxlovexxasdfxxyouxxdsasd'
# reg = 'xx(.*?)xx123xx(.*?)xxasdfxx(.*?)xx';
# g = re.search(reg, s2).group(1);
# h = re.findall(reg, s2);
#
# print(g);
#
# print(h[0][0]);
#
# digit = '123fdfgdgfgfd123';
# i = re.sub('123(.*?)123', '123%d123' % 789, digit);
# print(i);
#
# digits = 'dsads12345689sadsa11515asdsd';
# j = re.findall('(\d+)', digits);
# print(j[0]);

#
# url = 'http://stats.nba.com/schedule/#!/?rfr=nba&Week=1&PD=N';
# for i in range(1, 27):
#     new_url = re.sub('nba&(.*?)&PD', 'nba&Week=%d&PD' % i, url);
#     print(new_url);

f = open('source.txt', 'r', 1, 'utf8')
html = f.read()
f.close()

pic_url = re.findall('img src="(.*?)" class="lessonimg"', html, re.S)
i = 0
for each in pic_url:
    print('now downloading : ' + each)
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.jpg', 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1