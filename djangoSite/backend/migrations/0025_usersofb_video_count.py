# Generated by Django 3.1.4 on 2021-03-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_auto_20210311_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersofb',
            name='video_count',
            field=models.IntegerField(default=0),
        ),
    ]
