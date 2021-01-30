import base64
import json
from urllib.parse import urlencode
from spider.Utils.loopRequest import LoopRequest
from spider.bili_index import utils
import re


class SpiderBili(object):
    def __init__(self):
        self.request = LoopRequest()

    def online_list(self):
        url = 'https://www.bilibili.com/video/online.html'
        response = self.request.get(url).content.decode('utf-8')
        return utils.get_online_list(response)

    def run(self):
        self.online_list()


if __name__ == '__main__':
    spider = SpiderBili()
    spider.run()