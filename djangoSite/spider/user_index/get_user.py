import requests
import re
import json
from spider.Utils.loopRequest import LoopRequest
from spider.user_index import utils

request = LoopRequest()

url = 'https://www.bilibili.com/read/cv9222187?from=search'

res = request.get(url).content.decode('utf-8')
name_p = re.findall(r'<p><span class="font-size-12" style="">(.*?)</span></p>', res, re.S)
name_p2 = re.findall(r'<p><span class="font-size-12">(.*?)</span></p>', res, re.S)
print(name_p)
print(name_p2)
name_list = []
for names in name_p:
    names = names.replace('<span class="font-size-12">', '')
    names = names.replace('</span>', '')
    names = names[3:]
    ns = names.split('、')
    for n in ns:
        name_list.append(n)

for names in name_p2:
    names = names.replace('<span class="font-size-12">', '')
    names = names.replace('</span>', '')
    names = names[3:]
    ns = names.split('、')
    for n in ns:
        name_list.append(n)

name_list = name_list[1:]

with open('name.txt', 'w') as f:
    for name in name_list:
        f.write(name + '、')
f.close()