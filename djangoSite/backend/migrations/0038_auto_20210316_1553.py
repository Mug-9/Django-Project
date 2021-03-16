# Generated by Django 3.1.4 on 2021-03-16 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0037_auto_20210313_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOperator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_account', models.CharField(default='None', max_length=20)),
                ('operate_type', models.CharField(default='None', max_length=20)),
                ('face_object_type', models.CharField(default='None', max_length=20)),
                ('face_object_id', models.CharField(default='None', max_length=50)),
                ('face_object_msg', models.CharField(default='None', max_length=100)),
                ('operate_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='webreply',
            name='reply_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
