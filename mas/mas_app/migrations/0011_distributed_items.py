# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-11-05 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mas_app', '0010_auto_20221105_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributed_items',
            fields=[
                ('m_id', models.IntegerField(primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=255)),
                ('ingredients', models.CharField(max_length=255)),
                ('exp_date', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('avail_quantity', models.CharField(max_length=255)),
                ('hash_value', models.CharField(max_length=255)),
                ('pharmacy_pub_key', models.CharField(max_length=255)),
                ('dist_pub_key', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
