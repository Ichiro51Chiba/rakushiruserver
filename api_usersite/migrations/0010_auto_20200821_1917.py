# Generated by Django 3.0.8 on 2020-08-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0004_remove_company_user_com'),
        ('api_usersite', '0009_auto_20200814_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.AddField(
            model_name='user',
            name='companies',
            field=models.ManyToManyField(blank=True, null=True, to='api_user.Company'),
        ),
    ]