import json
import ssl
import time
from lxml import etree
import requests
import user_agent_list
import re
import random
import MySQLdb as md
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

ssl._create_default_https_context = ssl._create_unverified_context


class SpiderProxy():
    def __init__(self):
        self.url = 'https://ip.jiangxianli.com/?'
        self.header = user_agent_list.getheaders()
        self.proxy = {}
        self.proxies_list = []
        self.conn = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test')
        self.cursor = self.conn.cursor()
        self.run()

    def get_proxies_list(self):
        select = "select * from backend_proxies"
        self.cursor.execute(select)
        rets = self.cursor.fetchall()
        self.conn.close()
        for ret in rets:
            proxy = {
                'http': 'http://%s' % ret[1],
                'https': 'http://%s' % ret[1]
            }
            self.proxies_list.append(proxy)

    def get_proxy(self):
        self.proxy = random.choice(self.proxies_list)
        self.header = user_agent_list.getheaders()

    def run(self):
        self.get_proxies_list()
        self.get_proxy()


if __name__ == "__main__":
    sp = SpiderProxy()
    sp.get_proxy()