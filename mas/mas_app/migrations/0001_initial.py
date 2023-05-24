# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-11-04 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('p_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('p_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('p_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('p_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('r_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user_type', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('p_address', models.CharField(max_length=255)),
            ],
        ),
    ]
