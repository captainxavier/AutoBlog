# Generated by Django 3.0.4 on 2020-04-20 21:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200420_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=accounts.models.upload_profile_pic),
        ),
    ]
