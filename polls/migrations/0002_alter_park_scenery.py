# Generated by Django 3.2.13 on 2022-09-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='scenery',
            field=models.JSONField(blank=True, default=list, null=True, verbose_name='景点'),
        ),
    ]
