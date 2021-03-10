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
    face = models.CharField(max_length=30, default='None')

    def __str__(self):
        return u'mid: %s' % self.mid


class proxies(models.Model):
    id = models.AutoField(primary_key=True)
    iport = models.CharField(max_length=20)

