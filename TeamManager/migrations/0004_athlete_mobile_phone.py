# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamManager', '0003_auto_20161228_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]