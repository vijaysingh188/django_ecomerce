# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-25 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200625_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.DecimalField(decimal_places=2, default=5.99, max_digits=10),
        ),
    ]
