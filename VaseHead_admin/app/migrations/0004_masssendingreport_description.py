# Generated by Django 2.0.4 on 2018-04-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_masssendingreport_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='masssendingreport',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
    ]