import datetime
from datetime import datetime
from datetime import timedelta
import json
from urllib.parse import urlencode
from spider.Utils.loopRequest import LoopRequest
from spider.baidu_index import utils


class SpiderBaidu(object):

    def __init__(self):
        self.kind = ['all', 'pc', 'wise']
        self.cookies = ""
        self.request = LoopRequest()
        self.type = {}
        self.header = {}
        self.init()

    def init(self):
        self.cookies = "BDUSS=2ptTjI3OEpYMVNpOVpQY0ZCT2Ftd1NCb0tWdlhTWXM4RVFxMmtSSm5QWklXaHRnRVFBQUFBJCQAAAAAAAAAAAEAAAAelm82tcu66sHBusPRp8n6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEjN819IzfNfc"
        self.type['crowd'] = 'https://index.baidu.com/api/SocialApi/baseAttributes?'
        self.type['index'] = 'https://index.baidu.com/api/SearchApi/index?'
        self.type['live'] = 'https://index.baidu.com/api/LiveApi/getLive?'
        self.type['interest'] = 'https://index.baidu.com/api/SocialApi/interest?'
        self.header = {
            'Host': 'index.baidu.com',
            'Cookie': self.cookies
        }

    def get_crowd_age(self):
        request_args = {
            'wordlist[]': utils.keywords[0]
        }
        url = self.type['crowd'] + urlencode(request_args)
        response = self.request.get(url=url, headers=self.header).content.decode('utf-8')
        response_data = json.loads(response)
        results = response_data['data']['result']
        sex_tgi, sex_b, sex_all = [], [], []
        age_tgi, age_b, age_all, age_desc = [], [], [], []
        index = 0
        for result in results:
            for sex in result['gender']:
                if index == 0:
                    sex_tgi.append(sex['tgi'])
                    sex_b.append(sex['rate'])
                else:
                    sex_all.append(sex['rate'])
            for age in result['age']:
                if index == 0:
                    age_tgi.append(age['tgi'])
                    age_b.append(age['rate'])
                    age_desc.append(age['desc'])
                else:
                    age_all.append(age['rate'])

            index += 1
        sex_dict = {'b': sex_b, 'all': sex_all, 'tgi': sex_tgi, 'desc': ['女', '男']}
        age_dict = {'b': age_b, 'all': age_all, 'tgi': age_tgi, 'desc': age_desc}
        return age_dict, sex_dict

    def get_baidu_index(self, days=7):
        word_list = [
            [{'name': keyword, 'wordType': 1} for keyword in utils.keywords]
        ]
        request_args = {
            'area': 0,
            'word': json.dumps(word_list),
            'days': days,
        }
        url = self.type['index'] + urlencode(request_args)
        response = self.request.get(url=url, headers=self.header).content.decode('utf-8')
        response_data = json.loads(response)
        uniqid = response_data['data']['uniqid']
        encrypt_data = []

        for single_data in response_data['data']['userIndexes']:
            encrypt_data.append(single_data)
        general_data = []
        for single_data in response_data['data']['generalRatio']:
            general_data.append(single_data)
        general_data = general_data[0]
        general_data['word'] = "general"

        key = utils.get_key(uniqid, self.header)
        decrypt_data = []
        start_date = ""
        end_date = ""
        data_dict = {}
        for data in encrypt_data:
            for kind in self.kind:
                if 'data' in data[kind]:
                    start_date = data[kind]['startDate']
                    end_date = data[kind]['endDate']
                    data[kind]['data'] = utils.decrypt_func(key, data[kind]['data'])
                    data_dict[kind] = data[kind]['data']
        dates = utils.splice_day(start_date, end_date)
        data_dict['date'] = dates
        decrypt_data.append(data_dict)
        data_dict['word'] = 'index'
        decrypt_data.append(general_data)
        return decrypt_data

    def get_baidu_index_live(self):
        word_list = [
            [{'name': keyword, 'wordType': 1} for keyword in utils.keywords]
        ]
        print(word_list)
        request_args = {
            'area': 0,
            'word': json.dumps(word_list),
        }
        print(request_args)
        url = self.type['live'] + urlencode(request_args)
        response = self.request.get(url=url, headers=self.header).content.decode('utf-8')
        response_data = json.loads(response)
        uniqid = response_data['data']['uniqid']
        encrypt_data = []
        for single_data in response_data['data']['result']:
            encrypt_data.append(single_data)
        key = utils.get_key(uniqid, self.header)
        decrypt_data = []
        index_data = encrypt_data[0]['index'][0]
        data_dict = {}
        for kind in index_data:
            if kind[0] == '_':
                data = utils.decrypt_func(key, index_data[kind])
                data_dict[kind[1:]] = data
            else:
                times = utils.splice_time(index_data[kind].split('|')[0])
                data_dict['date'] = times
        data_dict['word'] = 'index'
        decrypt_data.append(data_dict)
        return decrypt_data

    def get_interest(self):
        request_args = {
            'wordlist[]': utils.keywords[0]
        }
        url = self.type['interest'] + urlencode(request_args)
        response = self.request.get(url, headers = self.header).content.decode('utf-8')
        response_data = json.loads(response)
        results = response_data['data']['result']
        interest_b, interest_all, tgi, desc = [], [], [], []
        index = 0
        for result in results:
            if index == 0:
                for interest in result['interest']:
                    desc.append(interest['desc'])
                    tgi.append(interest['tgi'])
                    interest_b.append(interest['rate'])
            else:
                for interest in result['interest']:
                    interest_all.append(interest['rate'])
            index += 1
        interest_dict = {'b': interest_b, 'all': interest_all, 'tgi': tgi, 'desc': desc, 'word': 'interest'}
        return interest_dict

    def run(self):
        self.get_interest()


if __name__ == "__main__":
    spider = SpiderBaidu()
    spider.run()
