from django.urls import path
from . import views

urlpatterns = [
    path('books', view = views.books, name="books")
]