# Generated by Django 3.1.4 on 2020-12-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20201228_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('number', models.IntegerField()),
            ],
        ),
    ]
