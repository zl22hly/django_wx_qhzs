# Generated by Django 3.2.13 on 2022-08-12 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxcloudrun', '0005_auto_20220812_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counters',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 12, 14, 49, 38, 508190)),
        ),
        migrations.AlterField(
            model_name='counters',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 12, 14, 49, 38, 508190)),
        ),
    ]
