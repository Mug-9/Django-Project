import pymysql
import json
import sys
from urllib.parse import urlencode
sys.path.append("..")
from spider.Utils.loopRequest import LoopRequest


class SpiderBaidu(object):

    def __init__(self):
        self.cookies = ""
        self.request = LoopRequest()
        self.type = {}
        self.header = {}
        self.init()

    def init(self):
        self.cookies = "BDUSS=2ptTjI3OEpYMVNpOVpQY0ZCT2Ftd1NCb0tWdlhTWXM4RVFxMmtSSm5QWklXaHRnRVFBQUFBJCQAAAAAAAAAAAEAAAAelm82tcu66sHBusPRp8n6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEjN819IzfNfc"
        self.type['crowd'] = 'https://index.baidu.com/api/SocialApi/baseAttributes?'
        self.header = {
            'Host': 'index.baidu.com',
            'Cookie': self.cookies
        }

    def get_crowd(self):
        keywords = ['b站官网']
        request_args = {
            'wordlist[]': keywords[0]
        }
        url = self.type['crowd'] +  urlencode(request_args)
        print("crowd url: ", url)
        response = self.request.get(url=url, headers=self.header).content.decode('utf-8')
        response_data = json.loads(response)
        result = response_data['data']['result']
        result_b = result[0]
        result_all = result[1]
        return result_b, result_all

    def run(self):
        self.get_crowd()


# if __name__ == "__main__":
#     spider = SpiderBaidu()
#     spider.run()
