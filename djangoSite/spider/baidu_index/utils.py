import datetime
from datetime import datetime
from datetime import timedelta
import json
from spider.Utils.loopRequest import LoopRequest
request = LoopRequest()

keywords = ['b站']
"""
传入日期时间（字符串）
"""


def splice_time(start_time):
    begin_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    times = [begin_time.strftime('%Y-%m-%d %H:%M:%S'), ]
    for index in range(1, 24):
        times.append((begin_time + timedelta(hours=index)).strftime('%Y-%m-%d %H:%M:%S'))
    return times


"""
传入日期（字符串）
"""


def splice_day(start_day, end_day):
    begin_date = datetime.strptime(start_day, '%Y-%m-%d')
    ended_date = datetime.strptime(end_day, '%Y-%m-%d')
    dates = []
    while begin_date <= ended_date:
        dates.append(begin_date.strftime('%Y-%m-%d'))
        begin_date = begin_date + timedelta(days=1)
    return dates


def get_key(uniqid, header):
    url = 'http://index.baidu.com/Interface/api/ptbk?uniqid=%s' % uniqid
    html = request.get(url, headers=header).content.decode('utf-8')
    html_data = json.loads(html)
    key = html_data['data']
    return key



def decrypt_func(key, data):
    """
        数据解密方法
    """
    a = key
    i = data
    n = {}
    s = []
    for o in range(len(a)//2):
        n[a[o]] = a[len(a)//2 + o]
    for r in range(len(data)):
        s.append(n[i[r]])
    return ''.join(s).split(',')
