# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminBackend', '0006_auto_20170527_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsettings',
            name='email_sender_name',
            field=models.CharField(max_length=200, verbose_name='EMAIL_SENDER'),
        ),
    ]
