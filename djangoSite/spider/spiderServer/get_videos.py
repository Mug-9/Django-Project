import json
import asyncio
import threading
from urllib.parse import urlencode
from loopRequest import LoopRequest
from datetime import datetime, time
import time
import base64
import json
from urllib.parse import urlencode
import utils
import re
import MySQLdb as md

conn = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test', charset='utf8')
cursor = conn.cursor()

cookie = 'SESSDATA=3e018edc%2C1630047578%2Cc5952*21'
header = {
    'Referer': 'https://www.bilibili.com/',
    'Origin': 'https://www.bilibili.com',
    'Cookie': cookie,
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'close'
}


class SpiderBili(object):
    def __init__(self):
        self.url = {}
        self.init()
        self.db_pool = {}

    def init(self):
        self.url['popular'] = 'https://api.bilibili.com/x/web-interface/popular?'
        self.url['online'] = 'https://www.bilibili.com/video/online.html'

    def online_list(self):
        req = LoopRequest()
        url = self.url['online']
        loop = 50
        while loop:
            try:
                res = req.get(url)
                if res.status_code == 200:
                    response = res.content.decode('utf-8')
                    res.close()
                    return utils.get_online_list(response)
            except Exception as e:
                print(e)
            loop -= 1
        return []

    def hot_list(self, ps=20, pn=1):
        req = LoopRequest()
        url = self.url['popular'] + 'ps=%s&pn=%s' % (ps, pn)
        loop = 50
        while loop:
            try:
                res = req.get(url)
                if res.status_code == 200:
                    response = res.content.decode('utf-8')
                    res.close()
                    return utils.get_hot_list(response)
            except Exception as e:
                print(e)
            time.sleep(2)
            loop -= 1
        return []

    def check_conn(self, thread_id):
        while True:
            try:
                self.db_pool[thread_id].ping(True)
                break
            except Exception as e:
                print(e)
                self.db_pool[thread_id] = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test',
                                 charset='utf8')
            time.sleep(5)

    def thread(self, index, now_time):
        thread_id = threading.currentThread().ident
        print('thread: %s' % thread_id)
        if index == 0:
            res = self.online_list()
        else:
            res = self.hot_list(20, index)

        for video in res:
            bvid = video['bvid']
            check = "select * from backend_videosdata where(bvid='%s');" % bvid
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(check)
            if cur.fetchone() is None:
                print('新加入数据')
                pubdate = utils.parse_time(video['pubdate'])
                insert = "insert into backend_videosdata(bvid, dateTime, view, coin, danmaku, reply, share, love, favorite) values('%s', '%s', %s, %s, %s, %s, %s, %s, %s);" % (video['bvid'], pubdate, 0, 0, 0,
                       0, 0, 0, 0)
                self.check_conn(thread_id)
                cur = self.db_pool[thread_id].cursor()
                cur.execute(insert)
                self.db_pool[thread_id].commit()
            check = "select * from backend_videosdata where(bvid='%s' and dateTime='%s');" % (bvid, now_time)
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(check)
            if cur.fetchone() is not None:
                print('%s 已存在' % bvid)
                continue
            insert = "insert into backend_videosdata(bvid, dateTime, view, coin, danmaku, reply, share, love, favorite) values('%s', '%s', %s, %s, %s, %s, %s, %s, %s);" % (
            video['bvid'], now_time, video['stat']['view'], video['stat']['coin'], video['stat']['danmaku'],
            video['stat']['reply'], video['stat']['share'], video['stat']['like'], video['stat']['favorite'])
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(insert)
            self.db_pool[thread_id].commit()
            time.sleep(1)

    def run(self, now_time):
        thread_list = []
        for index in range(1, 11):
            m = threading.Thread(target=self.thread, args=[index,now_time])
            thread_list.append(m)
        m = threading.Thread(target=self.thread, args=[0,now_time])
        thread_list.append(m)
        for th in thread_list:
            th.start()
        for th in thread_list:
            th.join()


if __name__ == '__main__':
    spider = SpiderBili()
    while True:
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hour = now_time[11:13]
        print(now_time)
        if now_time[14:] == '00:00':
            if int(hour) % 2 == 0:
                spider.run(now_time)
        time.sleep(1)

