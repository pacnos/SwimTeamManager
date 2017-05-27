# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminBackend', '0004_mailsettings_medical_mail_cc'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_host', models.CharField(max_length=1024, verbose_name='EMAIL_HOST')),
                ('email_port', models.PositiveSmallIntegerField(default=587, verbose_name='EMAIL_PORT')),
                ('email_host_user', models.CharField(max_length=255, verbose_name='EMAIL_HOST_USER')),
                ('email_host_password', models.CharField(max_length=255, verbose_name='EMAIL_HOST_PASSWORD')),
                ('email_security', models.CharField(choices=[('NO', 'None'), ('TLS', 'TLS'), ('SSL', 'SSL')], default='NO', max_length=2)),
                ('email_sender_name', models.EmailField(max_length=254, verbose_name='EMAIL_SENDER')),
                ('email_sender_mail', models.EmailField(max_length=254, verbose_name='EMAIL_SENDER')),
            ],
        ),
    ]