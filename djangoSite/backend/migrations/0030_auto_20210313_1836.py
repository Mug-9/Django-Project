# Generated by Django 3.1.4 on 2021-03-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_auto_20210313_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_header',
            field=models.CharField(max_length=50),
        ),
    ]
