# Generated by Django 3.1.4 on 2021-03-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0034_webreply_is_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='webreply',
            name='is_dislike',
            field=models.BooleanField(default=0),
        ),
    ]
