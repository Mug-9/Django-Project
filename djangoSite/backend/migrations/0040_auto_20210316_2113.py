# Generated by Django 3.1.4 on 2021-03-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0039_webcomment_like_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcomment',
            name='like_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改日期'),
        ),
    ]
