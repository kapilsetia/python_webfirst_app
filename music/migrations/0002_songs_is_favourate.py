# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='is_favourate',
            field=models.BooleanField(default=False),
        ),
    ]
