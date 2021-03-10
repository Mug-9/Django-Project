from django.urls import path
from . import views

urlpatterns = [
    path('login', view=views.Login.as_view(), name="login"),
    path('register', view=views.Register.as_view(), name="register"),
    path('GetCrowd', view=views.GetCrowd.as_view(), name="GetCrowd"),
    path('GetBaiduIndex', view=views.GetBaiduIndex.as_view(), name="GetBaiduIndex"),
    path('GetInterest', view=views.GetInterest.as_view(), name="GetInterest"),
    path('GetFeedIndex', view=views.GetFeedIndex.as_view(), name="GetFeedIndex"),
    path('GetNewIndex', view=views.GetNewIndex.as_view(), name="GetNewIndex"),
    path('GetRegion', view=views.GetRegion.as_view(), name="GetRegion"),
    path('OnlineList', view=views.OnlineList.as_view(), name="OnlineList"),
    path('HotList', view=views.HotList.as_view(), name="HotListList"),
    path('GetInfo', view=views.getInfo.as_view(), name="getInfo"),
    path('UpdateInfo', view=views.UpdateInfo.as_view(), name="updateInfo"),
    path('GetUpInfo', view=views.GetUpInfo.as_view(), name="GetUpInfo"),

]