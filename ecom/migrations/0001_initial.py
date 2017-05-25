# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('article_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('picture_link', models.CharField(max_length=200)),
                ('sold', models.BooleanField()),
                ('quantity', models.PositiveIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('firstname', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=8)),
                ('dob', models.DateField(verbose_name='dob')),
            ],
        ),
    ]
