# Generated by Django 3.1.4 on 2021-03-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_auto_20210311_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersofb',
            name='archive_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usersofb',
            name='archive_view',
            field=models.IntegerField(default=0),
        ),
    ]