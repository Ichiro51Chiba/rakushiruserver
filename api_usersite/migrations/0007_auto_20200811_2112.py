# Generated by Django 3.0.8 on 2020-08-11 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_usersite', '0006_settinguser_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settinguser',
            old_name='user',
            new_name='set_user',
        ),
    ]