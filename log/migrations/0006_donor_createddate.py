# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_auto_20170521_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
