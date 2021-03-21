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

maxconnections = 50
pool_sema = threading.BoundedSemaphore(value=maxconnections)
cookie = 'SESSDATA=e685c982%2C1631154796%2C88fe1*31'


class UpdateUserInfo(object):

    def __init__(self):
        self.baseUrl = ['https://api.bilibili.com/x/relation/stat?vmid=','https://api.bilibili.com/x/space/upstat?mid=', 'https://api.bilibili.com/x/space/arc/search?pn=1&ps=100&order=click&keyword=&mid=']
        self.db_pool = {}

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

    def get_type_name(self, mid):
        req = LoopRequest()
        url = '%s%s' % (self.baseUrl[2], mid)
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
        }
        loop = 30
        while loop:
            try:
                res = req.get(url, headers=header)
                if res.status_code == 200:
                    response = res.content.decode('utf-8')
                    response_json = json.loads(response)
                    count = response_json['data']['list']
                    res.close()
                    return response_json
            except Exception as e:
                print(e)
            loop -= 1
            time.sleep(2)
        return {'code': 400}

    def get_fans(self, mid):
        req = LoopRequest()
        url = '%s%s' % (self.baseUrl[0], mid)
        loop = 30
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
        }
        while loop:
            try:
                res = req.get(url, headers=header)
                if res.status_code == 200:
                    response = res.content.decode('utf-8')
                    response_json = json.loads(response)
                    fans = response_json['data']['follower']
                    res.close()
                    return response_json
            except Exception as e:
                print(e)
            loop -= 1
            time.sleep(2)
        return {'code': 400}

    def get_views(self, mid):
        req = LoopRequest()
        url = '%s%s' % (self.baseUrl[1], mid)
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
        loop = 30
        while loop:
            try:
                res = req.get(url, headers=header)
                if res.status_code == 200:
                    response = res.content.decode('utf-8')
                    response_json = json.loads(response)
                    views = response_json['data']['archive']
                    res.close()
                    return response_json
            except Exception as e:
                print(e)
            loop -= 1
            time.sleep(2)
        return {'code': 400}

    def update_views(self, response_json, mid):
        thread_id = threading.currentThread().ident
        if response_json['code'] == 400:
            return
        try:
            views = response_json['data']['archive']['view']
            like = response_json['data']['likes']
            update = "update backend_usersofb set archive_view=%s, archive_like=%s where(mid='%s');" % (views, like, mid)
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(update)
            self.db_pool[thread_id].commit()
        except Exception as e:
            print(e)
        time.sleep(2)

    def update_fans(self, response_json, mid):
        thread_id = threading.currentThread().ident
        if response_json['code'] == 400:
            return
        try:
            fans = response_json['data']['follower']
            select = "select * from backend_usersofb where(mid='%s');" % mid
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(select)
            res = cur.fetchone()
            fans_month_ago = res[8]
            fans_week_ago = res[9]
            fans_yesterday = res[10]
            old_fans = res[3]
            update = "update backend_usersofb set fans=%s, fans_yesterday=%s, fansd_yesterday=%s where(mid='%s');" % (fans, old_fans, old_fans-fans_yesterday, mid)
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(update)
            self.db_pool[thread_id].commit()
            nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            insert = "insert into backend_userfans(mid, fans, time) values('%s', %s, '%s')" % (mid, fans, nowTime)
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(insert)
            self.db_pool[thread_id].commit()
            day = datetime.now().strftime('%w')
            if int(day) == 1:
                update = "update backend_usersofb set fans_week_ago=%s, fansd_week_ago=%s where(mid='%s');" % (old_fans, old_fans-fans_week_ago, mid)
                self.check_conn(thread_id)
                cur = self.db_pool[thread_id].cursor()
                cur.execute(update)
                self.db_pool[thread_id].commit()
            day = datetime.now().strftime('%d')
            if int(day) == 1:
                update = "update backend_usersofb set fans_month_ago=%s, fansd_month_ago=%s where(mid='%s');" % (
                    old_fans, old_fans - fans_month_ago, mid)
                self.check_conn(thread_id)
                cur = self.db_pool[thread_id].cursor()
                cur.execute(update)
                self.db_pool[thread_id].commit()
        except Exception as e:
            print(e)
        time.sleep(2)

    def update_type_name(self, response_json, mid):
        thread_id = threading.currentThread().ident
        if response_json['code'] == 400:
            return
        try:
            video_count = response_json['data']['page']['count']
            select = "select * from backend_usersofb where(mid='%s');" % mid
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(select)
            res = cur.fetchone()
            video_count_week_ago = res[14]
            video_count_month_ago = res[16]
            old_video_count = res[7]
            update = "update backend_usersofb set video_count=%s where(mid='%s')" % (video_count, mid)
            self.check_conn(thread_id)
            cur = self.db_pool[thread_id].cursor()
            cur.execute(update)
            self.db_pool[thread_id].commit()
            day = datetime.now().strftime('%w')
            if int(day) == 1:
                update = "update backend_usersofb set video_count_week_ago=%s, videod_week_ago=%s where(mid=%s);" % (
                    old_video_count, old_video_count-video_count_week_ago, mid
                )
                self.check_conn(thread_id)
                cur = self.db_pool[thread_id].cursor()
                cur.execute(update)
                self.db_pool[thread_id].commit()
            day = datetime.now().strftime('%d')
            if int(day) == 1:
                update = "update backend_usersofb set video_count_month_ago=%s, videod_month_ago=%s where(mid=%s)" % (
                    old_video_count, old_video_count - video_count_month_ago, mid)
                self.check_conn(thread_id)
                cur = self.db_pool[thread_id].cursor()
                cur.execute(update)
                self.db_pool[thread_id].commit()
        except Exception as e:
            print(e)

        time.sleep(2)

    def thread_func(self, mid):
        with pool_sema:
            print(mid)
            thread_id = threading.currentThread().ident
            self.db_pool[thread_id] = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test', charset='utf8')
            self.update_fans(self.get_fans(mid), mid)
            self.update_type_name(self.get_type_name(mid), mid)
            self.update_views(self.get_views(mid), mid)
            self.db_pool[thread_id].close()
            print('%s 完成' % mid)

    def run(self):
        conn = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test', charset='utf8')
        cursor = conn.cursor()
        select = "select * from backend_usersofb;"
        cursor.execute(select)
        all = cursor.fetchall()
        conn.close()
        thread_list = []
        for each in all:
            m = threading.Thread(target=self.thread_func, args=[each[1],])
            m.start()
            thread_list.append(m)
        for th in thread_list:
            th.join()
        print('update over')


if __name__ == '__main__':
    update = UpdateUserInfo()
    while True:
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if now_time[14:16] == '00':
            print(now_time[11:])
        if now_time[11:] == '13:40:00':
            update.run()
        time.sleep(1)