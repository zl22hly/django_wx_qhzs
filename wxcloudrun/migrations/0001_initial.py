# Generated by Django 3.2.13 on 2022-08-18 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, max_length=11)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 11, 41, 50, 408454))),
                ('updatedAt', models.DateTimeField(default=datetime.datetime(2022, 8, 18, 11, 41, 50, 408454))),
            ],
            options={
                'db_table': 'Counters',
            },
        ),
    ]
