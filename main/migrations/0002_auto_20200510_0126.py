# Generated by Django 3.0.5 on 2020-05-10 00:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 1, 26, 9, 796655), verbose_name='date published'),
        ),
    ]