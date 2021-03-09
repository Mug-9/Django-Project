import json
import asyncio
import threading
from urllib.parse import urlencode
from spider.Utils.loopRequest import LoopRequest
import time
import MySQLdb as md

max_connections = 30
pool_sema = threading.BoundedSemaphore(max_connections)
db_pool = {}

conn = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test', charset='utf8')
cursor = conn.cursor()

ids = ''

with open('id.txt', 'r') as f:
    ids = f.readline()

id_list = ids.split('、')[1:-1]


cookie = 'SESSDATA=3e018edc%2C1630047578%2Cc5952*21'
header = {
    'Refer': 'https://space.bilibili.com/',
    'Cookie': cookie,
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'close'
}


def getInfo(mid):
    fansUrl = 'https://api.bilibili.com/x/relation/stat?vmid=%s' % mid
    infoUrl = 'https://api.bilibili.com/x/space/acc/info?mid=%s' % mid
    req = LoopRequest()
    fans = 0
    name = 'null'
    face = 'null'
    loop = 5
    while loop:
        res = req.get(fansUrl, headers=header)
        try:
            if res.status_code == 200:
                res_data = res.content.decode('utf-8')
                data = json.loads(res_data)
                fans = data['data']['follower']
                break
            res.close()
        except Exception as e:
            print(e)
        loop -= 1
        time.sleep(1)

    loop = 5
    while loop:
        res = req.get(infoUrl, headers=header)
        try:
            if res.status_code == 200:
                res_data = res.content.decode('utf-8')
                data = json.loads(res_data)
                name = data['data']['name']
                face = data['data']['face']
                break
            res.close()
        except Exception as e:
            print(e)
        loop -= 1
        time.sleep(1)
    return fans, name, face


def addUser(mid):
    thread_id = threading.currentThread().ident
    db_pool[thread_id] = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test', charset='utf8')
    cur = db_pool[thread_id].cursor()
    print("thread: %s " % thread_id)
    print(mid)
    check = "select * from backend_usersofb where(mid='%s');" % mid
    while True:
        try:
            cur = db_pool[thread_id].cursor()
            cur.execute(check)
            break
        except Exception as e:
            db_pool[thread_id].ping(True)
        time.sleep(3)

    if cur.fetchone() is not None:
        return
    fans, name, face = getInfo(mid)
    insert1 = "insert into backend_usersofb(mid, face, fans, name) values('%s', '%s', %s, '%s');" % (mid, face, fans, name)
    while True:
        try:
            cur = db_pool[thread_id].cursor()
            cur.execute(insert1)
            break
        except Exception:
            db_pool[thread_id].ping(True)
        time.sleep(3)
    print('%s 加入' % mid)
    id_list.append(mid)
    db_pool[thread_id].commit()
    db_pool[thread_id].close()


def getApi(url):
    req = LoopRequest()
    loop = 5
    user_list = []
    while loop:
        res = req.get(url, headers=header)
        try:
            if res.status_code == 200:
                res_data = res.content.decode('utf-8')
                data = json.loads(res_data)
                user_list = data['data']['list']
                break
            res.close()
        except Exception as e:
            print(e)
        loop -= 1
    thread_list = []
    for user in user_list:
        m = threading.Thread(target=addUser, args=[user['mid'],])
        thread_list.append(m)
    for th in thread_list:
        th.start()
    for th in thread_list:
        th.join()
    time.sleep(3)


async def main():
    baseUrl = 'http://api.bilibili.com/x/relation/followings?'
    for id in id_list:
        check = "select mid from backend_usersofb where(mid='%s');" % id
        cursor.execute(check)
        if cursor.fetchone() is None:
            fans, name, face = getInfo(id)
            insert1 = "insert into backend_usersofb(mid, face, fans, name) values('%s', '%s', %s, '%s');" % (id, face, fans, name)
            cursor.execute(insert1)
        for i in range(1, 6):
            params = {
                'vmid': id,
                'order': 'desc',
                'ps': 20,
                'pn': i,
            }
            url = baseUrl + urlencode(params)
            getApi(url)
        conn.commit()
        time.sleep(5)
        print('提交')

asyncio.get_event_loop().run_until_complete(main())
