# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0016_auto_20170720_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 21, 20, 15, 32, 770063), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 21, 20, 15, 32, 769561), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
