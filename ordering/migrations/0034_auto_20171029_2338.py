# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 15:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0033_auto_20170910_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(b'On going', b'On going'), (b'Shipping', b'Shipping'), (b'On hold', b'On hold')], default=b'Status', max_length=100),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name=b'Date'),
        ),
    ]