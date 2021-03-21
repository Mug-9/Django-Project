# Generated by Django 3.1.4 on 2021-03-21 05:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0040_auto_20210316_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFans',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('mid', models.CharField(default='None', max_length=20, unique=True)),
                ('name', models.CharField(default='None', max_length=20)),
                ('fans', models.IntegerField(default=0)),
            ],
        ),
    ]