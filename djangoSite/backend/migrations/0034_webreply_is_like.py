# Generated by Django 3.1.4 on 2021-03-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0033_auto_20210313_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='webreply',
            name='is_like',
            field=models.BooleanField(default=0),
        ),
    ]