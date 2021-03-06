# Generated by Django 3.0.5 on 2020-05-10 00:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=150)),
                ('blog_image', models.ImageField(upload_to='')),
                ('blog_summary', models.CharField(max_length=250)),
                ('published', models.DateTimeField(default=datetime.datetime(2020, 5, 10, 1, 25, 43, 712816), verbose_name='date published')),
                ('blog_content', models.TextField()),
                ('blog_slug', models.CharField(default=1, max_length=200)),
                ('blog_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='main.Category', verbose_name='Category')),
            ],
        ),
    ]
