import base64
import json
from urllib.parse import urlencode
from spider.Utils.loopRequest import LoopRequest
from spider.bili_index import utils
import re


class SpiderBili(object):
    def __init__(self):
        self.request = LoopRequest()
        self.url = {}
        self.init()

    def init(self):
        self.url['popular'] = 'https://api.bilibili.com/x/web-interface/popular?'
        self.url['online'] = 'https://www.bilibili.com/video/online.html'

    def online_list(self):
        url = self.url['online']
        response = self.request.get(url).content.decode('utf-8')
        return utils.get_online_list(response)

    def hot_list(self, ps=20, pn=1):
        url = self.url['popular'] + 'ps=%s&pn=%s' % (ps, pn)
        response = self.request.get(url).content.decode('utf-8')
        return utils.get_hot_list(response)

    def run(self):
        self.hot_list()


if __name__ == '__main__':
    spider = SpiderBili()
    spider.run()