# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20160930_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prjspec',
            name='f01',
            field=models.CharField(default='.', max_length=200, verbose_name='主題'),
        ),
        migrations.AlterField(
            model_name='prjspec',
            name='f02',
            field=models.CharField(default='.', max_length=2000, verbose_name='說明'),
        ),
    ]