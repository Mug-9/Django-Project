from django.shortcuts import render
from django.http.response import  JsonResponse

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
