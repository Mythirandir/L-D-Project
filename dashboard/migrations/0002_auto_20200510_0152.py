# Generated by Django 3.0.5 on 2020-05-10 00:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 1, 52, 17, 359202), verbose_name='Date of Bid'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 1, 52, 17, 358203), verbose_name='Project published on '),
        ),
        migrations.AlterField(
            model_name='project',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 1, 52, 17, 358203), verbose_name='Project expiries on'),
        ),
    ]
