from django.urls import path
from . import views

urlpatterns = [
    path('books', view=views.books, name="books"),
    path('login', view=views.login, name="login"),
    path('register', view=views.register, name="register"),
]