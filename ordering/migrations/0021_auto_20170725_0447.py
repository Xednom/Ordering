# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 20:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0020_auto_20170725_0438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 25, 4, 47, 15, 639153), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 25, 4, 47, 15, 638150), verbose_name='Date'),
        ),
    ]
