# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_auto_20170528_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='createdDate',
            new_name='availability',
        ),
    ]
