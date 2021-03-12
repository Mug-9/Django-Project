from django.db import models
# Create your models here.
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=20, default="account")
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20, default='name')
    email = models.EmailField()
    user_header = models.ImageField(upload_to='media/headers/', default='media/headers/header.png')

    def __str__(self):
        return u'email: %s' % self.email


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class VideosData(models.Model):
    id = models.AutoField(primary_key=True)
    bvid = models.CharField(max_length=20,  default='None')
    dateTime = models.DateTimeField(default=timezone.now)
    view = models.IntegerField(default=0)
    coin = models.IntegerField(default=0)
    danmaku = models.IntegerField(default=0)
    reply = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    love = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)

    def __str__(self):
        return u'time: %s' % self.dateTime


class UsersOfB(models.Model):
    user_b_id = models.AutoField(primary_key=True)
    mid = models.CharField(max_length=20,  default='None', unique= True)
    name = models.CharField(max_length=20, default='None')
    fans = models.IntegerField(default=0)
    fans_yesterday = models.IntegerField(default=0)
    fansd_yesterday = models.IntegerField(default=0)
    fans_week_ago = models.IntegerField(default=0)
    fansd_week_ago = models.IntegerField(default=0)
    fans_month_ago = models.IntegerField(default=0)
    fansd_month_ago = models.IntegerField(default=0)
    face = models.CharField(max_length=30, default='None')
    archive_view = models.IntegerField(default=0)
    archive_like = models.IntegerField(default=0)
    video_count = models.IntegerField(default=0)
    video_count_week_ago = models.IntegerField(default=0)
    videod_week_ago = models.IntegerField(default=0)
    video_count_month_ago = models.IntegerField(default=0)
    videod_month_ago = models.IntegerField(default=0)

    def __str__(self):
        return u'mid: %s' % self.mid


class UserTimeInfo(models.Model):
    user_time_info_id = models.AutoField(primary_key=True)
    mid = models.CharField(max_length=20, default='None')
    fans = models.IntegerField(default=0)
    archive_view = models.IntegerField(default=0)
    archive_like = models.IntegerField(default=0)


class proxies(models.Model):
    id = models.AutoField(primary_key=True)
    iport = models.CharField(max_length=20)

