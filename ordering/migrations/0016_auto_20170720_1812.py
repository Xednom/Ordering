# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 10:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0015_auto_20170718_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 20, 18, 12, 52, 21096), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
