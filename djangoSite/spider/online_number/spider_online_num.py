import json
import pymysql
import sys
sys.path.append("..")
from Utils.loopRequest import LoopRequest


class SpiderOnlineNumber(object):
    def __init__(self):
        self.url = 'https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getList?platform=web'
        self.number = 0
        self.connect = None
        self.cursor = None
        self.request = LoopRequest()

    def link_database(self):
        self.connect = pymysql.connect(host="123.56.252.111", user='root', password="123456",
                                  port=3306, db='test', charset='utf8')
        self.cursor = self.connect.cursor()

    def insert_database(self):
        self.link_database()
        sql = "insert into backend_onlinenumber(number, date, time) values(%s, now(), now())" % self.number
        self.cursor.execute(sql)
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

    def get_number(self):
        response = self.request.get('https://api.live.bilibili.com/xlive/web-interface/v1/webMain/getList?platform=web')
        response_data = response.content.decode('utf-8')
        print(response_data)
        json_data = json.loads(response_data)
        self.number = (json_data['data']['dynamic'])

    def run(self):
        self.get_number()
        self.insert_database()