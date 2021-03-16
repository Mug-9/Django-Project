from django.db import models
# Create your models here.
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=20, default="account")
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20, default='name')
    email = models.EmailField()
    user_header = models.CharField(max_length=100)

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


class WebComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment_id = models.CharField(max_length=20, default='None')
    user_account = models.CharField(max_length=20, default="None")
    web_likes = models.IntegerField(default=0)
    web_replys = models.IntegerField(default=0)
    is_like = models.BooleanField(default=0)
    like_time = models.DateTimeField('修改日期', auto_now=True)

    def __str__(self):
        return u'comment_id: %s' % self.comment_id


class WebReply(models.Model):
    id = models.AutoField(primary_key=True)
    comment_id = models.CharField(max_length=20, default='None')
    reply_id = models.CharField(max_length=50, default='None')
    reply_content = models.CharField(max_length=100, default='None')
    user_account = models.CharField(max_length=20, default='None')
    reply_like = models.IntegerField(default=0)
    reply_unlike = models.IntegerField(default=0)
    reply_time = models.DateTimeField(default=timezone.now)


class UserLikeReply(models.Model):
    id = models.AutoField(primary_key=True)
    reply_id = models.CharField(max_length=50, default='None')
    user_account = models.CharField(max_length=20, default='None')
    is_like = models.BooleanField(default=0)
    is_dislike = models.BooleanField(default=0)


class UserOperator(models.Model):
    id = models.AutoField(primary_key=True)
    user_account = models.CharField(max_length=20, default='None')
    operate_type = models.CharField(max_length=20, default='None')
    face_object_type = models.CharField(max_length=20, default='None')
    face_object_id = models.CharField(max_length=50, default='None')
    face_object_msg = models.CharField(max_length=100, default='None')
    operate_time = models.DateTimeField(default=timezone.now)
