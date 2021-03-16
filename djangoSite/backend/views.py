
import json
import threading
import time
from datetime import datetime, time
import datetime

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
        account = request.POST.get('account')
        password = request.POST.get('password')
        try:
            user = User.objects.get(account=account)
            if user.password == password:
                name = user.name
                headers = Token.HEADER
                data = {'account': account, 'email': account, 'name': name}
                payloads = {'iss': account, 'iat': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
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
        print(account, password)
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


def inLog(account,operate_type, face_object_type, face_object_id, face_object_msg):
    UserOperator.objects.create(user_account=account, operate_type=operate_type, face_object_type=face_object_type,
                                face_object_id=face_object_id, face_object_msg=face_object_msg)


def comment_info(comment_id):
    if len(comment_id) == 1:
        if comment_id == '1':
            return '图表 百度指数 '
        elif comment_id == '2':
            return '图表 分布人群'
        elif comment_id == '3':
            return '图表 兴趣分布'
        elif comment_id == '4':
            return '图表 百度资讯指数 '
        elif comment_id == '6':
            return '图表 区域分布 '

    else:
        return '视频%s' % comment_id


@method_decorator(csrf_exempt, name='dispatch')
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

    def post(self, request):
        try:
            token = request.POST.get('token')
            type = request.POST.get('type')
            account = Token.decrypt(token.split('.')[1])['iss']
            comment_id = request.POST.get('comment_id')
            if type == 'comment':
                like = request.POST.get('favorite')
                reply = request.POST.get('reply')
                is_like = request.POST.get('is_like')
                Comment = WebComment.objects.filter(user_account=account,comment_id=comment_id)
                if not Comment.exists():
                    WebComment.objects.create(comment_id=comment_id, user_account=account, web_likes=like, web_replys=reply, is_like=is_like)
                else:
                    Comment = WebComment.objects.get(user_account=account,comment_id=comment_id)
                    Comment.web_likes = like
                    Comment.web_replys = reply
                    Comment.is_like = is_like
                    Comment.save()
                print(is_like, is_like == '1')
                if is_like == '1':
                    inLog(account, 'comment', 'comment', comment_id,
                          '点赞 %s' % comment_info(comment_id))
                else:
                    inLog(account, 'comment', 'comment', comment_id,
                          '取消对 %s 的点赞' % comment_info(comment_id))
                info = {'code': 200, 'msg': '点赞成功'}
            elif type == 'reply':
                reply_content = request.POST.get('reply_content')
                reply_id = request.POST.get('reply_id')
                WebReply.objects.create(comment_id=comment_id, user_account=account, reply_id=reply_id, reply_content=reply_content,
                                          reply_like=0, reply_unlike=0)
                inLog(account, 'reply', 'comment',  comment_id, '在%s下进行评论 %s' % (comment_info(comment_id), reply_content))
                info = {'code': 200, 'msg': '评论成功'}
            elif type == 'like' or type == 'unlike' or type == 'dislike' or type == 'undislike':
                like_count = request.POST.get('like_count')
                dislike_count = request.POST.get('dislike_count')
                reply_id = request.POST.get('reply_id')
                is_like = request.POST.get('is_like')
                is_dislike = request.POST.get('is_dislike')
                Reply = WebReply.objects.get(reply_id=reply_id)
                Reply.reply_like = like_count
                Reply.reply_unlike = dislike_count
                Reply.save()
                ulr = UserLikeReply.objects.filter(user_account=account,reply_id=reply_id)
                if not ulr.exists():
                    UserLikeReply.objects.create(reply_id=reply_id, user_account=account,is_like=is_like, is_dislike=is_dislike)
                else:
                    ulr = UserLikeReply.objects.get(user_account=account, reply_id=reply_id)
                    ulr.is_like = is_like
                    ulr.is_dislike = is_dislike
                    ulr.save()
                if type == 'like':
                    inLog(account, 'like', 'reply', reply_id,
                              '点赞了 %s 的评论 %s' % (Reply.user_account, Reply.reply_content))
                elif type == 'unlike':
                    inLog(account, 'unlike', 'reply', reply_id,
                          '取消了 %s 的评论 %s 的点赞' % (Reply.user_account, Reply.reply_content))
                elif type == 'dislike':
                    inLog(account, 'dislike', 'reply', reply_id,
                              '点踩了 %s 的评论 %s' % (Reply.user_account, Reply.reply_content))
                elif type == 'undislike':
                    inLog(account, 'undislike', 'reply', reply_id,
                          '取消了 %s 的评论 %s 的点踩' % (Reply.user_account, Reply.reply_content))
                info = {'code': 200, 'msg': '操作成功'}
            elif type == 'delete':
                reply_id = request.POST.get('reply_id')
                comment_id = request.POST.get('comment_id')
                ulr = UserLikeReply.objects.filter(reply_id=reply_id)
                if ulr.exists():
                    ulr = UserLikeReply.objects.get(reply_id=reply_id)
                    ulr.delete()

                webReqly = WebReply.objects.get(reply_id=reply_id)
                inLog(account, 'delete', 'reply', reply_id,
                          '删除了评论 %s' % (webReqly.reply_content))
                webReqly.delete()
                webComment = WebComment.objects.get(comment_id=comment_id)
                webComment.web_replys -= 1
                webComment.save()
                info = {'code': 200, 'msg': '删除成功'}
        except Exception as e:
            print(e)
            info = {'code': 400, 'message': "出现错误"}
        return JsonResponse(info)


def get_comment(account, bvid):
    comments_info = {}
    comments = WebComment.objects.filter(user_account=account,comment_id=bvid)
    if comments.count() == 0:
        comments_info['web_like'] = 0
        comments_info['web_reply'] = 0
        comments_info['replys'] = []
        comments_info['comment_id'] = bvid
        comments_info['is_like'] = 0
        comments_info['word'] = 'comment'
    else:
        comment = comments[0]
        comments_info['is_like'] = comment.is_like
        comments_info['comment_id'] = comment.comment_id
        comments_info['web_like'] = comment.web_likes
        comments_info['web_reply'] = comment.web_replys
        Replys = WebReply.objects.filter(comment_id=comment.comment_id).order_by('reply_time').reverse()
        reps = []
        for reply in Replys:
            rep = {'reply_id': reply.reply_id, 'msg': reply.reply_content,
                   'user_account': reply.user_account,
                   'like': reply.reply_like, 'dislike': reply.reply_unlike, 'reply_time': (reply.reply_time+datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')}
            user = User.objects.get(account=reply.user_account)
            rep['img'] = user.user_header
            rep['name'] = user.name
            ulr = UserLikeReply.objects.filter(user_account=account, reply_id=rep['reply_id'])
            if not ulr.exists():
                rep['is_like'] = 0
                rep['is_dislike'] = 0
            else:
                ulr = UserLikeReply.objects.get(user_account=account, reply_id=rep['reply_id'])
                rep['is_like'] = ulr.is_like
                rep['is_dislike'] = ulr.is_dislike
            reps.append(rep)
        comments_info['replys'] = reps
        comments_info['word'] = 'comment'
    return comments_info


# 2
class GetCrowd(View):

    def get(self, request):
        account = 'default'
        type = request.GET.get('type')
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_crowd_age()
        results = [result[0], result[1], get_comment(account, '2')]
        res = json.dumps(results)
        return JsonResponse(res, safe=False)

# 1
class GetBaiduIndex(View):

    def get(self, request):
        type = request.GET.get('type')
        days = request.GET.get('days')
        area = request.GET.get('area')
        account = 'default'
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        if type == 'index':
            result = spider.get_baidu_index(days, area)
            results = [result[0], result[1], get_comment(account, '1')]
            res = json.dumps(results)
            return JsonResponse(res, safe=False)
        elif type == 'live':
            result = spider.get_baidu_index_live(area)
            results = [result[0], result[1], get_comment(account, '1')]
            res = json.dumps(results)
            return JsonResponse(res, safe=False)

# 3
class GetInterest(View):

    def get(self, request):
        account = 'default'
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_interest()
        results = [result, get_comment(account, '3')]
        res = json.dumps(results)
        return JsonResponse(res, safe=False)

# 4
class GetFeedIndex(View):

    def get(self, request):
        days = request.GET.get('days')
        area = request.GET.get('area')
        account = 'default'
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_feed_index(days, area)
        results = [result[0], result[1], get_comment(account, '4')]
        res = json.dumps(results)
        return JsonResponse(res, safe=False)

# 5
class GetNewIndex(View):

    def get(self, request):
        days = request.GET.get('days')
        account = 'default'
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.get_new_index(days)
        results = [result[0], result[1], get_comment(account, '4')]
        res = json.dumps(results)
        return JsonResponse(res, safe=False)

# 6
class GetRegion(View):
    def get(self, request):
        days = request.GET.get('days')
        account = 'default'
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        result = spider.spider_region(days)
        results = [result[0], result[1], get_comment(account, 6)]
        res = json.dumps(results)
        return JsonResponse(res, safe=False)


class OnlineList(View):
    def threading_cal(self, video, result, account):
        video_trend = VideosData.objects.filter(bvid=video['bvid']).order_by('dateTime')
        dateTime = []
        view_d, danmaku_d, coin_d, reply_d, share_d, like_d, favorite_d = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [
            0, ]
        view, danmaku, coin, reply, share, like, favorite = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [0, ]
        if video_trend.count() == 0:
            dateTime.append(video['pubdate'])
            dateTime.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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
            video['comment'] = get_comment(account, video['bvid'])
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
        video['comment'] = get_comment(account, video['bvid'])
        result.append(video)

    def get(self, request):
        account = 'default'
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        res = bili.online_list()
        result = []
        th_list = []
        for video in res:
            m = threading.Thread(target=self.threading_cal, args=[video, result, account])
            m.start()
            th_list.append(m)
        for th in th_list:
            th.join()
        return JsonResponse(result, safe=False)


class HotList(View):

    def threading_cal(self, video, result, account):
        video_trend = VideosData.objects.filter(bvid=video['bvid']).order_by('dateTime')
        dateTime = []
        view_d, danmaku_d, coin_d, reply_d, share_d, like_d, favorite_d = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [
            0, ]
        view, danmaku, coin, reply, share, like, favorite = [0, ], [0, ], [0, ], [0, ], [0, ], [0, ], [0, ]
        if video_trend.count() == 0:
            dateTime.append(video['pubdate'])
            dateTime.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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
            video['comment'] = get_comment(account, video['bvid'])
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
        video['comment'] = get_comment(account, video['bvid'])
        result.append(video)

    def get(self, request):
        ps = request.GET.get('ps')
        pn = request.GET.get('pn')
        account = "default"
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        res = bili.hot_list(ps, pn)
        result = []
        th_list = []
        for video in res:
            m = threading.Thread(target=self.threading_cal, args=[video, result, account])
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
                            'archive_like': utils.relieve_num(up.archive_like), 'archive_view': utils.relieve_num(up.archive_view)})
        return JsonResponse(up_list, safe=False)


class GetFansIncre(View):
    def get(self, request):
        Ups = UsersOfB.objects.order_by('fansd_yesterday').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        up_list = {'yesterday': [], 'week': [], 'month': []}
        for up in ups:
            up_list['yesterday'].append({'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid, 'fans_incre': utils.relieve_num(up.fansd_yesterday)})
        Ups = UsersOfB.objects.order_by('fansd_week_ago').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        for up in ups:
            up_list['week'].append(
                {'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid, 'fans_incre': utils.relieve_num(up.fansd_week_ago)})
        Ups = UsersOfB.objects.order_by('fansd_month_ago').reverse()
        pager = Paginator(Ups, 20)
        perpager_data = pager.page(1)
        ups = perpager_data.object_list
        for up in ups:
            up_list['month'].append(
                {'name': up.name, 'fans': utils.relieve_num(up.fans), 'face': up.face, 'mid': up.mid,
                 'fans_incre': utils.relieve_num(up.fansd_month_ago)})
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


class OperatorLog(View):
    def get(self, request):
        token = request.GET.get('token', '')
        account = 'default'
        info = {'code': 400, 'msg': '查找失败'}
        try:
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
            return JsonResponse(info, safe=False)
        print(account)
        Log = UserOperator.objects.filter(user_account=account)
        if Log.count() == 0:
            info = {'code': 201, 'msg': '没有记录'}
            return JsonResponse(info, safe=False)
        else:
            Logs = UserOperator.objects.filter(user_account=account).order_by('operate_time').reverse()
            info = {'code': 200, 'list': []}
            for log in Logs:
                info['list'].append({'msg': log.face_object_msg, 'time': (log.operate_time+datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'), 'type': log.operate_type})
            return JsonResponse(info, safe=False)


class GetFavorite(View):
    def get(self, request):
        token = request.GET.get('token', '')
        account = 'default'
        info = {'code': 400, 'msg': '查找失败'}
        try:
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
            return JsonResponse(info, safe=False)
        favorite = WebComment.objects.filter(user_account=account)
        if favorite.count() == 0:
            info = {'code': 201, 'msg': '没有记录'}
            return JsonResponse(info, safe=False)
        else:
            favorites = WebComment.objects.filter(user_account=account, is_like=1).order_by('like_time').reverse()
            info = {'code': 200, 'list': []}
            for favorite in favorites:
                info['list'].append({'time': (favorite.like_time+datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'), 'msg': comment_info(favorite.comment_id)})
            return JsonResponse(info, safe=False)
