# Generated by Django 3.0.8 on 2020-08-10 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0003_company_user_com'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='user_com',
        ),
    ]