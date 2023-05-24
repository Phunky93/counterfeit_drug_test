# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-11-04 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mas_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('m_id', models.IntegerField(primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=255)),
                ('ingredients', models.CharField(max_length=255)),
                ('exp_date', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('dstbtr_lat', models.CharField(max_length=255)),
                ('dstbtr_long', models.CharField(max_length=255)),
            ],
        ),
    ]