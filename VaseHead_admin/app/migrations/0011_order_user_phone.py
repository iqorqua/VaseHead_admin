# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_client_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_phone',
            field=models.CharField(default=380633576207, max_length=13),
            preserve_default=False,
        ),
    ]