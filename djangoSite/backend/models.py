from django.db import models


# Create your models here.
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=20, default="account")
    password = models.CharField(max_length=20)
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

