# Generated by Django 3.1.4 on 2020-12-28 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='account',
            new_name='email',
        ),
    ]
