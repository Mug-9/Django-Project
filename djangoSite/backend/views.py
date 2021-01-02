import hashlib
import time

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers, signing
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.middleware.csrf import get_token


# Create your views here.
def books(request):
    book = ['abcd']
    return HttpResponse('books')


HEADER = {
    'type': 'JWT',
    'alg': 'HS256'
}


def Encrypt(value):
    data = signing.dumps(value)
    data = signing.b64_encode(data.encode()).decode()
    return data


def Decrypt(value):
    data = signing.b64_decode(value.encode()).decode()
    data = signing.loads(data)
    return data


def Token(headers, payloads):
    header = Encrypt(headers)
    payload = Encrypt(payloads)
    md5 = hashlib.md5()
    md5.update(("%s.%s" % (header, payload)).encode())
    signature = md5.hexdigest()
    token = "%s.%s.%s" % (header, payload, signature)
    return token

# @csrf_exempt
# def login(request):
#     if request.method == "POST":
#         account = request.POST.get('account', '')
#         password = request.POST.get('password', '')
#         try:
#             user = User.objects.get(account=account)
#             if user.password == password:
#                 headers = HEADER
#                 data = {'account': account, 'email': account}
#                 payloads = {'iss': account, 'iat': time.time()}
#                 token = Token(headers, payloads)
#                 info = {'token': token, 'code': 200, 'data': data, 'message': "登录成功"}
#                 return JsonResponse(info)
#             else:
#                 info = {'message': "密码错误"}
#                 return JsonResponse(info)
#         except Exception as e:
#             info = {'message': "账户不存在"}
#             return JsonResponse(info)
#     else:
#         info = {'message': "错误地址"}
#         return HttpResponse(info)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        response = HttpResponse()
        try:
            user = User.objects.get(account=account)
            if user.password == password:
                response.content = "登录成功"
                request.session['login'] = account
                request.session['isLogin'] = True
                response.set_cookie('login', account+','+password, path='/login', max_age=24*60*60)
                response['Access-Control-Allow-Origin'] = 'http://localhost:8080/'
                response['Access-Control-Allow-Credentials'] = "true"
                return response
            else:
                return HttpResponse('密码错误')
        except Exception as e:
            print(e)
            return HttpResponse("账户不存在")
    else:
        return HttpResponse("GET")


@csrf_exempt
def register(request):
    if request.method == 'POST':
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
    return HttpResponse('注册失败!')


def online_number(request):
    if request.method == 'GET':
        date = request.GET.get('date', '')
        print(date)
        count = OnlineNumber.objects.filter(date=date).count()
        print(count)
        numbers = None
        if count == 0:
            numbers = []
        elif count == 1:
            numbers = [OnlineNumber.objects.filter(date=date)]
        else:
            numbers = OnlineNumber.objects.filter(date=date)
        return JsonResponse(serializers.serialize("json", numbers), safe=False)