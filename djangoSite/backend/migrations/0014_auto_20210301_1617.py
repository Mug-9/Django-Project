# Generated by Django 3.1.4 on 2021-03-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_proxies'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersofb',
            name='face',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='usersofb',
            name='fans',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usersofb',
            name='name',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='usersofb',
            name='mid',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
