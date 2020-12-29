import spider_online_num
import datetime
import threading

time_list = [0, 15, 30, 45, 60]


class onTime(object):
    def __init__(self):
        self.time_dis = 0
        self.spider = spider_online_num.SpiderOnlineNumber()

    def cal_dis(self):
        now_time = datetime.datetime.now()
        now_minute = now_time.time().minute
        next_day = now_time.date().day
        next_month = now_time.date().month
        next_year = now_time.date().year
        next_hour = now_time.time().hour
        next_minute = 0
        for time in time_list:
            if now_minute < time:
                next_minute = time
                break
        if next_minute == 60:
            next_time = now_time + datetime.timedelta(hours=+1)
            next_day = next_time.date().day
            next_month = next_time.date().month
            next_year = next_time.date().year
            next_hour = next_time.time().hour
            next_minute = 00
        next_time = datetime.datetime.strptime(str(next_year)+'-'+str(next_month)+'-'+str(next_day)
                                               +' '+str(next_hour)+':'+str(next_minute)+':00', "%Y-%m-%d %H:%M:%S")
        print("下一次爬取时间 %s " % next_time)
        self.time_dis = (next_time - now_time).total_seconds()

    def spider_number(self):
        self.spider.run()
        self.run()
        # threading.Timer(1800, self.spider_number).start()

    def run(self):
        self.cal_dis()
        threads = []
        thread = threading.Timer(self.time_dis, self.spider_number)
        threads.append(thread)
        thread.start()
        thread.join()


if __name__ == '__main__':
    ontime = onTime()
    ontime.run()
