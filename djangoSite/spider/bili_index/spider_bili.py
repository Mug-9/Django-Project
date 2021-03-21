import base64
import json
from urllib.parse import urlencode
from spider.Utils.loopRequest import LoopRequest
from spider.bili_index import utils
import re

cookie = 'SESSDATA=e685c982%2C1631154796%2C88fe1*31'
header = {
            'Referer': 'https://m.bilibili.com/',
            'Origin': 'https://m.bilibili.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'Cookie': cookie
        }

class SpiderBili(object):
    def __init__(self):
        self.request = LoopRequest()
        self.url = {}
        self.init()

    def init(self):
        self.url['popular'] = 'https://api.bilibili.com/x/web-interface/popular?'
        self.url['online'] = 'https://www.bilibili.com/video/online.html'
        self.url['searchVideo'] = 'https://api.bilibili.com/x/web-interface/view?bvid'
        self.url['fans'] = 'https://api.bilibili.com/x/relation/stat?vmid='
        self.url['typename'] = 'https://api.bilibili.com/x/space/arc/search?pn=1&ps=100&order=click&keyword=&mid='
        self.url['views'] = 'https://api.bilibili.com/x/space/upstat?mid='
        self.url['info'] = 'https://api.bilibili.com/x/space/acc/info?mid='

    def online_list(self):
        url = self.url['online']
        response = self.request.get(url, isProxy=False).content.decode('utf-8')
        return utils.get_online_list(response)

    def hot_list(self, ps=20, pn=1):
        url = self.url['popular'] + 'ps=%s&pn=%s' % (ps, pn)
        response = self.request.get(url, isProxy=False).content.decode('utf-8')
        return utils.get_hot_list(response)

    def search_video(self, bv):
        url = self.url['searchVideo'] + '=%s' % bv
        res = self.request.get(url, isProxy=False).content.decode('utf-8')
        res = json.loads(res)
        utils.parse_data(res['data'])
        return res['data']

    def search_up(self, mid):
        url = '%s%s' % (self.url['fans'], mid)
        result = {}
        res = self.request.get(url, isProxy=False).content.decode('utf-8')
        res = json.loads(res)
        result['fans'] = utils.relieve_num(res['data']['follower'])
        url = self.url['typename'] + mid
        res = self.request.get(url, isProxy=False).content.decode('utf-8')
        res = json.loads(res)
        result['video_count'] = utils.relieve_num(res['data']['page']['count'])

        url = '%s%s' % (self.url['views'], mid)
        res = self.request.get(url, isProxy=False, headers=header).content.decode('utf-8')
        res = json.loads(res)
        result['views'] = utils.relieve_num(res['data']['archive']['view'])
        result['like'] = utils.relieve_num(res['data']['likes'])

        url = '%s%s' % (self.url['info'], mid)
        res = self.request.get(url, isProxy=False).content.decode('utf-8')
        res = json.loads(res)
        result['name'] = res['data']['name']
        result['mid'] = res['data']['mid']
        result['face'] = res['data']['face']
        return result

    def run(self):
        print(self.search_up('65593413'))


if __name__ == '__main__':
    spider = SpiderBili()
    spider.run()