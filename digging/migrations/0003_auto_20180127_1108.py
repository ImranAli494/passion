# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-27 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digging', '0002_stock_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_products',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stock_products',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
