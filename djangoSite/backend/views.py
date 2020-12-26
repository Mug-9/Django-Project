from django.shortcuts import render
from django.http.response import  JsonResponse

# Create your views here.

def books(request):
    books = [
        {'id': 1, 'title': "python", "price": 89}
    ]
    return JsonResponse(books, safe=False)
