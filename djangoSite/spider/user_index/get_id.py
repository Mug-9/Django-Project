import requests
import re, time
import json
from spider.Utils.loopRequest import LoopRequest
from spider.user_index import utils

from lxml import etree


def get_id(name, state):
    name_state = json.loads(state)
    SingleTypeList = 'getSingleTypeList-jump-keyword-%s-search_type-bili_user' % (name)
    people = name_state['flow'][SingleTypeList]['result'][0]
    name_id = people['mid']
    print(name, name_id)
    with open('id.txt', 'a') as f:
        f.write(str(name_id) + '、')
    f.close()


request = LoopRequest()
users = ""
with open('name.txt', 'r') as f:
    users = f.readline()
name_list = users.split('、')[:-1]
with open('id.txt', 'w') as f:
    f.write('、')
f.close()




for name in name_list:
    print(name)
    url = utils.get_url(name)
    print(url)
    while True:
        res = request.get(url)
        print(res.headers)
        res_data = res.content.decode('utf-8')

        try:
            name_state = re.findall(r'<script>window.__INITIAL_STATE__=(.*?);\(function\(\)', res_data, re.S)[0]
            get_id(name, name_state)
            break
        except Exception as e:
            print(request.proxies.header)
            request.count = 0
        time.sleep(1)


