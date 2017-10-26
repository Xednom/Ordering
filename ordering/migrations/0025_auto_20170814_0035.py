# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 16:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0024_auto_20170811_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name_of_recipient',
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='middle_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 8, 14, 0, 35, 59, 698377), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 8, 14, 0, 35, 59, 695369), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipment_provider',
            field=models.CharField(choices=[('LBC', 'LBC'), ('GO', 'GO'), ('JRS Express', 'JRS Express'), ('Zen', 'Zen'), ('Philpost', 'Philpost'), ('EMS', 'EMS'), ('Fedex', 'Fedex'), ('DHL', 'DHL')], max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(default=0),
        ),
    ]