# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 03:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170624_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Post date'),
        ),
    ]
