# Generated by Django 3.0.4 on 2020-04-21 13:10

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to=blog.models.upload_location),
        ),
    ]
