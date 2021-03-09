
import asyncio
import json
import time
from urllib.parse import urlencode

from pyppeteer import launch


from spider.Utils.loopRequest import LoopRequest
request = LoopRequest()

def get():
    return ['a', 'b', 'c']

print(get())

time.sleep(100)

cookie = 'SESSDATA=3e018edc%2C1630047578%2Cc5952*21'

header = {
    'Refer': 'https://space.bilibili.com/',
    'Cookie': cookie,
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
}

url = 'https://api.bilibili.com/x/space/acc/info?mid=7552204'
res = request.get(url, headers=header).content.decode('utf-8')
print(res)

url = 'http://api.bilibili.com/x/relation/followings?'
params = {
    'vmid': 520149726,
    'order': 'desc',
    'ps': 20,
    'pn': 2,
}

url = url + urlencode(params)
print(url)


res = request.get(url, headers=header)
print(res)
data = res.content.decode('utf-8')
print(data)
if res.status_code == 200:
    data = json.loads(data)
    print(data['data']['list'])
