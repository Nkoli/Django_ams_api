# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-08 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams_api', '0002_auto_20171231_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='grade',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]
