# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_order_good_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]