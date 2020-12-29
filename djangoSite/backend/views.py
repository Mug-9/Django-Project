from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        except Exception as e:
            print(e)
            return HttpResponse("账户不存在")
    else:
        return HttpResponse('无效地址')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if email and password:
            try:
                User.objects.get(email=email)
                return HttpResponse('账号已存在!')
            except Exception as e:
                print(e)
                user = User(email=email, password=password)
                user.save()
                return HttpResponse('注册成功!')
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