from django.urls import path
from . import views

urlpatterns = [
    path('login', view=views.login, name="login"),
    path('register', view=views.register, name="register"),
    path('online_number', view=views.online_number, name="online_number"),
    path('books', view=views.books, name="books")
]