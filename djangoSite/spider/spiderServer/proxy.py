import json
import time
import user_agent_list
import MySQLdb as md
import requests

proxies_list = []


def check_iport(iport):
    print(iport)
    loop = 10
    while loop:
        proxy = {
            'http': 'http://%s' % iport,
            'https': 'http://%s' % iport
        }
        header=user_agent_list.getheaders()
        header['Connection'] = 'close'
        try:
            res = requests.get('https://httpbin.org/get', headers=header, proxies=proxy, timeout=7)
            if res.status_code == 200:
                res.close()
                return True
            res.close()
        except Exception as e:
            print(e)
        loop -= 1
        time.sleep(5)
    return False


def check_conn(conn):
    while True:
        try:
            conn.ping(True)
            break
        except Exception as e:
            print(e)
            conn = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test',
                             charset='utf8')
        time.sleep(5)


if __name__ == "__main__":

    while True:
        conn = md.connect(host='123.56.252.111', port=3306, user='root', passwd='123456', db='test')
        check_conn(conn)
        cursor = conn.cursor()
        port_url = 'http://127.0.0.1:5000/proxy'
        res = requests.get(port_url).content.decode('utf-8')
        proxies_list = json.loads(res)['proxies']
        print(proxies_list)
        for iport in proxies_list:
            select = "select id from backend_proxies where iport=\'%s\';" % iport
            check_conn(conn)
            cursor = conn.cursor()
            cursor.execute(select)
            if cursor.fetchone() is not None:
                continue
            if check_iport(iport):
                insert = "insert into backend_proxies(iport) values(\'%s\');" % iport
                print('%s 添加' % iport)
                check_conn(conn)
                cursor = conn.cursor()
                cursor.execute(insert)
                conn.commit()
            time.sleep(5)

        select = "select * from backend_proxies"
        check_conn(conn)
        cursor = conn.cursor()
        cursor.execute(select)
        rets = cursor.fetchall()
        for ret in rets:
            iport = ret[1]
            if not check_iport(iport):
                print('%s 删除' % iport)
                delete = "delete from backend_proxies where iport=\'%s\'" % iport
                check_conn(conn)
                cursor = conn.cursor()
                cursor.execute(delete)
                conn.commit()

        check_conn(conn)
        cursor = conn.cursor()
        conn.close()
        print('等待30分钟')
        time.sleep(30*60)
