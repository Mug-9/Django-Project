import requests
from spider.Utils.spider_proxy import SpiderProxy
import time


class LoopRequest(object):
    def __init__(self):
        self.proxies = SpiderProxy()
        self.count = 0

    def get(self, url, **args):
        return self.request('GET', url, **args)

    def post(self, url, **args):
        return self.request('POST', url, **args)

    def get_proxy(self):
        if self.count <= 0:
            self.proxies.get_proxy()
            self.count = 50
        self.count -= 1

    def request(self, method, url, **args):
        self.get_proxy()
        if "headers" in args:
            args['headers']['User-Agent'] = self.proxies.header['User-Agent']
            # args['Connection'] = 'keep-alive',
            # args['X-Requested-With'] = 'XMLHttpRequest',
        else:
            args['headers'] = self.proxies.header
        args['proxies'] = self.proxies.proxy
        args['timeout'] = 5
        args['verify'] = False
        loop = 50
        while loop:
            try:
                print("loopRequest: 第 %s 次尝试 %s" % (51-loop, url))
                requests.packages.urllib3.disable_warnings()
                response = requests.request(method, url, **args)
                print("loopRequest: %s 链接成功" % url)
                return response
            except Exception as e:
                print("loopRequest: Exception ", e)
                time.sleep(5)
                if loop == 0:
                    return "get error"
            loop -= 1