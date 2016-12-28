# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_data', models.DateField()),
                ('male', models.BooleanField()),
                ('competitor_number', models.CharField(max_length=30)),
                ('last_medical', models.DateField()),
                ('city', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=5)),
                ('street', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('mobile_phone_father', models.CharField(max_length=30)),
                ('mail_father', models.EmailField(max_length=254)),
                ('mobile_phone_mother', models.CharField(max_length=30)),
                ('mail_mother', models.EmailField(max_length=254)),
            ],
        ),
    ]
