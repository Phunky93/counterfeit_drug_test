# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-11-05 03:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mas_app', '0005_auto_20221105_0923'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Medicines',
            new_name='Medicine',
        ),
    ]