# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0009_auto_20170710_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_in', models.CharField(max_length=250)),
                ('stock_out', models.CharField(max_length=250)),
                ('balance', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='balance_algicleanz',
            new_name='product_name',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='balance_amfit',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='in_algicleanz',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='in_amfit',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='out_algicleanz',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='out_amfit',
        ),
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordering.Inventory'),
        ),
    ]
