# Generated by Django 3.0.8 on 2020-08-10 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_usersite', '0002_auto_20200809_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
    ]
