import json
import time
from django.http.response import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .models import *
from spider.baidu_index import spider_baidu
from backend.backend_utils import Tokens

Token = Tokens.Token()
spider = spider_baidu.SpiderBaidu()


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def post(self, request):
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        try:
            user = User.objects.get(account=account)
            if user.password == password:
                headers = Token.HEADER
                print(headers)
                data = {'account': account, 'email': account}
                payloads = {'iss': account, 'iat': time.time()}
                generated_token = Token.get_token(headers, payloads)
                info = {'token': generated_token, 'code': 200, 'data': data, 'message': "登录成功"}
                return JsonResponse(info)
            else:
                info = {'message': "密码错误"}
                return JsonResponse(info)
        except Exception as e:
            print(e, '不存在')
            info = {'message': "账户不存在"}
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
        try:
            token = request.GET.get('token')
            account = Token.decrypt(token.split('.')[1])['iss']
        except Exception as e:
            print(e)
        if type == 'index':
            result = spider.get_baidu_index(days)
            res = json.dumps(result)
            return JsonResponse(res, safe=False)
        elif type == 'live':
            result = spider.get_baidu_index_live()
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