from django.urls import path
from . import views

urlpatterns = [
    path('login', view=views.Login.as_view(), name="login"),
    path('register', view=views.Register.as_view(), name="register"),
    path('GetCrowd', view=views.GetCrowd.as_view(), name="GetCrowd"),
    path('GetBaiduIndex', view=views.GetBaiduIndex.as_view(), name="GetBaiduIndex"),
    path('GetInterest', view=views.GetInterest.as_view(), name="GetInterest")
]