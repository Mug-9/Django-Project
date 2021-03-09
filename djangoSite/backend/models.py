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


class OnlineNumber(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    number = models.IntegerField()

    def __str__(self):
        return u'time: %s' % self.time


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

