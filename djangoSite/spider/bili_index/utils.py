import json
import re
import time


def get_online_list(response):
    links = re.findall(r'<script>window.__INITIAL_STATE__=(.*?);\(function\(\)', response, re.S)[0]
    links = json.loads(links)
    return parse_data(links['onlineList'])


def get_hot_list(response):
    res = json.loads(response)
    list = res['data']['list']
    return parse_data(list)


def parse_data(response):
    if not isinstance(response, list):
        response['ctime'] = parse_time(response['ctime'])
        response['pubdate'] = parse_time(response['pubdate'])
        response['duration'] = cal_time(response['duration'])
    else:
        for item in response:
            item['ctime'] = parse_time(item['ctime'])
            item['pubdate'] = parse_time(item['pubdate'])
            item['duration'] = cal_time(item['duration'])
            item['stat']['coin'] = relieve_num(item['stat']['coin'])
            item['stat']['danmaku'] = relieve_num(item['stat']['danmaku'])
            item['stat']['favorite'] = relieve_num(item['stat']['favorite'])
            item['stat']['like'] = relieve_num(item['stat']['like'])
            item['stat']['reply'] = relieve_num(item['stat']['reply'])
            item['stat']['share'] = relieve_num(item['stat']['share'])
            item['stat']['view'] = relieve_num(item['stat']['view'])
    return response


def relieve_num(num):
    n = int(int(num) / 100000000)
    last = int(num) % 100000000
    head = int(last / 10000)
    tail = last % 10000
    if n > 0:
        return "%s.%s亿" % (n, int(last / 1000000))
    elif head > 0:
        return "%s.%s万" % (head, int(tail / 100))
    else:
        return tail


def parse_time(sec):
    time_local = time.localtime(sec)
    return time.strftime('%Y-%m-%d %H:%M:%S', time_local)


def cal_time(sec):
    hour = int(sec / 3600)
    sec %= 3600
    min = int(sec / 60)
    sec %= 60
    return "%s:%s:%s" % (hour, min, sec)


