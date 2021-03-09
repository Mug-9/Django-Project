import json
import time
from Utils import user_agent_list
import MySQLdb as md
import requests

proxies_list = []


def check_iport(iport):
    print(iport)
    proxy = {
        'http': 'http://%s' % iport,
        'https': 'http://%s' % iport
    }
    header=user_agent_list.getheaders()
    header['Connection'] = 'close'
    try:
        res = requests.get('https://httpbin.org/get', headers=header, proxies=proxy, timeout=7)
        if res.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":

    conn = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test')
    cursor = conn.cursor()

    while True:
        port_url = 'http://127.0.0.1:5000/proxy'
        res = requests.get(port_url).content.decode('utf-8')
        proxies_list = json.loads(res)
        for iport in proxies_list:
            select = "select id from backend_proxies where iport=\'%s\';" % iport
            cursor.execute(select)
            if cursor.fetchone() is not None:
                continue
            if check_iport(iport):
                insert = "insert into backend_proxies(iport) values(\'%s\');" % iport
                print('%s 添加' % iport)
                cursor.execute(insert)
            time.sleep(5)

        select = "select * from backend_proxies"
        cursor.execute(select)
        rets = cursor.fetchall()
        for ret in rets:
            iport = ret[1]
            if not check_iport(iport):
                print('%s 删除' % iport)
                delete = "delete from backend_proxies where iport=\'%s\'" % iport
                cursor.execute(delete)

        conn.commit()
        print('等待20分钟')
        time.sleep(20*60)
