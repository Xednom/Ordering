# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 18:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0017_auto_20170721_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='inventory',
        ),
        migrations.AddField(
            model_name='inventory',
            name='balance',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='inventory',
            name='stock_in',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='inventory',
            name='stock_out',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 22, 2, 55, 17, 80521), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 22, 2, 55, 17, 80020), verbose_name='Date'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
