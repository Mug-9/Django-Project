
import json
import threading

from datetime import datetime, time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import QueryDict
from django.http.response import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .models import *
from spider.baidu_index import spider_baidu
from spider.bili_index import spider_bili
from spider.bili_index import utils
from backend.backend_utils import Tokens

Token = Tokens.Token()
spider = spider_baidu.SpiderBaidu()
bili = spider_bili.SpiderBili()


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def post(self, request):
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        try:
            user = User.objects.get(account=account)
            if user.password == password:
                name = user.name
                headers = Token.HEADER
                data = {'account': account, 'email': account, 'name': name}
                payloads = {'iss': account, 'iat': time.time()}
                generated_token = Token.get_token(headers, payloads)
                info = {'token': generated_token, 'code': 200, 'data': data, 'message': "登录成功", }
                return JsonResponse(info)
            else:
                info = {'message': "密码错误"}
                return JsonResponse(info)
        except Exception as e:
            print(e, '不存在')
            info = {'message': "账户不存在"}
            return JsonResponse(info)


@method_decorator(csrf_exempt, name='dispatch')
class getInfo(View):
    def get(self, request):
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
            user = User.objects.get(account=account)
            data = {'account': account, 'email': user.email, 'password': user.password, 'name': user.name}
            info = {'code': 200, 'data': data}
            return JsonResponse(info)
        except Exception as e:
            info = {'message': "没有token"}
            return JsonResponse(info)


@method_decorator(csrf_exempt, name='dispatch')
class Register(View):
    def post(self, request):
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        if account and password:
            try:
                User.objects.get(account=account)
                return HttpResponse('账号已存在!')
            except Exception as e:
                print(e)
                user = User(account=account, password=password, email=account)
                user.save()
                response = HttpResponse("注册成功!")
                return response
        else:
            return HttpResponse('无效数据!')

    def get(self, request):
        pass

    def put(self, request):
        pass


class UpdateInfo(View):
    def get(self, request):
        try:
            data = request.GET.get('data')
            data = eval(data)
            nickName = data['nickName']
            account = data['account']
            password = data['password']
            email = data['email']
            try:
                user = User.objects.get(account=account)
                user.name = nickName
                user.password = password
                user.email = email
                user.save()
                Info = {'code': 200, 'message': '更新成功'}
                return JsonResponse(Info)
            except Exception as e:
                print(e)
                Info = {'code': 400, 'message': '更新失败'}
                return JsonResponse(Info)
        except Exception as e:
            print(e)
            info = {'code': 400, 'message': "出现错误"}
            return JsonResponse(info)

class GetCrowd(View):

    def get(self, request):
        type = request.GET.get('type')
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_crowd_age()
        res = json.dumps(result)
        return JsonResponse(res, safe=False)


class GetBaiduIndex(View):
    def get(self, request):
        type = request.GET.get('type')
        days = request.GET.get('days')
        area = request.GET.get('area')
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        if type == 'index':
            result = spider.get_baidu_index(days, area)
            res = json.dumps(result)
            return JsonResponse(res, safe=False)
        elif type == 'live':
            result = spider.get_baidu_index_live(area)
            res = json.dumps(result)
            return JsonResponse(res, safe=False)


class GetInterest(View):
    def get(self, request):
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_interest()
        res = json.dumps(result)
        return JsonResponse(res, safe=False)


class GetFeedIndex(View):
    def get(self, request):
        days = request.GET.get('days')
        area = request.GET.get('area')
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_feed_index(days, area)
        res = json.dumps(result)
        return JsonResponse(res, safe=False)


class GetNewIndex(View):
    def get(self, request):
        days = request.GET.get('days')
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_new_index(days)
        res = json.dumps(result)
        return JsonResponse(res, safe=False)


class GetRegion(View):
    def get(self, request):
        days = request.GET.get('days')
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.spider_region(days)
        res = json.dumps(result)
        return JsonResponse(res, safe=False)


class OnlineList(View):
    def threading_cal(self, video, result):
        video_trend = VideosData.objects.filter(bvid=video['bvid']).order_by('dateTime')
        dateTime = []
        view_d, danmaku_d, coin_d, reply_d, share_d, like_d, favorite_d = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [
            0, ]
        view, danmaku, coin, reply, share, like, favorite = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [0, ]
        if video_trend.count() == 0:
            dateTime.append(video['pubdate'])
            dateTime.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            coin_d.append(video['stat']['coin'])
            view_d.append(video['stat']['view'])
            danmaku_d.append(video['stat']['danmaku'])
            reply_d.append(video['stat']['reply'])
            share_d.append(video['stat']['share'])
            like_d.append(video['stat']['like'])
            favorite_d.append(video['stat']['coin'])
            view.append(video['stat']['view'])
            danmaku.append(video['stat']['danmaku'])
            coin.append(video['stat']['coin'])
            reply.append(video['stat']['reply'])
            share.append(video['stat']['share'])
            like.append(video['stat']['like'])
            favorite.append(video['stat']['favorite'])
            echarts_data = {
                'coin_d': coin_d,
                'view_d': view_d,
                'danmaku_d': danmaku_d,
                'reply_d': reply_d,
                'share_d': share_d,
                'like_d': like_d,
                'favorite_d': favorite_d,
                'dateTime': dateTime,
                'coin': coin,
                'view': view,
                'danmaku': danmaku,
                'reply': reply,
                'share': share,
                'like': like,
                'favorite': favorite,
            }
            video['echarts_data'] = echarts_data
            result.append(video)
            return
        dateTime.append(str(video_trend[0].dateTime)[:-6])
        for i in range(1, len(video_trend)):
            coin_d.append(video_trend[i].coin - video_trend[i - 1].coin)
            view_d.append(video_trend[i].view - video_trend[i - 1].view)
            danmaku_d.append(video_trend[i].danmaku - video_trend[i - 1].danmaku)
            reply_d.append(video_trend[i].reply - video_trend[i - 1].reply)
            share_d.append(video_trend[i].share - video_trend[i - 1].share)
            like_d.append(video_trend[i].love - video_trend[i - 1].love)
            favorite_d.append(video_trend[i].favorite - video_trend[i - 1].favorite)
            dateTime.append(str(video_trend[i].dateTime)[:-6])
            view.append(video_trend[i].view)
            danmaku.append(video_trend[i].danmaku)
            coin.append(video_trend[i].coin)
            reply.append(video_trend[i].reply)
            share.append(video_trend[i].share)
            like.append(video_trend[i].love)
            favorite.append(video_trend[i].favorite)
        echarts_data = {
            'coin_d': coin_d,
            'view_d': view_d,
            'danmaku_d': danmaku_d,
            'reply_d': reply_d,
            'share_d': share_d,
            'like_d': like_d,
            'favorite_d': favorite_d,
            'dateTime': dateTime,
            'coin': coin,
            'view': view,
            'danmaku': danmaku,
            'reply': reply,
            'share': share,
            'like': like,
            'favorite': favorite,
        }
        video['echarts_data'] = echarts_data
        result.append(video)


    def get(self, request):
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        res = bili.online_list()
        result = []
        th_list = []
        for video in res:
            m = threading.Thread(target=self.threading_cal, args=[video, result])
            m.start()
            th_list.append(m)
        for th in th_list:
            th.join()
        return JsonResponse(result, safe=False)


class HotList(View):
    def threading_cal(self, video, result):
        video_trend = VideosData.objects.filter(bvid=video['bvid']).order_by('dateTime')
        dateTime = []
        view_d, danmaku_d, coin_d, reply_d, share_d, like_d, favorite_d = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [
            0, ]
        view, danmaku, coin, reply, share, like, favorite = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [0, ]
        if video_trend.count() == 0:
            dateTime.append(video['pubdate'])
            dateTime.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            coin_d.append(video['stat']['coin'])
            view_d.append(video['stat']['view'])
            danmaku_d.append(video['stat']['danmaku'])
            reply_d.append(video['stat']['reply'])
            share_d.append(video['stat']['share'])
            like_d.append(video['stat']['like'])
            favorite_d.append(video['stat']['coin'])
            view.append(video['stat']['view'])
            danmaku.append(video['stat']['danmaku'])
            coin.append(video['stat']['coin'])
            reply.append(video['stat']['reply'])
            share.append(video['stat']['share'])
            like.append(video['stat']['like'])
            favorite.append(video['stat']['favorite'])
            echarts_data = {
                'coin_d': coin_d,
                'view_d': view_d,
                'danmaku_d': danmaku_d,
                'reply_d': reply_d,
                'share_d': share_d,
                'like_d': like_d,
                'favorite_d': favorite_d,
                'dateTime': dateTime,
                'coin': coin,
                'view': view,
                'danmaku': danmaku,
                'reply': reply,
                'share': share,
                'like': like,
                'favorite': favorite,
            }
            video['echarts_data'] = echarts_data
            result.append(video)
            return
        dateTime.append(str(video_trend[0].dateTime)[:-6])
        for i in range(1, len(video_trend)):
            coin_d.append(video_trend[i].coin - video_trend[i - 1].coin)
            view_d.append(video_trend[i].view - video_trend[i - 1].view)
            danmaku_d.append(video_trend[i].danmaku - video_trend[i - 1].danmaku)
            reply_d.append(video_trend[i].reply - video_trend[i - 1].reply)
            share_d.append(video_trend[i].share - video_trend[i - 1].share)
            like_d.append(video_trend[i].love - video_trend[i - 1].love)
            favorite_d.append(video_trend[i].favorite - video_trend[i - 1].favorite)
            dateTime.append(str(video_trend[i].dateTime)[:-6])
            view.append(video_trend[i].view)
            danmaku.append(video_trend[i].danmaku)
            coin.append(video_trend[i].coin)
            reply.append(video_trend[i].reply)
            share.append(video_trend[i].share)
            like.append(video_trend[i].love)
            favorite.append(video_trend[i].favorite)
        echarts_data = {
            'coin_d': coin_d,
            'view_d': view_d,
            'danmaku_d': danmaku_d,
            'reply_d': reply_d,
            'share_d': share_d,
            'like_d': like_d,
            'favorite_d': favorite_d,
            'dateTime': dateTime,
            'coin': coin,
            'view': view,
            'danmaku': danmaku,
            'reply': reply,
            'share': share,
            'like': like,
            'favorite': favorite,
        }
        video['echarts_data'] = echarts_data
        result.append(video)

    def get(self, request):
        ps = request.GET.get('ps')
        pn = request.GET.get('pn')
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        res = bili.hot_list(ps, pn)
        result = []
        th_list = []
        for video in res:
            m = threading.Thread(target=self.threading_cal, args=[video, result])
            m.start()
            th_list.append(m)
        for th in th_list:
            th.join()
        return JsonResponse(result, safe=False)


class GetUpInfo(View):
    def get(self, request):
        ps = request.GET.get('ps', 1)
        pn = request.GET.get('pn', 20)
        n = int(ps)
        Ups = UsersOfB.objects.order_by('fans').reverse()
        pager = Paginator(Ups, pn)
        try:
            perpger_data = pager.page(n)
        except PageNotAnInteger:
            perpager_data = pager.page(1)
        except EmptyPage:
            perpager_data = pager.page(pager.num_pages)
        ups = perpger_data.object_list
        up_list = []
        for up in ups:
            up_list.append({'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid,'video_count': up.video_count,
                            'archive_like': up.archive_like, 'archive_view': up.archive_view})
        return JsonResponse(up_list, safe=False)


class GetFansIncre(View):
    def get(self, request):
        Ups = UsersOfB.objects.order_by('fansd_yesterday').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        up_list = {'yesterday': [], 'week': [], 'month': []}
        for up in ups:
            up_list['yesterday'].append({'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid, 'fans_incre': up.fansd_yesterday})
        Ups = UsersOfB.objects.order_by('fansd_week_ago').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        for up in ups:
            up_list['week'].append(
                {'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid, 'fans_incre': up.fansd_week_ago})
        Ups = UsersOfB.objects.order_by('fansd_month_ago').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        for up in ups:
            up_list['month'].append(
                {'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid,
                 'fans_incre': up.fansd_month_ago})
        return JsonResponse(up_list, safe=False)


class GetVideoIncre(View):
    def get(self, request):
        Ups = UsersOfB.objects.order_by('videod_week_ago').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        up_list = {'week': [],  'month': []}
        for up in ups:
            up_list['week'].append({'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid, 'video_incre': up.videod_week_ago})
        Ups = UsersOfB.objects.order_by('videod_month_ago').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        for up in ups:
            up_list['month'].append(
                {'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid, 'video_incre': up.videod_month_ago})
        return JsonResponse(up_list, safe=False)
