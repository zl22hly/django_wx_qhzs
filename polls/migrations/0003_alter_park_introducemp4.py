# Generated by Django 3.2.13 on 2022-08-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_park_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='introduceMP4',
            field=models.CharField(max_length=600, verbose_name='介绍影片'),
        ),
    ]