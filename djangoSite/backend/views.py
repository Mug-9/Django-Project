from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

from .models import *

# Create your views here.
def books(request):
    books = [
        {'id': 1, 'title': "python", "price": 89}
    ]
    if request.method == "GET":
        return JsonResponse(books, safe=False)
    else:
        print('post', request.POST)
        print('body', request.body)
        return JsonResponse(books, safe=False)


def login(request):
    if request.method == 'POST':
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')

        if account and password:
            user = User()


def register(request):
    if request.method == 'POST':
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        print(account, password)

        if account and password:
            user = User(account=account, password=password)
            user.save()
            return HttpResponse('注册成功！')
    return HttpResponse('注册失败！')