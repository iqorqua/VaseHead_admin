# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-21 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_masssendingreport_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMessaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256)),
                ('user_id', models.CharField(max_length=100)),
                ('messages_count', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=256)),
                ('good_id', models.IntegerField()),
                ('good_color', models.CharField(max_length=100)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
